# 每个对象级别的变量，在调用时一定要带上self表明属于当前对象，比如self.name。
# _init方法属于Python语言的构造函数，一个类只能有一个__init_方法，用于初始化类及其变量。
# 通过对象的setCount（）、getCount）函数处理它的变量。
class MyClass:
	count = 0
	name = 'DefaultName'

	def __init__(self, name):
		self.name = name
		print('类的变量是%s\n对象的变量是:%s' % (MyClass.name, self.name))

	def setCount(self, count):
		self.count = count

	def getCount(self):
		return self.count


if __name__ == "__main__":
	cls = MyClass('lisi')
	cls.setCount(10)
	print('count=%d' % cls.getCount())