import sys
# 本代码 只能使用命令行执行 python chapter01.py
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

widget.resize(360, 360)

widget.setWindowTitle("hello pyqt5")

widget.show()

sys.exit(app.exec_())
