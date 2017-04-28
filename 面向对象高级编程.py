#!/usr/bin/env python3
# -*-coding:utf-8 -*-

from types import MethodType

class Student(object):
	pass

def set_age(self, age):
		self.age = age


s = Student()
s.set_age = MethodType(set_age, s)   # 给实例s绑定一个方法 set_age()
s.set_age(25)
print(s.age)

def set_score(self, score):
	self.score = score

Student.set_score = MethodType(set_score, Student)   # 给类Student绑定一个方法 set_score，所有的实例都能调用这个方法

s.set_score(100)
print(s.score)