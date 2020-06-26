# 字典
# 1
print('\n#1')
zdict = {}
zdict['w1'] = 'hello'
zdict['w2'] = 'ziwang.com'
print('zdict,', zdict)

# 2
print('\n#2')
vdict = {'url1': 'TopQuant.vip'
	, 'url2': 'www.TopQuant.vip'
	, 'url3': 'ziwang.com'}
print('vdict,', vdict)

# 3
print('\n#3')
s2 = zdict['w1']
print('s2,', s2)
s3 = vdict['url2']
print('s3,', s3)

#     字典内置函数和方法如下。
#     (1) Python 字典包含以下内置函数。
#     cmp(dictl. dict2)：比较两个字典元素
#     len(dict)计算字典元素的个数，即键的总数
#     strd dict)输出字典可打印的字符串标识。
#     type(variable):返回输入的变量类型，如果变量是字典，就返回字典类型。
#     (2) Python 字典包含以下内置方法。
#     radiansdict.clear(:删除字典内所有元素
# 	radiansdict.copyO：返回一个字典的浅复制。
# 	radiansdict.fromkeys(:创建一个新字典，以序列seq中的元素做字典的键，
# 	val为字典所有键对应的初始值。
# 	radiansdict.get(key, default-None):返回指定键的值，如果值不在字典中，则
# 	返回 default 值。
# 	radiansdict.has key(key)：如果键在字典中，则返回true:否则返回false.
# 	radiansdict.items0：以列表形式返回可途历的(键，值)元组数组。
# 	radiansdict keys(): 以列表形式返回一个字典中所有的键。
# 	radiansdict.setdefault(key, default-None)：和 get0)类似，但如果键已经不存在
# 	于字典中，则将添加键并将值设为dcfault.
# 	radiansdict.update(dict2):把 dict2的键-值对更新到字典中。
# 	radiansdict.valuesO：:以列表形式返回字典中所有的值。
