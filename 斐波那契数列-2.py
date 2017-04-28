#!/usr/bin/env python3
# -*-coding:utf-8 -*-

'''
学会 __getitem__的使用
'''

'''
'''
class Fib1(object):
	def __init__(self):
		self.a, self.b = 0, 1  #初始化两个计数器 a，b

	def __iter__(self):
		return self   #设置可迭代对象，由于实例本身就是迭代对象，故返回其本身

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b  # 计算下一个值

		if self.a > 100:
			raise StopIteration()

		return self.a      # 返回下一个值

'''fib1 = []
for n in Fib1():
	fib1.append(n)

print(fib1)

'''

# 由于Fib1()无法像list一样可以使用下标索引，也无法使用切片功能，故对其进行改进
class Fib2(object):
	def __getitem__(self, n):
		if isinstance(n, int):     # 如果 n 是索引
			a, b = 1, 1

			for x in range(n):
				a, b = b, a + b

		if isinstance(n, slice):   # 如果 n 是切片
			start = n.start
			stop = n.stop

			if start is None:
				start = 0

			a, b = 1, 1

			L = []

			for x in range(stop):
				if x >= start:
					L.append(a)

				a, b = b, a + b

			return L


f = Fib2()
print(f[0:5])
print(f[:10])



'''
Fib2()类虽然能使用切片和索引，但步进、负数都没有进行相应的处理，故而还有改进的空间
'''