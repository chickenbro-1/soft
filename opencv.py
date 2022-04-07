from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets,QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import cv2
import numpy as np
class opencv(QMainWindow):
    def __init__(self):
        super(opencv, self).__init__()
        #self.setupUi(self)
        #self.retranslateUi(self)
        self.img = cv2.imread("temp.png", 0)
        x = cv2.Scharr(self.img, cv2.CV_16S, 1, 0)  # X 方向
        y = cv2.Scharr(self.img, cv2.CV_16S, 0, 1)  # Y 方向
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        dst_scharr = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

        self.setWindowTitle('QPixmap例子')

        layout = QVBoxLayout()

        lab1 = QLabel()
        lab1.setPixmap(QPixmap(dst_scharr))

        layout.addWidget(lab1)

        self.setLayout(layout)
'''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 452)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 70, 581, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 0, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 70, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 315, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(410, 30, 31, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(440, 40, 54, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(210, 400, 141, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.save_result)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "log算子边缘检测结果"))
        self.label_2.setText(_translate("Form", " "))
        self.label_3.setText(_translate("Form", "由图像中点处（第400）列检测图像中有"))
        self.label_4.setText(_translate("Form", "个地层"))
        self.pushButton.setText(_translate("Form", "保存结果"))
    
    def Sobel(self):
        x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
        y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        dst_sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        return dst_sobel
    def Canny(self):
        dst_cany = cv2.Canny(img, 50, 50)
        return dst_cany
    def Scharr(self):
        x = cv2.Scharr(img, cv2.CV_16S, 1, 0)  # X 方向
        y = cv2.Scharr(img, cv2.CV_16S, 0, 1)  # Y 方向
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        dst_scharr = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        return dst_scharr
    def Log(self):
        dst = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
        dst_log = cv2.convertScaleAbs(dst)
        return dst_log
'''
