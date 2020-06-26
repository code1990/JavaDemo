# 类的动态属性
#     如果不希望类的某属性被悄悄地访问、赋值或修改，希望在被访问、赋值或修
#     改时能得到一些通知，那么可以使用函数 property0.函数原型是:
#     property(tfgett,fset [, fdel[, doc】111)
#     它返回新式类(继承了 objct 的类)的一个属性，其中fget是属性被访问时执
#     行的方法，fset是属性被赋值时执行的方法，fdel是属性被删除时执行的方法。
# 	下面代码定义了一个MyClass类，该类必须继承自object类，它有一个私有变量_param。
# 方法一：使用类的属性。
class MyClass(object):
	def __init__(self):
		self._param = None

	def getParam(self):
		print("get param: %s" % self._param)
		return self._param

	def setParam(self, value):
		print("set param: %s" % self._param)
		self._param = value

	def delParam(self):
		print("del param: %s" % self._param)
		del self._param

	param = property(getParam, setParam, delParam)


if __name__ == "__main__":
	cls = MyClass()
	cls.param = 10
	print("current param : %s " % cls.param)
	del cls.param
