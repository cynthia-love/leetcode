# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    输入一个大于2的正整数, 求将该数反复被2整除直到商小于2为止的次数
"""
"""
    分析, 3 / 2 = 1...1, 4/2=2, 2/2 = 1
    5/2 = 2.5, 2.5/2=1.25
    即求2^n <= x < 2^(n+1)这里的n
"""

def f(n):
    k = 1
    while 2**k <= n:
        k += 1
    return k-1

print(f(3))
print(f(4))
print(f(5))
print(f(6))
print(f(127))
print(f(128))

# 方法2, 原始方法
def f(n):
    count = 0
    while n // 2 >= 2:
        count += 1
        n = n / 2
    return count+1

print(f(3))
print(f(4))
print(f(5))
print(f(6))
print(f(127))
print(f(128))