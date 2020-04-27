# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第6章 函数
    为了让程序的代码更为简单, 就需要把程序分解为较小的组成部分, 三种方法: 函数, 类, 模块
"""

"""
    函数基本知识
"""

# 最简单的函数
def f():
    print("Hello function")

f()

for i in range(3):
    f()

# 带参数的函数
def f2(name):
    print("Hello "+name)
f2("Haha")

def f3(name1, name2):
    print(name1, name2)
f3("Lucy", "Lily")

# 带返回值的函数
def f4(name):
    return "带返回值"+name

print(f4("Jim"))

def f5():
    return 1, 2, 3
x, y, z = f5()  # 如前面所说, tuple的关键是, 而不是(), 所以这里相当于返回(1, 2, 3)
print(x, y, z)
print(type(f5()))  # <class 'tuple'>
