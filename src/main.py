import os
import sys
from io import StringIO
import subprocess
from multiprocessing import freeze_support
from threading import Thread, Lock

import json
from time import ctime, sleep
from traceback import print_tb

import cv2 as cv
import numpy as np

import wx
from gui import _Frame, _LoadingDialog, _AboutDialog
from gui_help import SetHelpProvider

from edge import ProcessingInit
#from edge import show


APP_NAME = u"chromaLine"
APP_NAME_CN = u"炫彩剪影"
APP_VERSION = u"v1.0.0"
LAST_MODIFICATION = u"Mar. 20, 2023"
HELP_LINK = u"https://docs.opencv.org/4.5.4/d2/d96/tutorial_py_table_of_contents_imgproc.html"
IMG_WINDOW_TITLE = u"Image preview"
PREVIEW_SIZE = 600
OUTPUT_SUFFIX = u'_chroma.jpg'

work_path = os.getcwd()
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(os.getenv('TEMP'), '%s.log' % APP_NAME)


class logging():

    def __init__(self, path):
        self.log_path = path
        self.buffer = StringIO()
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        sys.stdout = self.buffer
        sys.stderr = self.buffer

    def __enter__(self):
        return self

    def __exit__(self, type, obj, trace):
        if trace:
            print_tb(trace)
            sys.exc_clear()
        self.close()
        return True

    def close(self):
        sys.stdout = self._stdout
        sys.stderr = self._stderr
        if self.buffer.tell():
            if os.path.exists(self.log_path):
                log = open(self.log_path, 'a', encoding='utf-8')
            else:
                log = open(self.log_path, 'w', encoding='utf-8')
                log.write('####%s\n' % self.log_path)
            log.write('\n////%s\n' % ctime())
            log.write(self.buffer.read())
            log.write('\n')
            log.close()
        self.buffer.close()


class imgFrame(wx.Frame):

    def __init__(self, parent):
        super(imgFrame, self).__init__(parent=parent, title=IMG_WINDOW_TITLE, \
                                       size=wx.Size(PREVIEW_SIZE, PREVIEW_SIZE), \
                                       style=wx.CAPTION | wx.SYSTEM_MENU | wx.MINIMIZE_BOX | \
                                       wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.FRAME_FLOAT_ON_PARENT)
        self.SetIcon(wx.Icon(os.path.join(base_path, 'appIcon.ico')))
        self.img = wx.StaticBitmap(self)
        #self.Centre(wx.BOTH)
        self.click_hook = None
        self.img.Bind(wx.EVT_LEFT_DOWN, self.click)
        self.Bind(wx.EVT_CLOSE, self.hide)
        self.width = -1
        self.height = -1

    def show(self, img):
        height, width = img.shape[ : 2]
        bitmap = wx.Bitmap.FromBuffer(width, height, img)
        if width != self.width or height != self.height:
            self.width = width
            self.height = height
            self.SetSize(wx.Size(width + 8, height + 30))    # +16, +38
        self.img.SetBitmap(bitmap)
        self.img.Layout()
        if not self.IsShown():
            self.Show()
            #self.ShowWithEffect(wx.SHOW_EFFECT_BLEND, 300)

    def hide(self, evt):
        self.Hide()
        #self.HideWithEffect(wx.SHOW_EFFECT_BLEND, 300)

    def click(self, evt):
        if self.click_hook:
            self.click_hook(*evt.GetPosition())


