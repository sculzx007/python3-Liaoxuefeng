# /usr/bin/env python3
# -*- coding:utf-8 -*-

from functiontools import reduce

#方法1 
'''
思路：先找到小数点的位置，再分成左右两部分算出两个值最后再加在一起
'''
def str2float(s):
    def dot(s):
        for i in list(range(len(s)-1)):
            if s[i] == '.':
                return i

    def left(char):
        return char[:dot(char)]

    dotLeft = left(s)

    def right(char):
        t = char[dot(char)+1:]
        return t[::-1]

    dotRight = right(s)

    def fn1(x, y):
        return x * 10 + y

    def fn2(x, y):
        return x * 0.1 + y

    def char2num(char):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[char]

    L = reduce(fn1, map(char2num, dotLeft))
    R = reduce(fn2, map(char2num, dotRight))

    return L + R * 0.1


'''
方法2：

from functools import reduce

def str2float(s):
    XiaoShu = len(s) - s.find('.') - 1      # 计算小数位数
    s = s.replace('.', '')                  # 删除小数点
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    num = reduce(lambda x, y: 10 * x + y, map(char2num, s))                                        # 转换成不带小数的整数
    num = num / (10 ** XiaoShu)                             # 移动小数点
    return num

print('str2float(\'123.456\') =', str2float('123.456'))
'''