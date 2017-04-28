# /usr/bin/env pyhton3
# -*-coding:utf-8 -*-


'''
埃式筛法求解素数：
首先，列出从 2 开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数 2，它一定是素数，然后用 2 把序列的 2 的倍数筛掉：
3, , 5, , 7, , 9, , 11, , 13, , 15, , 17, , 19, , ...
取新序列的第一个数 3，它一定是素数，然后用 3 把序列的 3 的倍数筛
掉：
5, , 7, , , , 11, , 13, , , , 17, , 19, , ...
取新序列的第一个数 5，然后用 5 把序列的 5 的倍数筛掉：
7, , , , 11, , 13, , , , 17, , 19, , ...
不断筛下去，就可以得到所有的素数。
'''


# 构建一个从3开始的奇数序列
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数
def not_divisible(n):
    return lambda x: x % n > 0

# 定义一个生成器，不断返回下一个素数
def primse():
    yield 2          # 初始化序列

    it = odd_iter()  # 返回序列的第一个数

    while True:
        n = next(it)
        yield n

        it = filter(not_divisible(n), it) # 构造新的序列

L = []
for n in primse():
    if n < 1000:
        L.append(n)
        
    else:
        break

print(L)