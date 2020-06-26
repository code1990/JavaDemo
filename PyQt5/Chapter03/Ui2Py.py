# ui转换成py的转换工具
import os
import os.path

# 转换脚本的位置
root_path = r'F:\Python\Python36\Scripts\pyuic5.exe'
# UI文件所在的路径
dir_path = r'F:\github\PyQt\PyQt5\Chapter03'


# F:\Python\Python36\Scripts\pyuic5.exe -o F:\github\PyQt\PyQt5\Chapter03\Test01.py F:\github\PyQt\PyQt5\Chapter03\Test01.ui

# 列出目录下的所有ui文件
def get_ui_list():
	ui_list = []
	files = os.listdir(dir_path)
	for filename in files:
		# print(dir_path + os.sep + filename)
		# print(filename)
		if os.path.splitext(filename)[1] == '.ui':
			ui_list.append(dir_path + os.sep + filename)

	return ui_list


# 把后缀为ui的文件改成后缀为py的文件名
def transPyFile(filename):
	return os.path.splitext(filename)[0] + '.py'


# 调用系统命令把ui转换成py
def runMain():
	ui_list = get_ui_list()
	for ui_file in ui_list:
		py_file = transPyFile(ui_file)
		cmd = '{root_path} -o {py_file} {ui_file}'.format(root_path=root_path, py_file=py_file, ui_file=ui_file)
		print(cmd)
	# os.system(cmd)


###### 程序的主入口
if __name__ == "__main__":
	runMain()