class imgProxy(Thread):

    def __init__(self, parent):
        super(imgProxy, self).__init__(name='imgProxyThread')
        self.img = [None] * 4
        self.index = -1
        self.showing = -1
        self._loaded = False
        self._wait_time = int(PREVIEW_SIZE / 10)
        self._lock = Lock()
        self._loop = True
        self._p, self._pipe = ProcessingInit()
        self.frame = imgFrame(parent)
        self.start()

    def _show(self, index):
        self.showing = index
        img = self.img[index]
        if isinstance(img, np.ndarray):
            img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            with self._lock: self.frame.show(img_rgb)

    def process(self, img):
        index = self.index
        self.index = -1
        self.img[3] = None
        self._pipe.send(('set', 0, img))
        self._pipe.send(('get', 3))
        while True:    # 阻塞
            if isinstance(self.img[3], np.ndarray):
                output = self.img[3]
                break
        self.index = index
        self._pipe.send(('set', 0, self.img[0]))
        self._pipe.send(('get', index))
        return output

    def has_img(self):
        return self._loaded

    def load(self, img, config_list=[]):
        self._loaded = False
        if isinstance(img, np.ndarray):
            with self._lock:
                self._pipe.send(('set', 0, img))
                i = 0; n = len(config_list)
                while i < n:
                    self._pipe.send(('set', i + 1, config_list[i]))
                    i += 1
            self.index = 1
            self.img[0] = img
            self._loaded = True

    def set(self, index, config):
        if self._loaded:
            self._pipe.send(('set', index, config))

    def show(self, index):
        if self._loaded:
            if index == 0:
                self._show(index)
            else:
                self.index = index
                self._pipe.send(('get', index))

    def run(self):
        msg_img = None
        flag = -1
        while self._loop:
            while self._pipe.poll() :
                msg = self._pipe.recv()
                if msg[0] == 'img':
                    msg_img = msg
                    if msg[1] != flag:
                        flag = msg[1]
                        break
                elif msg[0] == 'info':
                    with self._lock:
                        print(msg[2])
            if msg_img:
                self.img[msg_img[1]] = msg_img[2]
                if self.index == msg_img[1]:
                    self._show(self.index)
                msg_img = None
                sleep(0.01)
        self._pipe.send(('exit', ))

    def exit(self):
        self._loop = False
        self._p.join()
        self._p.close()


