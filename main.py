import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import Qt
from painting import MainWidget
from new_project import new_project
from opencv import opencv
from Rake_wave import Rake_wave
from reflection_coe import reflection_coe
from synthetic_seismogram import synthetic_seismogram
from spectrum_diagram import spectrum_diagram
import qdarkstyle
import os
import pathlib
import re
import json

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1031, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.Tab = QtWidgets.QWidget()
        self.Tab.setObjectName("Tab")
        self.splitter = QtWidgets.QSplitter(self.Tab)
        self.splitter.setGeometry(QtCore.QRect(0, 390, 331, 61))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_6.setObjectName("pushButton_6")
        self.comboBox = QtWidgets.QComboBox(self.Tab)
        self.comboBox.setGeometry(QtCore.QRect(180, 10, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.splitter_5 = QtWidgets.QSplitter(self.Tab)
        self.splitter_5.setGeometry(QtCore.QRect(10, 50, 141, 131))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.pushButton = QtWidgets.QPushButton(self.splitter_5)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.splitter_3 = QtWidgets.QSplitter(self.Tab)
        self.splitter_3.setGeometry(QtCore.QRect(180, 50, 151, 131))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.Tab)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.widget_2 = MainWidget(self.Tab)
        self.widget_2.setGeometry(QtCore.QRect(375, 9, 591, 441))
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QtWidgets.QWidget(self.Tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 210, 231, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.layoutWidget1 = QtWidgets.QWidget(self.Tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 250, 231, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.layoutWidget2 = QtWidgets.QWidget(self.Tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 290, 261, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.clicked.connect(self.full_value)

        self.horizontalLayout_3.addWidget(self.radioButton)
        self.layoutWidget3 = QtWidgets.QWidget(self.Tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 330, 281, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.clicked.connect(self.full_value_2)
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.tabWidget.addTab(self.Tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #新建正演文件
        self.actionda = QtWidgets.QAction(MainWindow)
        self.actionda.setObjectName("actionda")
        self.actionda.triggered.connect(self.new_project)
        #
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")

        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(self.opencv)

        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.triggered.connect(self.reflection_coe)

        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_4.triggered.connect(self.Rake_wave)

        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_5.triggered.connect(self.spectrum_diagram)

        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_6.triggered.connect(self.synthetic_seismogram)

        self.actioncanny = QtWidgets.QAction(MainWindow)
        self.actioncanny.setObjectName("actioncanny")
        self.actionScharr = QtWidgets.QAction(MainWindow)
        self.actionScharr.setObjectName("actionScharr")
        self.actionsobel = QtWidgets.QAction(MainWindow)
        self.actionsobel.setObjectName("actionsobel")
        self.actionlog = QtWidgets.QAction(MainWindow)
        self.actionlog.setObjectName("actionlog")
        self.menu.addSeparator()
        self.menu.addAction(self.actionda)
        self.menu_3.addAction(self.action_2)
        self.menu_3.addAction(self.action_3)
        self.menu_3.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_5.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.label.setBuddy(self.lineEdit)
        self.label_3.setBuddy(self.lineEdit_3)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_4.setBuddy(self.lineEdit_4)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.new_project)
        self.pushButton_3.clicked.connect(self.Rake_wave)
        self.pushButton_4.clicked.connect(self.reflection_coe)
        self.pushButton_5.clicked.connect(self.synthetic_seismogram)
        self.pushButton_6.clicked.connect(self.spectrum_diagram)
        self.pushButton_7.clicked.connect(self.opencv)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "合成地震记录"))
        self.pushButton_6.setText(_translate("MainWindow", "频谱图"))
        self.comboBox.setItemText(0, _translate("MainWindow", "canny算子"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Scharr算子"))
        self.comboBox.setItemText(2, _translate("MainWindow", "sobel算子"))
        self.comboBox.setItemText(3, _translate("MainWindow", "log算子"))
        self.pushButton.setText(_translate("MainWindow", "新建正演文件"))
        self.pushButton_4.setText(_translate("MainWindow", "设置反射系数"))
        self.pushButton_7.setText(_translate("MainWindow", "图像识别"))
        self.pushButton_3.setText(_translate("MainWindow", "设置雷克子波"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "无经典模型"))
        self.label.setText(_translate("MainWindow", "采样时间（S）"))
        self.label_3.setText(_translate("MainWindow", "主频（HZ）"))
        self.label_2.setText(_translate("MainWindow", "采样间隔（S）"))
        self.radioButton.setText(_translate("MainWindow", "默认值"))
        self.label_4.setText(_translate("MainWindow", "设置道间距："))
        self.radioButton_2.setText(_translate("MainWindow", "默认值"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab), _translate("MainWindow", "正演模拟"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "文件信息读取"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "工具"))
        self.menu_5.setTitle(_translate("MainWindow", "帮助"))
        self.actionda.setText(_translate("MainWindow", "新建正演文件"))
        self.action1.setText(_translate("MainWindow", "保存文件"))
        self.action.setText(_translate("MainWindow", "帮助文档"))
        self.action_2.setText(_translate("MainWindow", "图像识别"))
        self.action_3.setText(_translate("MainWindow", "设置反射系数"))
        self.action_4.setText(_translate("MainWindow", "设置雷克子波"))
        self.action_5.setText(_translate("MainWindow", "频谱图"))
        self.action_6.setText(_translate("MainWindow", "合成地震记录"))
        self.actioncanny.setText(_translate("MainWindow", "canny算子"))
        self.actionScharr.setText(_translate("MainWindow", "Scharr算子"))
        self.actionsobel.setText(_translate("MainWindow", "sobel算子"))
        self.actionlog.setText(_translate("MainWindow", "log算子"))
    #1新建正演项目
    def new_project(self):
        self.ui_1 = new_project()
        self.ui_1.show()
    #2图像识别
    def opencv(self):
        self.type = self.comboBox.currentText()
        self.ui_2 = opencv(self.type)
        self.ui_2.show()
    #3雷克子波
    def Rake_wave(self):
        self.sampling_rate = self.lineEdit_2.text()
        # 主频
        self.Dominant_frequency = self.lineEdit_3.text()
        # 采样时间
        self.sampling_time = self.lineEdit.text()
        if self.sampling_rate == '' or self.sampling_time == '' or self.Dominant_frequency == '':
            QMessageBox.warning(self, "警告", "请先输入完整的参数！", QMessageBox.Yes | QMessageBox.No)
        else:
        #采样率
            self.ui_3 = Rake_wave(self.sampling_rate,self.Dominant_frequency,self.sampling_time)
            self.ui_3.show()
    #4设置反射系数
    def reflection_coe(self):
        file_name = "__data.png"
        if os.path.isfile(file_name) == False:
            QMessageBox.warning(self, "警告", "请先绘制图像！", QMessageBox.Yes | QMessageBox.Discard)
            return
        else:
            self.ui_4 = reflection_coe()
            self.ui_4.show()
    #5合成地震记录
    def synthetic_seismogram(self):

        my_file = pathlib.Path("project.json")
        if my_file.exists():
            with open(my_file, "r") as fr:
                f_ = json.load(fr)
                str_1 = re.findall("'sampling_rate': '(.*?)'", str(f_))
                str_2 = re.findall("'Dominant_frequency': '(.*?)'", str(f_))
                str_3 = re.findall("'sampling_time': '(.*?)'", str(f_))
                str_4 = re.search("'xishu'", str(f_))
                if len(str_1) == 0 or len(str_2) == 0 or len(str_3) == 0 or str_4 == None:
                    QMessageBox.warning(self, "警告", "请先确定主频，间隔，时间并设置雷克子波！", QMessageBox.Yes | QMessageBox.No)
                    return
                else:
                    self.ui_5 = synthetic_seismogram()
        else:
            QMessageBox.warning(self, "警告", "请先新建正演文件", QMessageBox.Yes | QMessageBox.No)
            return


    #6频谱图
    def spectrum_diagram(self):
        self.ui_6 = spectrum_diagram()
        self.ui_6.show()
    #自动填充默认值
    def full_value(self):
        #采样时间
        self.lineEdit.setText("0.032")
        #主频
        self.lineEdit_2.setText("0.001")
        #采样率
        self.lineEdit_3.setText("35")
    def full_value_2(self):
        #采样时间
        self.lineEdit_4.setText("5")



if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())