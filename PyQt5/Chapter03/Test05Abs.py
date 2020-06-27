# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\github\PyQt\PyQt5\Chapter03\Test05Abs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# Vertical Spacer表示两个布局管理器不要彼此挨着，否则视觉效果会不好看。
# Horizontal Spacer表示“开始”按钮应该与栅格布局管理器尽可能离得远一些，
# 否则视觉效果也会不好看。
# HorizontalLine表示“开始"按钮与左边的两个布局管理器根本不是同一-个
# 类别，用一条线把它们区分开来。
# minimumSize和maximumSize属性用来设置控件在布局管理器中的最小尺寸和
# 最大尺寸，我们对Buton (按钮)的这两个属性按照图3-35所示进行设置。
# 每个窗口控件都有属于自己的两个尺寸:一个是sizeHint (尺寸提示) ;一个是
# minimumSize (最小尺寸)。前者是窗口控件的期望尺寸，后者则是窗口控件压缩时
# 所能够被压缩到的最小尺寸。
# sizePolicy 的作用是，如果窗口控件在布局管理器中的布局不能满足我们的需
# 求，那么就可以设置该窗口控件的sizePolicy来实现布局的微调。sizePolicy 也是每
#
# 对于水平策略和垂直策略，相关的解释如下。
#
# Fixed:窗口控件具有其 sizecint所提示的尺寸且尺寸不会再改变。
# Mininum: 窗口控件的 sizeHint所提示的尺寸就是它的最小尺寸：该窗口控
# 件不能被压缩得比这个值小，但可以变得更大。
# Maximum: 窗口控件的sizeFint 所提示的尺寸就是它的最大尺寸：该窗口控
# 件不能变得比这个值大，但它可以被压缩到minisizeHint给定的尺寸大小。
# Preferred:窗口控件的 sizcHint 所提示的尺寸就是它的期望尺寸:该窗口控
# 件可以缩小到 minisizeHint 所提示的尺寸，也可以变得比 sizeHint 所提示的尺
# 寸还要大。
# Expanding: 窗口控件可以缩小到 minisizeHint 所提示的尺寸，也可以变得比
# sizeHint所提示的尺寸大，但它希望能够变得更大。
# MinimumExpanding:窗口控件的sizeHTint所提示的尺寸就是它的最小尺寸:
# 该窗口控件不能被压缩得比这个值还小，但它希望能够变得更大。
# Ignored:无视窗口控件的 sizeHint 和 minisizeHint所提示的尺寸，按照默认
# 来设置。

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 24, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 48, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 42, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(135, 80, 48, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 80, 48, 16))
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(136, 190, 54, 20))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(136, 150, 54, 20))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(135, 110, 54, 20))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(200, 190, 54, 20))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(200, 150, 54, 20))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(200, 110, 54, 20))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.label.setText(_translate("MainWindow", "收益"))
        self.label_2.setText(_translate("MainWindow", "最大回撤"))
        self.label_3.setText(_translate("MainWindow", "sharp比"))
        self.label_4.setText(_translate("MainWindow", "最大收益"))
        self.label_5.setText(_translate("MainWindow", "最小收益"))
