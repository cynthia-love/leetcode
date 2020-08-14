# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    迭代器和生成器
    注意, 生成器是迭代器的一种(本身就是迭代器), 可以直接用next()函数
    而list, set, tuple等只是可迭代对象, 需用iter()才能转化成迭代器
"""

"""迭代器"""
# 注意, 可迭代的 != 是迭代器
# list, tuple, set, str, dict, file, generator都是可迭代的, 但其本身并不是迭代器
# 只有迭代器才能调用next(), 没有后续元素抛出StopIteration
# 对于可迭代的对象, 可以通过iter(obj)获取其对应的迭代器
# for循环实际上是自动实现了获取迭代器->next->没有后续元素抛出StopIteration终止
l = [8, 7, 6, 5, 4]
it1 = iter(l)
it2 = iter(l)
# 同一个可迭代对象可以创建多个迭代器, 每个迭代器自己维护自己的进度状态
print(next(it1), next(it2))  # 8, 8, 而不是8, 7
# 迭代器是对于原可迭代对象的元素是引用(位置索引), 而不是复制, 比如这里改变l[1], 则迭代器输出内容也跟着改
l[1] = 100
print(next(it1), next(it2))
# 迭代器可以通过list(), set()将引用强制转换为实例
l1 = list(it1)
l[4] = 100
print(l1)  # [6, 5, 4], 注意点1: 只转换迭代器尚未迭代部分, 注意点2: 因为不是引用了, 再改l, l1不会跟着变

"""生成器, 迭代器的一种"""
def f_range(n):
    i = 0
    while i <= n-1:
        yield i
        i += 1
        if i == 3:
            return  # 带yield的函数里可以有return, 但return不能带参数, return相当于raise StopIteration

# 生成器, 懒惰计算(好好理解这个词), 需要时才去计算, 整个系列的数不需要一次性全部算出来留在内存里
# 当没有下一个yield或者遇到不带参数的return, 抛出StopIteration异常
for i in f_range(8):  # range就是这么实现的, 比如range(1000000)并不是一次生成一个长一百万的list
    print(i)

# 生成器应用场景-无限斐波那契数列
def f_fibonacci():
    # 0, 1, 1, 2, 3, 5
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x+y

ge = f_fibonacci()
for i in range(10):
    print(next(ge))

# 比较下面三种计算因子的函数
def f1(n):
    # 传统函数, 需要立刻构建数据结构存储所有的值
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res

print(f1(8))

def f2(n):
    # 生成器, 用到时才算, 没用到则函数悬在那不往下执行
    for i in range(1, n+1):
        if n % i == 0:
            yield i
print(list(f2(8)))

def f3(n):
    # 优化后的生成器
    k = 1
    while k < n**0.5:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    # n**0.5要单提出来, 比如4*4=16, 4只能输出一次
    # 当然也可以在 yield n // k 前面判断, 但在循环里面增加逻辑肯定不如在外面性能好
    if k == n**0.5:
        yield k
print(list(f3(16)))