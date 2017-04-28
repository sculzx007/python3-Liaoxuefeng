#!/usr/bin/env python3
# -*-coding:utf-8 -*-
class Student(object):

	@property   # 把一个getter方法变成属性，只需要加上@property
	def score(self):
		return self._score

	@score.setter   # @property 创建了装饰器@score.setter，负责把setter方法变成属性赋值
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0-100')
		self._score = value

s = Student()
s.score = 50
print(s.score)