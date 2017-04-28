#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@修饰符有点像函数指针，
python解释器发现执行的时候如果碰到@修饰的函数，首先就解析它，找到它对应的函数进行调用，
并且会把@修饰下面一行的函数作为一个函数指针传入它对应的函数
'''
import functools
#两层嵌套的装饰器
def log(func):
    @functools.wraps(func)  # 将原始函数now()的__name__等属性复制到wrapper()函数中，否则有些依赖函数签名的代码会出错
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log   # 相当于执行了now = log(now)
def now():
    print('2017-4-21')

now()
print(now.__name__)  #验证now函数是不是原来定义的函数now()
'''
注意！！！！
调用now()后，执行的不是定义的now()函数
而是将变量名now指向了log中返回的wrapper函数，这是一个新的函数，
只不过因为wrapper函数返回的是原始函数而已，即与原始函数的表达式相同，但不是原始函数
而原来的now()函数是仍然存在
'''


'''
#三层嵌套的装饰器
def log2(text):
    def decorator(func2):
        def wrapper2(*args, **kw):
            print('%s %s():' % (text, func2.__name__))
            return func2(*args, **kw)
        return wrapper2
    return decorator

@log('execute')     #相当于执行了 now = log('execute')(now)
def now2():
    print('2017-04-21')

now2()
print(now2.__name__)

'''