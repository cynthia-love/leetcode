# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    我的地盘听我的
"""

# 所有的python函数都有返回值, 不写就是None
def f():
    a = 1

b = f()
print(b)  # None

# python返回值默认可以是任何类型, 任意多个(可用tuple或list打包)
def f1():
    return 1, "a", 2
x, y, z = f1()
print(x, y, z)

from typing import List
# python也可以指定返回值类型
def f2()->List[int]:
    return [1, 2, 3]
print(f2())
x, y, z = f2()
print(x, y, z)

# 变量作用域; 函数外的称为全局变量, 函数里的称为局部变量, 外部访问不到
g_x = 3
def f3():
    l_y = g_x
    print(g_x, l_y)
f3()

# 特别地, 如果在函数内试图修改全局变量, 则该变量自动降级为局部变量
# 所以, 永远不要在函数内部试图去修改全局变量; 真的极个别情况下有需求的话, 用global声明一个变量名指向对应全局变量
def f4():
    g_x = 8
f4()
print(g_x)

def f5():
    global g_x
    g_x = 100
f5()
print(g_x)  # 可以看到这里g_x值变成100了

# **********************************************************************************************************************
# 上述函数作用域和全局变量的关系, 再降一级, 函数和其内嵌函数之间也存在类似关系, 只不过global变成了nonlocal
def f6():
    x = 8
    def f():
        print(x)   # 这种内嵌函数访问外部函数变量(不是全局变量)的情况, 这里内部函数称为闭包
    f()
f6()

# 同样, 尝试修改, 会自动降级成内部函数的局部变量
def f6():
    x = 8
    def f():
        x = 10
        print(x)
    f()
    print(x)
f6()

# 同样, 可以用nonlocal强制升级作用域
# 当然, 内嵌函数也是可以用global的, 直接升级到全局变量; 而nonlocal只升一层
def f7():
    x = 8
    def f():
        nonlocal x
        x = 1000
        global g_x
        g_x = 9999
    f()
    print(x)
f7()
print(g_x)

# 特别地, 内嵌函数也可以外部传参
def f8(x):
    def f(y):
        print(x, y)
    f(x)  # 笨方法是过一手f8()再显示调一下f()
f8(8)

def f9(x):
    def f(y):
        print(x, y)
    return f
f9(100)(200)  # 之所以能这么写是因为f9()的返回值是一个函数, 且带参数, 所以能再加一个括号(200)
# 这种写法有意义吗, 完全可以直接return f(x)啊