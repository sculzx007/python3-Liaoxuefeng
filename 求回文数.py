# /usr/bin/env python3
# -*- coding:utf-8 -*-

def is_palindrome(n):
    return str(n) == str(n)[::-1]    
    # 回文数的定义，从左往右读和从右往左读是一样的，str(n)代表从左往右，str(n)[::-1]代表从右往左，[::-1]表示从右往左数，步进为1

output = filter(is_palindrome, range(1, 1000))

print(list(output))