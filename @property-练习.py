#!/usr/bin/env python3
# -*-coding:utf-8 -*-

class Screen(object):

	# @property相当于把一个getter方法转化属性，该属性的作用是获得参数信息，@property会生成一个@width.setter
	@property
	def width(self):
		return self._width

	# 使用@property后，若想通过属性设置信息，则需要使用@width.setter，将前面@property生成的@width.setter指向这里的函数
	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self, height):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	# 如果想定义只读，可只设置@property，即只有getter方法，setter方法因为没有指向，故无法获取
	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768

print(s.resolution)

assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution  # 断言语句