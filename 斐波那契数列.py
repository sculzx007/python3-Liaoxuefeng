#!/usr/bin/env python3
# -*-coding:utf-8 -*-

'''
学会 __iter__的使用
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

fib1 = []
for n in Fib1():
	fib1.append(n)

print(fib1)