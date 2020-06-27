# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\github\PyQt\PyQt5\Chapter03\Test01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# 会自动弹出“新建窗体”对话框，如图3-3所示.
# 	在模板选项中，最常用的就是 Widget    (通用窗口)和 Main Window （主窗口).
# 	在 PyQt5 中 Widget被分离出来，用来替    代Dialog，并将 Widget放入了OtWidget模块库中。
#     按“Ctr1+R”快捷键，就可以看到窗口的预览效果了.

# objectName,控件对象名称。
#     geometry，相对坐标系。
#     sizePolicy，控件大小策略。
#     minimumSize，最小宽度、高度。
#     maximumSize，最大宽度、高度。如果想让窗口或控件的大小固定，则可以将 minimumSize 和l maximumSize 这两个属性设置成一样的数值。
#     font，字体，
#     Cursor,光标。
#     windowTitle,窗口标题。
#     windowslcon/icon,口图标/控件图标。
#     iconSize，图标大小，
#     toolTip，提示信息。
#     statusTip.任务栏提示信息。
# 	text，控件文本。
#     shortcut，快捷键
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(30, 50, 75, 23))
		self.pushButton.setObjectName("pushButton")
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
