#     方法二:使用@property访问类的属性。
#     同方法一，首先定义了一个MyClass类，该类必须继承自object类，它有一个
#     私有变量 param. @property 可以将Python 定义的函数“当作”属性访问，从而提
#     供更加友好的访间方式，但是有时候 setter/getter 也是需要的。
class MyClass(object):
	def __init__(self):
		self._param = None

	@property
	def param(self):
		print("get param: %s" % self._param)
		return self._param

	@param.setter
	def param(self, value):
		print("set param: %s" % self._param)
		self._param = value

	@param.deleter
	def param(self):
		print("del param: %s" % self._param)
		del self._param


if __name__ == "__main__":
	cls = MyClass()
	cls.param = 10
	print("current param : %s " % cls.param)
	del cls.param
