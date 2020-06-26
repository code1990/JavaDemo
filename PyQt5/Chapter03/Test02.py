# 实现界面与逻辑的分离方法很简单品
# 并继承界面文件的主窗口类即可。
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Test02MainWin import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	sys.exit(app.exec_())
