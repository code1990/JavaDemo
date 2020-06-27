# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\github\PyQt\PyQt5\Chapter03\Test06Signal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#     信号（signal)和槽（slot）)是Qt的核心机制。在创建事件循环之后，通过建立
#     信号和槽的连接就可以实现对象之间的通信，当信号发射(emit) 时，连接的槽函
#     数将会自动执行。在PyQt5中，信号和槽通过QObject.signal.connect0连接。
# 	    所有从QObject 类或其子类(如 QWidget)派生的类都能够包含信号和槽。当
#     对象改变其状态时，信号就由该对象发射出去。槽用于接收信号，但它们是警通的
#     对象成员丽数，多个信号可以与单个槽进行连接，单个信号也可以与多个槽进行连
#     接。总之，信号和槽构建了一种强大的控件编程机制。

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.closeWinBtn = QtWidgets.QPushButton(Form)
        self.closeWinBtn.setGeometry(QtCore.QRect(100, 90, 75, 21))
        self.closeWinBtn.setObjectName("closeWinBtn")

        self.retranslateUi(Form)
        self.closeWinBtn.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.closeWinBtn.setText(_translate("Form", "关闭窗口"))
