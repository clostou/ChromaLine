import wx


def SetHelpProvider(frame):
    self = frame
    wx.ToolTip.Enable(False)
    
    self.m_panel1.SetToolTip(u'''\
模块：noiseSmooth - 图像平滑/去噪 
    去除或抑制图像中的噪声，减小其对边缘检测的影响。
支持算法：
    双边滤波 (Bilateral Filtering)
    中值平滑 (Median Blurring)''')
    self.m_radioBtn1.SetToolTip(u"无去噪")
    self.m_radioBtn2.SetToolTip(u"双边滤波")
    self.m_radioBtn3.SetToolTip(u"中值平滑")
    self.m_slider1.SetToolTip(u'''\
双边滤波参数 - sigmaSpace：
    坐标空间滤波器标准偏差值，用于构建距离权重模板，
决定多远范围内的像素会被计算。''')
    self.m_slider2.SetToolTip(u'''\
双边滤波参数 - sigmaColor：
    颜色空间滤波器标准偏差值，用于构建灰度值相似度
模板，决定多少差值内的像素会被计算。''')
    self.m_slider3.SetToolTip(u'''\
中值平滑参数 - ksize：
    参与统计计算的像素块的尺寸。''')

    self.m_panel2.SetToolTip(u'''\
模块：edgeExtract - 边缘提取
    图像的边缘一般是背景与前景物体的交界处，因此利用
差分卷积识别出灰度值急剧变化区域，来提取边缘。
支持算法：
    自适应阈值化 (Adaptive Thresholding)
    Canny边缘检测
    Scharrr边缘检测
    Laplace of Gaussian (LoG)边缘检测
后处理：
    图像细化 (Thinning)
    形态学梯度 (Morphological Gradient)''')
    self.m_radioBtn4.SetToolTip(u"自适应阈值化")
    self.m_radioBtn5.SetToolTip(u"Canny边缘检测")
    self.m_radioBtn6.SetToolTip(u"Scharrr边缘检测")
    self.m_radioBtn7.SetToolTip(u"LoG边缘检测")
    self.m_choice3.SetToolTip(u'''\
自适应阈值化参数 - adaptiveMethod：
    自适应方法。
    gaussian：阈值为周围像素的高斯均值（按权重）。
    mean：阈值为周围像素的平均值。''')
    self.m_slider4.SetToolTip(u'''\
自适应阈值化参数 - C：
    阈值偏置值。通过自适应方法计算的值，减去该常数值
即为最终阈值。''')
    self.m_slider5.SetToolTip(u'''\
自适应阈值化参数 - blocksize：
    计算自适应阈值时的窗口大小。''')
    self.m_slider7.SetToolTip(u'''\
Canny边缘检测参数 - threshold1：
    双阈值中的低阈值。梯度小于该值像素点被认为一定
不属于边缘。''')
    self.m_slider6.SetToolTip(u'''\
Canny边缘检测参数 - threshold2：
    双阈值中的高阈值。梯度大于该值的像素点被归为
“确定边缘”像素，而小于该值且大于低阈值的像素，
其保留与否取决于是否与确定边缘相连。''')
    self.m_slider8.SetToolTip(u'''\
Canny边缘检测参数 - apertureSize：
    计算梯度时使用的Sobel卷积核的大小。''')
    self.m_slider9.SetToolTip(u'''\
Scharr边缘检测线性变换参数 - a：
    对检测结果进行线性变换时的下限，小于该值的像素点
将被置为0。''')
    self.m_slider10.SetToolTip(u'''\
Scharr边缘检测线性变换参数 - b：
    对检测结果进行线性变换时的上限，大于该值的像素点
将被置为255。''')
    self.m_slider12.SetToolTip(u'''\
LoG边缘检测线性变换参数 - a：
    对检测结果进行线性变换时的下限，小于该值的像素点
将被置为0。''')
    self.m_slider11.SetToolTip(u'''\
LoG边缘检测线性变换参数 - b：
    对检测结果进行线性变换时的上限，大于该值的像素点
将被置为255。''')
    self.m_checkBox1.SetToolTip(u'''\
边缘检测后处理 - 图像细化：
    细化图像几何结构，得到简化的拓扑等价图像。''')
    self.m_checkBox2.SetToolTip(u'''\
边缘检测后处理 - 形态学梯度：
    将图像的膨胀运算结果减去腐蚀运算结果，可以得到
部分轮廓信息。''')

    self.m_panel3.SetToolTip(u'''\
模块：colorRender - 色彩渲染
    在HSV颜色空间中通过不同算法调节各分量，实现不同
的颜色过渡效果。
Hue - 色相调节：
    纯色 (Static)
    线性过渡 (Linear)
    随机迷宫 (Maze)
Saturation - 饱和度调节：
    原图映射 (Map Mode)''')
    self.m_radioBtn8.SetToolTip(u"纯色")
    self.m_radioBtn9.SetToolTip(u"线性过渡")
    self.m_radioBtn10.SetToolTip(u"随机迷宫")
    self.m_choice1.SetToolTip(u'''\
线性过渡参数 - direction：
    线性过渡的轴线方向。
    LU：左上至右下对角线方向
    RU：右上至左下对角线方向
    U：从上至下垂直方向
    L：从左至右水平方向''')
    self.m_slider14.SetToolTip(u'''\
线性过渡参数 - period：
    线性过渡的色相循环周期。其值越大色彩变化越慢，
反之越快。''')
    self.m_slider13.SetToolTip(u'''\
随机迷宫参数 - diagonalLength：
    生成迷宫的对角线长度，其值越大，迷宫尺寸越大，
相应地色彩随机性越不明显。''')
    self.m_checkBox3.SetToolTip(u'''\
随机迷宫参数 - blur：
    是否对迷宫色块边界进行渐变处理。''')
    self.m_textCtrl2.SetToolTip(u'''\
随机迷宫参数 - center：
    生成迷宫的起点，效果上为色彩变化的起点。''')
    self.m_slider15.SetToolTip(u'''\
色相调节参数 - hueOffset：
    色相偏置值。该值将与上述色相调节算法计算出的
值相加，得到最终的色相值。''')
    self.m_slider16.SetToolTip(u'''\
饱和度调节参数 - saturation：
    饱和度值。当未启用原图映射时，所有像素的饱和度
均相等，且等于该值。''')
    self.m_checkBox4.SetToolTip(u'''\
饱和度调节参数 - mapMode：
    启用原图映射。此方法将依据原图的色彩信息调节
当前图片的饱和度。''')
    self.m_choice2.SetToolTip(u'''\
原图映射参数 - phase：
    选择从原图的哪个HSV分量提取信息。''')
    self.m_slider17.SetToolTip(u'''\
原图映射参数 - lower：
    偏置因数。用于对原图色彩信息进行简单的线性调整。''')

    self.m_textCtrl1.SetToolTip(u"输入图片路径")
    self.m_button4.SetToolTip(u"浏览文件")
    self.m_button7.SetToolTip(u"全部导出")
    self.m_button8.SetToolTip(u"导出图片")
    self.m_button3.SetToolTip(u"重置参数")
    self.m_button5.SetToolTip(u"切换显示原图")
    self.m_button31.SetToolTip(u"上一张")
    self.m_button41.SetToolTip(u"下一张")