class mainFrame(_Frame):

    def __init__(self):
        super(mainFrame, self).__init__(None)
        self.SetTitle(f"{APP_NAME} {APP_VERSION}")
        self.m_statusBar.SetStatusWidths([-3, -1])
        self.SetIcon(wx.Icon(os.path.join(base_path, 'appIcon.ico')))

        self.m_button31.Disable()
        self.m_button41.Disable()
        self.fgSizer1.Hide(self.bSizer6, True)
        self.bSizer2.Layout()
        self.fgSizer2.Hide(self.gSizer1, True)
        self.fgSizer2.Hide(self.bSizer27, True)
        self.fgSizer2.Hide(self.bSizer30, True)
        self.bSizer10.Layout()
        self.fgSizer3.Hide(self.bSizer35, True)
        self.bSizer33.Layout()
        self.m_slider16.Disable()
        
        self.m_textCtrl1.SetHint("Press ENTER to open")
        drop_target = FileDrop(self.m_panel7, self._file_load)
        self.m_panel7.SetDropTarget(drop_target)
        self.Layout()
        
        self._saturation_mode = True
        self._choice_maplist1 = ['g', 'm']
        self._choice_maplist2 = [1, 2, 3, 4]
        self._choice_maplist3 = ['h', 's', 'v']
        self._supported_format = ['bmp', 'dib', 'exr', 'hdr', 'jp2', 'jpe', 'jpeg', 'jpg', 'pbm', 'pfm', 'pgm', 'pic', 'png', 'pnm', 'ppm', 'pxm', 'ras', 'sr', 'tif', 'tiff', 'webp']
        self._wildcard = '''\
All Image|*.bmp;*.dib;*.exr;*.hdr;*.jp2;*.jpe;*.jpeg;*.jpg;*.pbm;*.pfm;*.pgm;*.pic;*.png;*.pnm;*.ppm;*.pxm;*.ras;*.sr;*.tif;*.tiff;*.webp|\
Windows bitmaps - *.bmp, *.dib|*.bmp;*.dib|\
JPEG files - *.jpeg, *.jpg, *.jpe|*.jpeg;*.jpg;*.jpe|\
JPEG 2000 files - *.jp2|*.jp2|\
Portable Network Graphics - *.png|*.png|\
WebP - *.webp|*.webp|\
Portable image format - *.pbm, *.pgm, *.ppm, *.pxm, *.pnm|*.pbm;*.pgm;*.ppm;*.pxm;*.pnm|\
PFM files - *.pfm|*.pfm|\
Sun rasters - *.sr, *.ras|*.sr;*.ras|\
TIFF files - *.tiff, *.tif|*.tiff;*.tif|\
OpenEXR Image files - *.exr|*.exr|\
Radiance HDR - *.hdr, *.pic|*.hdr;*.pic'''
        
        self.active_page = 0
        self.config = [{'method': 'bilateral', 's_space': 8, 's_value': 20},
                       {'method': 'adaThresh', 'C': 10, 'size': 9, 'thinning': False, 'morphGrad': False},
                       {'method': 'hsv', 'h_method': 'linear', 'direction': 1, 'period': 1.0, 'hue_offset': 0, 'phase': 'v', 'lower': 0.0}]
        self.file_list = []
        self.file_index = -1
        self.imgP = imgProxy(self)
        self.img = None
        self.img_preview = None
        self.img_name = None

    def file_choose(self, evt):
        global work_path
        dlg = wx.FileDialog(self, "Choose image files", work_path, wildcard=self._wildcard,
                            style=wx.FD_DEFAULT_STYLE|wx.FD_MULTIPLE|wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            file_list = dlg.GetPaths()
            work_path = os.path.dirname(file_list[0])
            self._file_load(file_list)
        dlg.Destroy()

    def file_path_edit(self, evt):
        global work_path
        path = evt.GetEventObject().GetValue()
        if os.path.exists(path):
            work_path = os.path.dirname(path)
            self._file_load([path])

    def _file_load(self, file_list):
        print('Read Image: ', file_list)
        self.imgP.frame.hide(None)
        self.file_list = file_list
        self.file_index = -1
        num = len(file_list)
        if num > 1:
            self.m_textCtrl1.Disable()
        else:
            self.m_textCtrl1.Enable()
        self.m_staticText7.SetLabel(str(num))
        self.m_button31.Disable()
        self.m_button41.Enable(num > 1)
        self._file_pick(0)
    
    def file_previous(self, evt):
        if self.file_index <= 1:
            evt.GetEventObject().Disable()
            index = 0
        else:
            index = self.file_index - 1
        self.m_button41.Enable()
        self._file_pick(index)

    def file_next(self, evt):
        if self.file_index >= len(self.file_list) - 2:
            evt.GetEventObject().Disable()
            index = len(self.file_list) - 1
        else:
            index = self.file_index + 1
        self.m_button31.Enable()
        self._file_pick(index)

    def _file_pick(self, index):
        if self.file_index == index: return
        self.file_index = index
        try:
            self.img_name = os.path.basename(self.file_list[index])
            buf = np.fromfile(self.file_list[index], dtype=np.uint8)
            self.img = cv.imdecode(buf, cv.IMREAD_COLOR)
            max_length = max(self.img.shape)
            if max_length > PREVIEW_SIZE:
                scale = PREVIEW_SIZE / max_length
                self.img_preview = cv.resize(self.img, (0, 0), fx=scale, fy=scale, interpolation=cv.INTER_AREA)
            else:
                self.img_preview = self.img
        except Exception as e:
            print(repr(e))
            self.m_textCtrl1.SetValue('')
            self.m_textCtrl1.UnsetToolTip()
            self.imgP.load(None)
            self.imgP.frame.SetTitle(IMG_WINDOW_TITLE)
        else:
            self.m_notebook4.ChangeSelection(0)
            self.active_page = 0
            self.m_textCtrl1.SetValue(self.file_list[index])
            self.m_textCtrl1.SetToolTip(wx.ToolTip(self.file_list[index]))
            self.imgP.load(self.img_preview, self.config)
            self.imgP.frame.SetTitle(\
                f"{IMG_WINDOW_TITLE}  -  {self.img_name} | {self.img.shape[1]}x{self.img.shape[0]}")
        finally:
            self.m_staticText6.SetLabel(str(index + 1))

    def page_change(self, evt):
        self.active_page = self.m_notebook4.GetSelection()
        self.imgP.show(self.active_page + 1)

    def img_origin(self, evt):
        if self.imgP.showing == 0:
            self.imgP.show(self.active_page + 1)
        elif self.imgP.showing > 0:
            self.imgP.show(0)

    def activate(self, evt):
        if evt.GetActive():
            self.imgP.frame.click_hook = None

    def _img_update(self, index):
        self.imgP.set(index + 1, self.config[index])

    def noise_origin(self, evt):
        self.m_panel5.Hide()
        self.fgSizer1.Hide(self.bSizer5, True)
        self.fgSizer1.Hide(self.bSizer6, True)
        self.bSizer2.Layout()
        self.config[0]['method'] = 'origin'
        self._img_update(0)

    def noise_bilateral(self, evt):
        self.fgSizer1.Hide(self.bSizer6, True)
        self.fgSizer1.Show(self.bSizer5, recursive=True)
        self.m_panel5.Show()
        self.bSizer2.Layout()
        self.config[0]['method'] = 'bilateral'
        self.noise_bilateral_update(None)

    def noise_bilateral_update(self, evt):
        self.config[0]['s_space'] = self.m_slider1.GetValue()
        self.config[0]['s_value'] = self.m_slider2.GetValue()
        self._img_update(0)

    def noise_median(self, evt):
        self.fgSizer1.Hide(self.bSizer5, True)
        self.fgSizer1.Show(self.bSizer6, recursive=True)
        self.m_panel5.Show()
        self.bSizer2.Layout()
        self.config[0]['method'] = 'median'
        self.noise_median_update(None)

    def noise_median_update(self, evt):
        size = 2 *  self.m_slider3.GetValue() + 1
        self.m_staticText331.SetLabel(str(size))
        self.config[0]['size'] = size
        self._img_update(0)

    def edge_adaThresh(self, evt):
        self.fgSizer2.Hide(self.gSizer1, True)
        self.fgSizer2.Hide(self.bSizer27, True)
        self.fgSizer2.Hide(self.bSizer30, True)
        self.fgSizer2.Show(self.bSizer67, recursive=True)
        self.m_checkBox1.Enable()
        self.bSizer10.Layout()
        self.config[1]['method'] = 'adaThresh'
        self.edge_adaThresh_update1(None)
        self.edge_adaThresh_update2(None)

    def edge_adaThresh_update1(self, evt):
        self.config[1]['ada'] = self._choice_maplist1[self.m_choice3.GetSelection()]
        self.config[1]['C'] = self.m_slider4.GetValue()
        self._edge_advance_abort()
        if evt: self._img_update(1)

    def edge_adaThresh_update2(self, evt):
        size = 2 * self.m_slider5.GetValue() + 1
        self.m_staticText39.SetLabel(str(size))
        self.config[1]['size'] = size
        self._edge_advance_abort()
        self._img_update(1)

    def edge_Canny(self, evt):
        self.fgSizer2.Hide(self.bSizer67, True)
        self.fgSizer2.Hide(self.bSizer27, True)
        self.fgSizer2.Hide(self.bSizer30, True)
        self.fgSizer2.Show(self.gSizer1, recursive=True)
        self.m_checkBox1.Disable()
        self.bSizer10.Layout()
        self.config[1]['method'] = 'Canny'
        self.edge_Canny_update1(None)
        self.edge_Canny_update2(None)

    def edge_Canny_update1(self, evt):
        a = self.m_slider7.GetValue()
        b = self.m_slider6.GetValue()
        if a >= b and evt:
            if evt.GetEventObject() == self.m_slider7:
                self.m_slider6.SetValue(a); b = a
            else:
                self.m_slider7.SetValue(b); a = b
        self.config[1]['lower'] = a
        self.config[1]['upper'] = b
        self._edge_advance_abort()
        if evt: self._img_update(1)

    def edge_Canny_update2(self, evt):
        size = 2 * self.m_slider8.GetValue() + 1
        self.m_staticText36.SetLabel(str(size))
        self.config[1]['size'] = size
        self._edge_advance_abort()
        self._img_update(1)

    def edge_Scharr(self, evt):
        self.fgSizer2.Hide(self.bSizer67, True)
        self.fgSizer2.Hide(self.gSizer1, True)
        self.fgSizer2.Hide(self.bSizer30, True)
        self.fgSizer2.Show(self.bSizer27, recursive=True)
        self.m_checkBox1.Disable()
        self.bSizer10.Layout()
        self.config[1]['method'] = 'Scharr'
        self.edge_Scharr_update(None)

    def edge_Scharr_update(self, evt):
        a = self.m_slider9.GetValue()
        b = self.m_slider10.GetValue()
        if b - a <= 1 and evt:
            if evt.GetEventObject() == self.m_slider9:
                b = a + 1; self.m_slider10.SetValue(b)
            else:
                a = b - 1; self.m_slider9.SetValue(a)
        self.config[1]['a'] = a
        self.config[1]['b'] = b
        self._edge_advance_abort()
        self._img_update(1)

    def edge_LoG(self, evt):
        self.fgSizer2.Hide(self.bSizer67, True)
        self.fgSizer2.Hide(self.gSizer1, True)
        self.fgSizer2.Hide(self.bSizer27, True)
        self.fgSizer2.Show(self.bSizer30, recursive=True)
        self.m_checkBox1.Disable()
        self.bSizer10.Layout()
        self.config[1]['method'] = 'LoG'
        self.edge_LoG_update(None)

    def edge_LoG_update(self, evt):
        a = self.m_slider12.GetValue()
        b = self.m_slider11.GetValue()
        if b - a <= 1 and evt:
            if evt.GetEventObject() == self.m_slider12:
                b = a + 1; self.m_slider11.SetValue(b)
            else:
                a = b - 1; self.m_slider12.SetValue(a)
        self.config[1]['a'] = a
        self.config[1]['b'] = b
        self._edge_advance_abort()
        self._img_update(1)

    def _edge_advance_abort(self):
        if self.config[1]['thinning']:
            self.m_checkBox1.SetValue(False)
            self.config[1]['thinning'] = False
        if self.config[1]['morphGrad']:
            self.m_checkBox2.SetValue(False)
            self.config[1]['morphGrad'] = False

    def edge_advance_update(self, evt):
        self.config[1]['thinning'] = self.m_checkBox1.GetValue()
        self.config[1]['morphGrad'] = self.m_checkBox2.GetValue()
        if evt: self._img_update(1)

    def color_static(self, evt):
        self.m_panel8.Hide()
        self.fgSizer3.Hide(self.bSizer38, True)
        self.fgSizer3.Hide(self.bSizer35, True)
        self.bSizer33.Layout()
        self.config[2]['h_method'] = 'static'
        self._img_update(2)

    def color_linear(self, evt):
        self.fgSizer3.Hide(self.bSizer35, True)
        self.fgSizer3.Show(self.bSizer38, recursive=True)
        self.m_panel8.Show()
        self.bSizer33.Layout()
        self.config[2]['h_method'] = 'linear'
        self.color_linear_update(None)

    def color_linear_update(self, evt):
        period = round(10 ** (self.m_slider14.GetValue() / 20), 2)
        self.m_staticText23.SetLabel(str(period)[: 4])
        self.config[2]['direction'] = self._choice_maplist2[self.m_choice1.GetSelection()]
        self.config[2]['period'] = period
        self._img_update(2)

    def color_maze(self, evt):
        self.fgSizer3.Hide(self.bSizer38, True)
        self.fgSizer3.Show(self.bSizer35, recursive=True)
        self.m_panel8.Show()
        self.bSizer33.Layout()
        self.config[2]['h_method'] = 'maze'
        self.color_maze_update(None)

    def color_maze_update(self, evt):
        self.config[2]['diag_len'] = self.m_slider13.GetValue()
        self.config[2]['blur'] = self.m_checkBox3.GetValue()
        self._img_update(2)

    def color_maze_center(self, evt):
        if not self.imgP.has_img(): return
        m, n, _ = self.img.shape
        if evt:
            m_p, n_p, _ = self.img_preview.shape
            def set_center(x, y):
                _x = y / m_p
                _y = x / n_p
                self.m_textCtrl2.SetValue(str((int(_y * n), int(_x * m))))
                self.config[2]['center'] = (_x, _y)
                self._img_update(2)
            self.imgP.frame.click_hook = set_center
            #self.imgP.frame.Raise()
        else:
            center = self.config[2]['center']
            self.m_textCtrl2.SetValue(str((int(center[1] * n), int(center[0] * m))))

    def color_advance_hue_update(self, evt):
        self.config[2]['hue_offset'] = self.m_slider15.GetValue()
        if evt: self._img_update(2)

    def color_advance_sat(self, evt):
        self._saturation_mode = self.m_checkBox4.GetValue()
        if self._saturation_mode:
            self.m_slider16.Disable()
            self.bSizer49.Show(self.m_panel9, recursive=True)
            self.bSizer33.Layout()
            if self.config[2].get('saturation') != None:
                self.config[2]['saturation'] = None
        else:
            self.bSizer49.Hide(self.m_panel9, True)
            self.bSizer33.Layout()
            self.m_slider16.Enable()
        self.color_advance_sat_update(evt)

    def color_advance_sat_update(self, evt):
        if self._saturation_mode:
            lower = round(self.m_slider17.GetValue() / 40, 3)
            self.m_staticText31.SetLabel(str(lower)[: 4])
            self.config[2]['phase'] = self._choice_maplist3[self.m_choice2.GetSelection()]
            self.config[2]['lower'] = lower
        else:
            self.config[2]['saturation'] = self.m_slider16.GetValue()
        if evt: self._img_update(2)

    def img_export(self, evt):
        if not self.imgP.has_img(): return
        img = self.imgP.process(self.img)
        if isinstance(evt, wx.Event):
            output_path = os.path.join(work_path, \
                                       '.'.join(self.img_name.split('.')[: -1]) + OUTPUT_SUFFIX)
        else:
            output_path = evt
        print('Write Image:', output_path)
        cv.imencode('.jpg', img)[1].tofile(output_path)
        showFile(output_path)

    def img_export_all(self, evt):
        if not self.imgP.has_img(): return
        if isinstance(evt, wx.Event):
            fileBatchExport(self, work_path)
        else:
            fileBatchExport(self, evt)

    def set_default(self, evt):
        if self.active_page == 0:
            self.m_radioBtn2.SetValue(True)
            self.m_slider1.SetValue(8)
            self.m_slider2.SetValue(20)
            self.m_slider3.SetValue(1)
            self.noise_bilateral(None)
        elif self.active_page == 1:
            self.m_radioBtn4.SetValue(True)
            self.m_choice3.SetSelection(0)
            self.m_slider4.SetValue(10)
            self.m_slider5.SetValue(4)
            self.m_slider7.SetValue(20)
            self.m_slider6.SetValue(40)
            self.m_slider8.SetValue(3)
            self.m_slider9.SetValue(0)
            self.m_slider10.SetValue(100)
            self.m_slider12.SetValue(0)
            self.m_slider11.SetValue(100)
            self.m_checkBox1.SetValue(False)
            self.m_checkBox2.SetValue(False)
            self.edge_advance_update(None)
            self.edge_adaThresh(None)
        elif self.active_page == 2:
            self.m_radioBtn9.SetValue(True)
            self.m_choice1.SetSelection(0)
            self.m_slider14.SetValue(0)
            self.m_slider13.SetValue(30)
            self.m_checkBox3.SetValue(True)
            self.m_textCtrl2.SetValue('(0, 0)')
            self.config[2]['center'] = (0, 0)
            self.m_slider15.SetValue(0)
            self.m_checkBox4.SetValue(True)
            self.m_slider16.SetValue(255)
            self.m_choice2.SetSelection(2)
            self.m_slider17.SetValue(0)
            self.color_advance_hue_update(None)
            self.color_advance_sat(None)
            self.color_linear(None)

    def m_file_choose(self, evt):
        self.file_choose(evt)
    
    def m_folder_choose(self, evt):
        global work_path
        dlg = wx.DirDialog(self, "Choose image folder", work_path, \
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            work_path = dlg.GetPath()
            file_list = []
            for file in os.listdir(work_path):
                if file.split('.')[-1] in self._supported_format:
                    file_list.append(os.path.join(work_path, file))
            self._file_load(file_list)
        dlg.Destroy()
    
    def m_img_export(self, evt):
        if self.imgP.has_img():
            dlg = wx.FileDialog(self, "Export image file", work_path, \
                                '.'.join(self.img_name.split('.')[: -1]) + OUTPUT_SUFFIX, \
                                wildcard='JPEG files - *.jpeg, *.jpg, *.jpe|*.jpeg;*.jpg;*.jpe|All files - *.*|*.*', \
                                style=wx.FD_DEFAULT_STYLE)
            if overwriteConfirm(dlg):
                self.img_export(dlg.GetPath())
        else:
            dlg = wx.MessageDialog(self, "No image available to export.", \
                                   "Message", wx.OK|wx.ICON_WARNING)
            dlg.ShowModal()
        dlg.Destroy()
    
    def m_img_export_all(self, evt):
        if self.imgP.has_img():
            dlg = wx.DirDialog(self, "Export all image files", work_path, \
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                self.img_export_all(dlg.GetPath())
        else:
            dlg = wx.MessageDialog(self, "No image available to export.", \
                                   "Message", wx.OK|wx.ICON_WARNING)
            dlg.ShowModal()
        dlg.Destroy()
    
    def m_enable_tooltips(self, evt):
        flag =  self.m_menuItem11.IsChecked()
        wx.ToolTip.Enable(flag)
    
    def m_exit(self, evt):
        self.Close()
    
    def m_config_save(self, evt):
        dlg = wx.FileDialog(self, "Write config file", work_path, 'chromaLineConfig.json', \
                            wildcard='JSON File - *.json|*.json|All files - *.*|*.*', \
                            style=wx.FD_DEFAULT_STYLE)
        if overwriteConfirm(dlg):
            config_dic = {'noiseSmooth': self.config[0],
                          'edgeExtract': self.config[1],
                          'colorRender': self.config[2]}
            with open(dlg.GetPath(), 'w', encoding='utf-8') as f:
                json.dump(config_dic, f, indent=4, ensure_ascii=False, \
                           sort_keys=False, separators=(',',': '))
        dlg.Destroy()
    
    def _ctrl_operate(self, config_dic):
        config = config_dic.get('noiseSmooth')
        if config and config.get('method'):
            if config['method'] == 'origin':
                self.m_radioBtn1.SetValue(True)
                self.noise_origin(None)
            elif config['method'] == 'bilateral':
                self.m_radioBtn2.SetValue(True)
                if config.get('s_space'):
                    self.m_slider1.SetValue(config['s_space'])
                if config.get('s_value'):
                    self.m_slider2.SetValue(config['s_value'])
                self.noise_bilateral(None)
            elif config['method'] == 'median':
                self.m_radioBtn3.SetValue(True)
                if config.get('size'):
                    self.m_slider3.SetValue(int((config['size'] - 1) * 0.5))
                self.noise_median(None)
        config = config_dic.get('edgeExtract')
        if config and config.get('method'):
            if config.get('thinning') != None:
                self.m_checkBox1.SetValue(config['thinning'])
            if config.get('morphGrad') != None:
                self.m_checkBox2.SetValue(config['morphGrad'])
            self.edge_advance_update(None)
            if config['method'] == 'adaThresh':
                self.m_radioBtn4.SetValue(True)
                if  config.get('ada'):
                    self.m_choice3.SetSelection(self._choice_maplist1.index(config['ada']))
                if config.get('C') != None:
                    self.m_slider4.SetValue(config['C'])
                if config.get('size'):
                    self.m_slider5.SetValue(int((config['size'] - 1) * 0.5))
                self.edge_adaThresh(None)
            elif config['method'] == 'Canny':
                self.m_radioBtn5.SetValue(True)
                if config.get('lower'):
                    self.m_slider7.SetValue(config['lower'])
                if config.get('upper'):
                    self.m_slider6.SetValue(config['upper'])
                if config.get('size'):
                    self.m_slider8.SetValue(int((config['size'] - 1) * 0.5))
                self.edge_Canny(None)
            elif config['method'] == 'Scharr':
                self.m_radioBtn6.SetValue(True)
                if config.get('a') != None:
                    self.m_slider9.SetValue(config['a'])
                if config.get('b'):
                    self.m_slider10.SetValue(config['b'])
                self.edge_Scharr(None)
            elif config['method'] == 'LoG':
                self.m_radioBtn7.SetValue(True)
                if config.get('a') != None:
                    self.m_slider12.SetValue(config['a'])
                if config.get('b'):
                    self.m_slider11.SetValue(config['b'])
                self.edge_LoG(None)
        config = config_dic.get('colorRender')
        if config and config.get('h_method'):
            if config.get('hue_offset') != None:
                self.m_slider15.SetValue(config['hue_offset'])
            if config.get('saturation') == None:
                self.m_checkBox4.SetValue(True)
                if config.get('phase'):
                    self.m_choice2.SetSelection(self._choice_maplist3.index(config['phase']))
                if config.get('lower') != None:
                    self.m_slider17.SetValue(int(config['lower'] * 40))
            else:
                self.m_checkBox4.SetValue(False)
                self.m_slider16.SetValue(config['saturation'])
            self.color_advance_hue_update(None)
            self.color_advance_sat(None)
            if config['h_method'] == 'static':
                self.m_radioBtn8.SetValue(True)
                self.color_static(None)
            elif config['h_method'] == 'linear':
                self.m_radioBtn9.SetValue(True)
                if config.get('direction'):
                    self.m_choice1.SetSelection(self._choice_maplist2.index(config['direction']))
                if config.get('period'):
                    self.m_slider14.SetValue(int(np.log10(config['period']) * 20))
                self.color_linear(None)
            elif config['h_method'] == 'maze':
                self.m_radioBtn10.SetValue(True)
                if config.get('diag_len'):
                    self.m_slider13.SetValue(config['diag_len'])
                if config.get('blur'):
                    self.m_checkBox3.SetValue(config['blur'])
                if config.get('center'):
                    self.config[2]['center'] = config['center']
                    self.color_maze_center(None)
                self.color_maze(None)
    
    def m_config_load(self, evt):
        dlg = wx.FileDialog(self, "Read config file", work_path, wildcard='JSON File - *.json|*.json', \
                            style=wx.FD_DEFAULT_STYLE|wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            with open(dlg.GetPath(), 'r', encoding='utf-8') as f:
                config_dic = json.load(f)
            assert set(config_dic.keys()) == {'noiseSmooth', 'edgeExtract', 'colorRender'}, 'unmatched key'
            self._ctrl_operate(config_dic)
        dlg.Destroy()
    
    def m_log(self, evt):
        if os.path.exists(log_path):
            subprocess.Popen('explorer "%s"' % log_path)
    
    def m_help(self, evt):
        subprocess.Popen('explorer "%s"' % HELP_LINK)
    
    def m_about(self, evt):
        dlg = AboutFrame(self)
        dlg.ShowModal()
        dlg.Destroy()


class FileDrop(wx.FileDropTarget):

    def __init__(self, target, function):
        wx.FileDropTarget.__init__(self)
        self.target = target
        self.func = function

    def OnDropFiles(self, x, y, filenames):
        self.func(filenames)
        return True


def overwriteConfirm(dialogObj):
    overwrite = wx.ID_CANCEL
    while dialogObj.ShowModal() in (wx.ID_OK, wx.ID_YES):
        path = dialogObj.GetPath()
        if os.path.exists(path):
            name = os.path.basename(path)
            if len(name) > 16: name = name[: 16] + '...'
            dlg = wx.MessageDialog(dialogObj, '''File "%s"\nhas already existed, ok to overwrite?''' % name, \
                                   "Message", wx.ICON_INFORMATION|wx.YES_NO|wx.CANCEL)
            overwrite = dlg.ShowModal()
            dlg.Destroy()
        else:
            overwrite = wx.ID_YES
        if overwrite != wx.ID_NO: break
    if overwrite == wx.ID_YES:
        return True
    else:
        return False


class fileBatchExport(Thread):

    def __init__(self, parent, outdir):
        super(fileBatchExport, self).__init__(name='fileExportThread')
        self.file_list = parent.file_list
        self.output_dir = outdir
        self.process = parent.imgP.process
        self.loading = LoadingFrame(parent, len(self.file_list))
        self.start()
        self.loading.ShowModal()

    def run(self):
        img_list = []
        for file in self.file_list:
            buf = np.fromfile(file, dtype=np.uint8)
            img = self.process(cv.imdecode(buf, cv.IMREAD_COLOR))
            if self.loading._running:
                img_name = '.'.join(os.path.basename(file).split('.')[: -1]) + OUTPUT_SUFFIX
                cv.imencode('.jpg', img)[1].tofile(os.path.join(self.output_dir, img_name))
                img_list.append(img_name)
                self.loading.update()
            else:
                break
            sleep(0.1)
        print('Write Image:', work_path, img_list)
        self.loading.quit(None)
        showFile(work_path, img_list)


class LoadingFrame(_LoadingDialog):

    def __init__(self, parent, n):
        super(LoadingFrame, self).__init__(parent)
        self.n = n; self.i = 1
        self._running = True
        self.update()

    def update(self):
        if self._running and self.i <= self.n:
            self.m_gauge1.SetValue(int(100 * self.i / self.n))
            self.m_staticText44.SetLabel('%d / %d' % (self.i, self.n));
            self.i += 1

    def quit(self, evt):
        self._running = False
        if evt:
            evt.Skip()
        else:
            self.Close()


class AboutFrame(_AboutDialog):

    def __init__(self, parent):
        super(AboutFrame, self).__init__(parent)
        self.m_bitmap2.SetBitmap(wx.Bitmap(os.path.join(base_path, 'appIcon.ico')))
        self.m_staticText47.SetLabel(f"{APP_NAME} - {APP_NAME_CN} {APP_VERSION}")
        self.m_staticText48.SetLabel(f"一个功能丰富的图片线稿提取器\n\n\
Designed by Yangwang, last updated on {LAST_MODIFICATION}\n\
Powered by Python 3.8 | OpenCV 4.5.4")

    def confirm(self, evt):
        self.Close()


def showFile(location, items=[]):
    cmd = f'{base_path}\\select.exe "{location}"'
    for item in items:
        cmd += ' "%s"' % item
    p = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout= subprocess.PIPE, \
                         stderr=subprocess.STDOUT, text=True)
    out, err = p.communicate()
    if p.returncode: print(out)


class mainApp(wx.App):

    def OnInit(self):
        self.SetAppName(APP_NAME)
        self.Frame = mainFrame()
        SetHelpProvider(self.Frame)
        self.SetTopWindow(self.Frame)
        self.Frame.Show()
        return True

    def OnExit(self):
        self.Frame.imgP.exit()
        return True


if __name__ == '__main__':
    freeze_support()
    with logging(log_path):
        app = mainApp(redirect=False, filename=None)
        app.MainLoop()


