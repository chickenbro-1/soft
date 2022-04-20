from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from decimal import *
import math
import json

class Rake_wave(QMainWindow):
    def __init__(self,sampling_rate,Dominant_frequency,sampling_time):
        super(Rake_wave, self).__init__()
        self.sampling_rate= sampling_rate
        self.Dominant_frequency =Dominant_frequency
        self.sampling_time=sampling_time
        self.Rickwave(sampling_rate, Dominant_frequency, sampling_time)

        fjson = 'project.json'
        with open(fjson, 'r') as f:
            content = json.load(f)
        axis = {"sampling_rate":sampling_rate,"Dominant_frequency":Dominant_frequency,"sampling_time":sampling_time}
        content.update(axis)
        with open(fjson, 'w') as f_new:
            json.dump(content, f_new)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.resize(800, 659)
    def Rickwave(self,sampling_rate,Dominant_frequency,sampling_time):
        '''
            传入参数    dt ->采样率 f
                        t ->采样时间 i
                        fmax ->主频f
        '''
        dt = float(sampling_rate)
        fmax=float(Dominant_frequency)
        t =float(sampling_time)
        def floatrange(start, stop, steps):
            '''
            生成采样序列
            start:计数从 start 开始
            stop:计数到 stop 结束
            step:步长
            '''
            resultList = []
            while Decimal(str(start)) <= Decimal(str(stop)):
                resultList.append(float(Decimal(str(start))))
                start = Decimal(str(start)) + Decimal(str(steps))
            return resultList
        t_list = floatrange(-t, t, dt)
        Rickwave_list = []
        for t_list_i in t_list:
            value1 = (Decimal(str(Decimal(str(math.pi)) * Decimal(str(math.pi))))) * (
                Decimal(str(Decimal(str(fmax)) * Decimal(str(fmax))))) * (
                         Decimal(str(Decimal(str(t_list_i)) * Decimal(str(t_list_i)))))
            Rickwave_value = (Decimal(str(1)) - Decimal(str(2)) * value1) * Decimal(str(math.exp(-value1)))
            Rickwave_list.append(Rickwave_value)
        print(len(Rickwave_list), 'Rickwave_list')
        # 清屏
        plt.cla()
        # 获取绘图并绘制
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        x = t_list
        y = Rickwave_list
        ax.plot(x,y)
        cavans = FigureCanvas(fig)
        self.setCentralWidget(cavans)