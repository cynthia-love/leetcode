# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    递归, 函数自己调自己
    默认情况下, Python限制递归层数最高100
"""

# 阶乘
def f1(x: int):
    sum = 1
    for i in range(x):
        sum *= i+1
    return sum

print(f1(5))

def r_f1(x: int):
    if x == 1: return 1
    return x*r_f1(x-1)
print(f1(5))

# 斐波那契数列
def r_f2(x: int):
    # if x == 1: return 1
    # if x == 2: return 1
    # if x == 1 or x == 2: return 1
    if x in [1, 2]: return 1
    return r_f2(x-1)+r_f2(x-2)
print(r_f2(12))

# 汉诺塔, X, Y, Z 三根柱子, n个盘子
"""
    如果n=1, X->Z
    如果n=2, X->Y, X->Z, Y->Z
    如果n=3, 把上面两个->Y, X->Z, Y的2个->Z
    如果n=4, 把上面三个->Y, X->Z, Y的3个->Z
"""
def hanoi(n, f, b, t):  # from , by, to
    if n == 1:
        # 如果只有一个, 那直接from->to
        print(f+"->"+t)
    else:
        # 如果有多个, 相当于
        # 上面n-1个借to到by上
        hanoi(n-1, f, t, b)
        # 最底下1个from->to
        print(f+"->"+t)
        # by上的n-1个借from到to上
        hanoi(n-1, b, f, t)

hanoi(5, "X", "Y", "Z")
