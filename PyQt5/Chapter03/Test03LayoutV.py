# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\github\PyQt\PyQt5\Chapter03\Test03LayoutV.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#     Qt Designer提供了4种窗口布局方式，分别是：
# 	Vertical Layout (垂直布局)、
#     Horizontal Layout(水平布局)、
# 	Grid Layout(橱格布局)和
# 	Form Layout (表单布局).

# 垂直布局:控件默认按照从上到下的顺序进行纵向添加.
#     水平布局：控件默认按照从左到右的顺序进行横向添加。
#     栅格布局：将窗口控件放入一个网格之中，然后将它们合理地划分成若干行
#     (row)和列 (column)，并把其中的每个窗口控件放置在合适的单元(cell)
#     中，这里的单元即是指由行和列交又所划分出来的空间。
#
# 	表单布局:控件以两列的形式布局在表单中，其中左列包含标签，右列包含    输入控件。
#     一般进行布局有两种方式：一是通过布局管理器进行布局：二是通过容器控    件进行布局
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 110, 355, 210))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
