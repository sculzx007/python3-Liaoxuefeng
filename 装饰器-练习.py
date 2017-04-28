#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
（1）写出一个decorator，能在函数调用前后打印出'begin call' 和'end call'
（2）写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
'''

# 第二题
import functools

def log(func):
    if isinstance(func, str):
        def decorator(func1):
            @functools.wraps(func1)
            def wrapper(*args, **kw):
                print('begin call')
                print('%s:%s()' % (func, func1()))
                print('end call')
                return func1(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            func()
            print('end call')
        return wrapper

# 传入log的参数为函数时
@log
def f1():
    print('f1')

f1()

# 传入log的参数是文本时
@log('execute')
def f2():
    return('f2')  #注意，这里不使用print()，而是使用return

f2()

