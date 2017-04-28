#! usr/bin/env python3
# -*- coding:utf-8 -*-

"""
杨辉三角

代码示例：
def triangles():
     l=[1]
     while True:
         l=[0]+l+[0]
         x=[l[i]+l[i+1] for i in range(len(l)-1)]
         l=x
         yield x
     return triangles()
逐行分析

函数声明
杨辉三角第一行
循环，循环条件为True（也就是一直循环下去，没有终点）
在列表前后都添加上0（之所以要这么做是为了简化后面计算）
列表生成式 生成项为l[i]+l[i],也就是循环当前项与后一项的和。range范围为0到len(l)-1这个是根据观察得出来的，后面会解释。
将l的值替换成x的值
用yield语句输出x
返回一个生成器
解题思路

观察：
    通过观察杨辉三角，发现其每一行列表中的元素，通过相邻两数相加就是下一行列表中的元素。
解法
    我们可以通过为当前列表两端分别加上一个元素0,并使相邻两项相加就可以得出下一行列表中的元素了。通过列表生成式可以方便的写成[l[i]+l[i+1] for i in range(len(l)-1)]

个人看法

本章老师某些地方解释有些不清楚，例如fib函数其实并不是generator，其返回值才是generator（fib(10)）。fib应该叫做‘生成器函数’
type(fib) #"function"
type(fib()) #"generator"

第8行语句的指令就是返回一个gennerator triangles()
"""
def triangles():
    L = [1]

    while True:
        yield L
        L = [L[0]] + [L[i] + L[i + 1] for i in range(len(L)-1)] + [L[-1]]
        #  解释：[L[0]] = [1], [L[-1]] = [L[0]] = [1],这是杨辉三角中的首和尾
        #  [L[i] + L[i + 1]表示相邻两个数相加，并加入到列表中


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break