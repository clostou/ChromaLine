import cv2 as cv
import numpy as np
import random
from time import time, sleep
from copy import copy

from multiprocessing import Process, Pipe
from threading import Thread
from traceback import format_exc


class noiseSmooth():

    def __init__(self, img):
        self.img = img    # Any
        self._medFilt_args = None
        self._biFilt_args = None
        self.img_smooth = {}
    
    def medFilt(self, size=3, **kwargs):
        if (size, ) == self._medFilt_args: return
        self._medFilt_args = (size, )
        self.img_smooth['medFilt'] =  cv.medianBlur(self.img, size)
        
    def biFilt(self, s_space=8, s_value=20, **kwargs):
        if (s_space, s_value) == self._biFilt_args: return
        self._biFilt_args = (s_space, s_value)
        self.img_smooth['biFilt'] =  cv.bilateralFilter(self.img, s_space, s_value, s_value)

    def get(self, method='bilateral', **kwargs):
        if method == 'bilateral':
            self.biFilt(**kwargs)
            return self.img_smooth['biFilt']
        elif method == 'median':
            self.medFilt(**kwargs)
            return self.img_smooth['medFilt']
        elif method == 'origin':
            return self.img
        else:
            raise ValueError("Unkown smoothing method '%s'" % method)


class  edgeExtract():

    def __init__(self, img):
        self.img = img    # Gray
        self._adaTresh_args = None
        self._Canny_args = None
        self._Canny_maplist = {3: 10, 5: 100, 7: 1000}
        self._updateScharr()
        self._updateLoG()
        self.img_edge = {}

    # 二值化边缘提取
    def adaThresh(self, C=10, size=9, ada='g', **kwargs):    # adaptiveThreshold: 卷积核size不能为1
        args = (C, size, ada)
        if args == self._adaTresh_args: return
        else: self._adaTresh_args = args
        if ada == 'g':
            ada_method = cv.ADAPTIVE_THRESH_GAUSSIAN_C
        elif ada == 'm':
            ada_method = cv.ADAPTIVE_THRESH_MEAN_C
        else:
            return
        self.img_edge['adaThresh'] = cv.adaptiveThreshold(self.img, 255, ada_method, \
                                                          cv.THRESH_BINARY_INV, size, C)

    def Canny(self, lower=20, upper=40, size=7, **kwargs):    # Canny: 卷积核size只能为3-7之间的奇数
        args = (lower, upper, size)
        if args == self._Canny_args: return
        else: self._Canny_args = args
        lower *= self._Canny_maplist[size]
        upper *= self._Canny_maplist[size]
        self.img_edge['Canny'] = cv.Canny(self.img, lower, upper, apertureSize=size, L2gradient=True)

    # 非二值化边缘提取
    def _reScale(self, src, a, b):
        alpha = 255 / (b - a)
        beta = - alpha * a
        dst = alpha * src + beta
        dst[np.where(dst > 255)] = 255.
        dst[np.where(dst < 0)] = 0.
        return dst.astype(np.uint8, copy=False)

    def _updateScharr(self):
        self._Scharr_args = None
        scharr = np.sqrt(cv.Scharr(self.img, cv.CV_32F, 1, 0)**2 + cv.Scharr(self.img, cv.CV_32F, 0, 1)**2)
        k = np.max(scharr) / 100
        self._rawScharr = (scharr, k)

    def Scharr(self, a=0, b=100, **kwargs):
        args = (a, b)
        if args == self._Scharr_args or b <= a: return
        else: self._Scharr_args = args
        _a = self._rawScharr[1] * a
        _b = self._rawScharr[1] * b
        self.img_edge['Scharr'] = self._reScale(self._rawScharr[0], _a, _b)

    def _getLoGKernel(self, size, sigma):
        _size = size // 2
        scale = np.linspace(-_size, _size, 2 * _size + 1, dtype=np.int8)
        X, Y = np.meshgrid(scale, scale)
        alpha = 0.5 * (X**2 + Y**2) / sigma**2
        kernel = (alpha - 1) * np.exp(-alpha) / (np.pi * sigma**4)
        return kernel

    def _updateLoG(self, size=7, sigma=1):
        self._LoG_args = None
        LoGKernel = self._getLoGKernel(size, sigma)
        log =  np.abs(cv.filter2D(self.img, cv.CV_32F, LoGKernel, borderType=cv.BORDER_REFLECT))
        k = np.max(log) / 100
        self._rawLoG = (log, k)

    def LoG(self, a=-100, b=100, **kwargs):
        args = (a, b)
        if args == self._LoG_args or b <= a: return
        else: self._LoG_args = args
        _a = self._rawLoG[1] * a
        _b = self._rawLoG[1] * b
        self.img_edge['LoG'] = self._reScale(self._rawLoG[0], _a, _b)

    # 形态学处理
    def morphGrad(self, img, N=1, **kwargs):
        kernel = self.__dict__.setdefault('morphKernel', \
                                          cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3)))
        return cv.morphologyEx(img, \
                               cv.MORPH_GRADIENT, kernel, iterations=N)
    
    def thinning(self, img, thresh=128, **kwargs):
        index = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        value = [1] * 8
        def _getAdjacency(img, x, y):
            nonlocal value; i = 0
            while i < 8:
                try:
                    value[i] = img[x+index[i][0], y+index[i][1]]
                except:
                    value[i] = 1
                i += 1
            return value
        def _checkChange(adList):
            _adList = copy(adList)
            _adList.append(_adList.pop(0))
            i = 0; count = 0
            while i < 8:
                if _adList[i] == 1 and adList[i] == 0: count += 1
                i += 1
            return count == 1
        m, n = img.shape
        img_bin = cv.threshold(img, thresh, 1, cv.THRESH_BINARY)[1]
        while True:
            # 1
            mask = np.ones(img.shape, dtype=img.dtype)
            for x in range(m):
                for y in range(n):
                    if not img_bin[x, y]: continue
                    value = _getAdjacency(img_bin, x, y)
                    if not _checkChange(value): continue
                    if not (2 <= sum(value) <= 6): continue
                    if value[0] & value[2] & value[4] != 0 or value[2] & value[4] & value[6] != 0: continue
                    mask[x, y] = 0
            img_bin = cv.bitwise_and(img_bin, mask)
            # 2
            mask = np.ones(img.shape, dtype=img.dtype)
            for x in range(m):
                for y in range(n):
                    if not img_bin[x, y]: continue
                    value = _getAdjacency(img_bin, x, y)
                    if not _checkChange(value): continue
                    if not (2 <= sum(value) <= 6): continue
                    if value[0] & value[2] & value[6] != 0 or value[0] & value[4] & value[6] != 0: continue
                    mask[x, y] = 0
            img_bin = cv.bitwise_and(img_bin, mask)
            if np.all(mask): break
        return img_bin * 255

    # 其他处理
    def inv(self, img):
        return cv.bitwise_not(img)

    # 公共接口
    def get(self, method='adaThresh', **kwargs):
        if method == 'adaThresh':
            self.adaThresh(**kwargs)
            edge = self.img_edge['adaThresh']
        elif method == 'Canny':
            self.Canny(**kwargs)
            edge = self.img_edge['Canny']
        elif method == 'Scharr':
            self.Scharr(**kwargs)
            edge = self.img_edge['Scharr']
        elif method == 'LoG':
            self.LoG(**kwargs)
            edge = self.img_edge['LoG']
        else:
            raise ValueError("Unkown edge extraction method '%s'" % method)
        if kwargs.get('thinning'):
            edge = self.thinning(edge, **kwargs)
        if kwargs.get('morphGrad'):
            edge = self.morphGrad(edge, **kwargs)
        if kwargs.get('inverse'):
            edge = self.inv(edge)
        return edge


