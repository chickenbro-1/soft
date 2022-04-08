import sys
import cv2 as cv
import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QGridLayout,QMessageBox,QLabel, QPushButton)

class opencv(QDialog):
    def __init__(self,type):
        # 初始化一个img的ndarray, 用于存储图像
        self.img = np.ndarray(())
        super().__init__()
        self.type = type
        self.initUI(type)
    def initUI(self,type):
        # 设置窗口图标
        # self.setWindowIcon(QIcon("filename"))
        # 设置窗口名
        self.setWindowTitle("{}边缘检测结果".format(type))
        self.resize(400, 300)
        self.btnOpen = QPushButton('Open', self)
        self.btnSave = QPushButton('Save', self)
        self.btnProcess = QPushButton('Process', self)
        self.btnQuit = QPushButton('Quit', self)
        self.label = QLabel()
        # 布局设定
        layout = QGridLayout(self)
        layout.addWidget(self.label, 0, 1, 3, 4)
        layout.addWidget(self.btnOpen, 4, 1, 1, 1)
        layout.addWidget(self.btnSave, 4, 2, 1, 1)
        layout.addWidget(self.btnProcess, 4, 3, 1, 1)
        layout.addWidget(self.btnQuit, 4, 4, 1, 1)
        # 信号与槽连接, PyQt5与Qt5相同, 信号可绑定普通成员函数
        self.btnOpen.clicked.connect(self.openSlot)
        self.btnSave.clicked.connect(self.saveSlot)
        self.btnProcess.clicked.connect(self.processSlot)
        self.btnQuit.clicked.connect(self.close)
    def openSlot(self):
        # 调用打开文件diglog
        fileName, tmp = QFileDialog.getOpenFileName(
            self, 'Open Image', './__data', '*.png *.jpg *.bmp')
        if fileName is '':
            return
        # 采用opencv函数读取数据
        self.img = cv.imread(fileName, -1)
        if self.img.size == 1:
            return
        self.refreshShow()
    def saveSlot(self):
        # 调用存储文件dialog
        fileName, tmp = QFileDialog.getSaveFileName(
            self, 'Save Image', './__data', '*.png *.jpg *.bmp', '*.png')
        if fileName is '':
            return
        if self.img.size == 1:
            return
        # 调用opencv写入图像
        cv.imwrite(fileName, self.img)
    def processSlot(self):
        if self.img.size == 1:
            return
        maping = {
            'Scharr算子':self.Scharr(),
            'sobel算子':self.Sobel(),
            'log算子':self.Log(),
        }
        self.img = maping.get(self.type)
        self.refreshShow()
    def refreshShow(self):
        # 提取图像的尺寸和通道, 用于将opencv下的image转换成Qimage
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QPixmap.fromImage(self.qImg))
    def Sobel(self):
        x = cv2.Sobel(self.img, cv2.CV_16S, 1, 0)
        y = cv2.Sobel(self.img, cv2.CV_16S, 0, 1)
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        dst_sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        #num ,ret = cv2.connectedComponents(dst_sobel)
        return dst_sobel
    def Scharr(self):
        x = cv2.Scharr(self.img, cv2.CV_16S, 1, 0)  # X 方向
        y = cv2.Scharr(self.img, cv2.CV_16S, 0, 1)  # Y 方向
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        dst_scharr = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        return dst_scharr
    def Log(self):
        dst = cv2.Laplacian(self.img, cv2.CV_16S, ksize=3)
        dst_log = cv2.convertScaleAbs(dst)
        return dst_log
    def warningBtn_clicked(self,num):
        QMessageBox.warning(self, '结果', '识别到有{}层地层'.format(num),QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = opencv()
    w.show()
    sys.exit(a.exec_())