class colorRender():

    def __init__(self, img, edge):
        self.img = img    # BGR
        self.edge = edge    # Gray
        self._maze_args = (0, 0, 0)

    def originMap(self, phase='v', lower=0.0, **kwargs):
        img_hsv = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
        if phase == 'h':
            img_map = ((img_hsv[: , : , 0] / 180 + lower) * 255).astype(np.uint8)
        elif phase == 's':
            img_map = ((1. - lower) * img_hsv[: , : , 1] + lower * 255).astype(np.uint8)
        elif phase == 'v':
            img_map = ((1. - lower) * img_hsv[: , : , 2] + lower * 255).astype(np.uint8)
        else:
            img_map = np.zeros(img_hsv.shape, dtype=np.uint8)
        return cv.boxFilter(img_map, -1, (3, 3))
    
    def linearMap(self, direction=1, period=1, **kwargs):
        m, n, _ = self.img.shape
        diag_len = np.sqrt(m**2 + n**2)
        img_map = np.zeros((m, n), dtype=np.uint8)
        hue_range = 256 / period
        x = y = 0;
        if direction == 1:
            k = hue_range / diag_len**2
            while x < m:
                y = 0
                while y < n:
                    img_map[x, y] = k * (x * m + y * n)
                    y += 1
                x += 1
        elif direction == 2:
            k = hue_range / diag_len**2
            while x < m:
                y = 0
                while y < n:
                    img_map[x, (n - 1) - y] = k * (x * m + y * n)
                    y += 1
                x += 1
        elif direction == 3:
            k = hue_range / m
            while x < m:
                img_map[x, : ] = k * x
                x += 1
        elif direction == 4:
            k = hue_range / n
            while y < n:
                img_map[: , y] = k * y
                y += 1
        return img_map

    def mazeMap(self, diag_len=30, center=(0, 0), blur=True, **kwargs):
        m, n, _ = self.img.shape
        scale = np.sqrt(m**2 + n**2) / diag_len
        x0, y0 = center
        x0 = int(m * x0 / scale)
        y0 = int(n * y0 / scale)
        if (diag_len, x0, y0) != self._maze_args:
            self._maze_args = (diag_len, x0, y0)
            _m = int(m / scale) + 1
            _n = int(n / scale) + 1
            # Randomized Prim's algorithm
            random.seed(time())
            maze = np.zeros((_m, _n, 5), dtype=np.bool)
            maze[x0, y0, 0] = 1
            cells = [(x0, y0)]
            while cells:
                directions = []
                i = random.randint(0, len(cells) - 1)
                x, y = cells[i]
                if not maze[x, y, 1] and x > 0 and not maze[x - 1, y, 0]:
                    directions.append('U')
                if not maze[x, y, 2] and y > 0 and not maze[x, y - 1, 0]:
                    directions.append('L')
                if not maze[x, y, 3] and x < _m - 1 and not maze[x + 1, y, 0]:
                    directions.append('D')
                if not maze[x, y, 4] and y < _n - 1 and not maze[x, y + 1, 0]:
                    directions.append('R')
                if directions:
                    direction = random.choice(directions)
                    if direction == 'U':
                        maze[x, y, 1] = 1
                        x -= 1
                        maze[x, y, 3] = 1
                    if direction == 'L':
                        maze[x, y, 2] = 1
                        y -= 1
                        maze[x, y, 4] = 1
                    if direction == 'D':
                        maze[x, y, 3] = 1
                        x += 1
                        maze[x, y, 1] = 1
                    if direction == 'R':
                        maze[x, y, 4] = 1
                        y += 1
                        maze[x, y, 2] = 1
                    cells.append((x, y))
                    maze[x, y, 0] = 1
                else:
                    cells.pop(i)
            wall = maze[: , : , 1: ]
            # Recursive backtrack pathing
            path = np.zeros((_m, _n))
            path[(x0, y0)] = 1
            stack = [(x0, y0)]
            x = x0; y = y0
            while stack:
                if wall[x, y, 0] and path[x - 1, y] == 0:
                    pos = (x - 1, y)
                elif wall[x, y, 1] and path[x, y - 1] == 0:
                    pos = (x, y - 1)
                elif wall[x, y, 2] and path[x + 1, y] == 0:
                    pos = (x + 1, y)
                elif wall[x, y, 3] and path[x, y + 1] == 0:
                    pos = (x, y + 1)
                else:
                    pos = ()
                if pos:
                    stack.append((x, y))
                    x, y = pos
                    path[pos] = len(stack)
                else:
                    x, y = stack.pop()
            self._rawMaze = img_map = cv.resize(\
                (path / np.max(path) * 255).astype(np.uint8), \
                (n, m), interpolation=cv.INTER_NEAREST)
        if blur:
            size = 2 * (int(np.ceil(0.8 * scale)) // 2) + 1
            img_map = cv.GaussianBlur(self._rawMaze, (size, size), scale)
        else:
            img_map = self._rawMaze
        return img_map

    def renderHSV(self, h_method='linear', hue_offset=0, **kwargs):
        m, n, _ = self.img.shape
        img = np.zeros((m, n, 3), dtype=np.uint8)
        if h_method == 'static':
            img[: , : , 0] = (38 + hue_offset) % 180
        elif h_method == 'linear':
            img[: , : , 0] = (180 / 255 * self.linearMap(**kwargs) + hue_offset) % 180
        elif h_method == 'maze':
            img[: , : , 0] = (180 / 255 * self.mazeMap(**kwargs) + hue_offset) % 180
        if kwargs.get('saturation') != None:
            img[: , : , 1] = kwargs['saturation']
        else:
            img[: , : , 1] = self.originMap(**kwargs)
        img[: , : , 2] = self.edge
        return cv.cvtColor(img, cv.COLOR_HSV2BGR)

    def get(self, method='hsv', **kwargs):
        if method == 'hsv':
            return self.renderHSV(**kwargs)
        else:
            raise ValueError("Unkown color render '%s'" % method)


class imgProcess():

    def __init__(self, img=None):
        self.img = [None] * 4
        self.changed = 3
        self.config_smooth = {}
        self.config_edge = {}
        self.config_color = {}
        if img:
            self.img[0] = img    # BGR
            self.changed = 0

    def read(self, img):
        if isinstance(img, str):
            self.img[0] = cv.imread(img, cv.IMREAD_COLOR)
            self.changed = 0
        elif isinstance(img, np.ndarray) and len(img.shape) == 3:
            self.img[0] = img
            self.changed = 0
        else:
            return
        self.module_smooth = noiseSmooth(self.img[0])

    def update(self, end=3):
        if end <= self.changed: return
        module_ind = list(range(self.changed, end))
        if 0 in module_ind:
            self.img[1] = self.module_smooth.get(**self.config_smooth)
            self.module_edge = edgeExtract(cv.cvtColor(self.img[1], cv.COLOR_BGR2GRAY))
        if 1 in module_ind:
            self.img[2] = self.module_edge.get(**self.config_edge)
            self.module_color = colorRender(self.img[1], self.img[2])
        if 2 in module_ind:
            self.img[3] = self.module_color.get(**self.config_color)
        self.changed = end

    def set(self, index, kwargs):
        if index == 1:
            self.config_smooth.update(kwargs)
            self.img[1] = self.module_smooth.get(**self.config_smooth)
            self.module_edge = edgeExtract(cv.cvtColor(self.img[1], cv.COLOR_BGR2GRAY))
        elif index == 2:
            self.config_edge.update(kwargs)
            self.img[2] = self.module_edge.get(**self.config_edge)
            self.module_color = colorRender(self.img[1], self.img[2])
        elif index == 3:
            self.config_color.update(kwargs)
            self.img[3] = self.module_color.renderHSV(**self.config_color)
        else:
            return
        self.changed = index
        return self.img[index]


class commThread(Thread):

    def __init__(self, pipe):
        super(commThread, self).__init__(name='commThread')
        self.pipe = pipe
        self.queue = []
        self._temp = None
        self._flag = -1
        self.start()

    def poll(self):
        return len(self.queue)
    
    def recv(self):
        return self.queue.pop(0)

    def send(self, data):
        self.pipe.send(data)

    def _send_temp(self):
        if self._flag >= 0:
            self.queue.append(self._temp)
            self._flag = -1

    def run(self):
        while True:
            if not self.poll():
                self._send_temp()
            if self.pipe.poll():
                msg = self.pipe.recv()
            else:
                continue
            if msg[0] == 'set':
                if msg[1] != self._flag:
                    self._send_temp()
                    self._flag = msg[1]
                self._temp = msg
            else:
                self._send_temp()
                self.queue.append(msg)
            if msg[0] == 'exit':
                break


def _imgP(pipe):
    process = imgProcess()
    pipe = commThread(pipe)
    while True:
        if pipe.poll():
            msg = pipe.recv()
        else:
            sleep(0.01)
            continue
        try:
            if msg[0] == 'set':
                if msg[1] == 0:
                    process.read(msg[2])
                else:
                    #pipe.send(('info', 'INFO', msg))
                    img = process.set(msg[1], msg[2])
                    pipe.send(('img', msg[1], img))
            elif msg[0] == 'get':
                process.update(msg[1])
                pipe.send(('img', msg[1], process.img[msg[1]]))
            elif msg[0] == 'exit':
                del process
                break
        except Exception as e:
            pipe.send(('info', repr(e), format_exc()))


def ProcessingInit(img=None, config=[]):
    con1, con2 = Pipe()
    p = Process(target=_imgP, args=(con2, ), name='imgProcess')
    p.start()
    if img:
        con1.send(('set', 0, img))
        for i, args_dict in enumerate(config):
            con1.send(('set', i + 1, args_dict))
    return p, con1


def show(img):
    cv.imshow('Image', img)


if __name__ == '__main__':
    path = r'.\test.jpeg'
    img_gray = cv.imread(path, cv.IMREAD_GRAYSCALE)
    p = edgeExtract(img_gray)
    p.adaThresh(12)
    p.Canny(20, 40)
    p.Scharr(b=80)
    p.LoG(0, 60)
    '''
    img = np.zeros((700, 700, 3), dtype=np.uint8)
    edge = np.zeros((700, 700), dtype=np.uint8)
    c = colorRender(img, edge)
    cv.imshow('Maze', c.mazeMap(30, (0, 0), True))
    '''
    c = colorRender(cv.imread(path, cv.IMREAD_COLOR), p.img_edge['Scharr'])
    img = c.renderHSV()
    cv.imshow('Image', img)
    #cv.imshow('Image', c.renderHSV('linear', {'direction': 2, 'period': 0.8, 'phase': 's', 'lower': 0.4}, 30))
    #cv.imshow('Image', c.renderHSV('maze', {'diag_len': 30, 'center':(0.5, 0.5), 'blur': False, 'phase': 's', 'lower': 0.4}, 0))


