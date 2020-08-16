# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    编写一个python函数, is_multiple(n, m), 接收两个正数, 如果n是m的倍数, 返回True, 否则False
"""
def is_multiple(n: int, m: int) -> bool:
    return n % m == 0 if m else False  # 注意处理m为0的情况

print(is_multiple(10, 2))
print(is_multiple(10, 3))
print(is_multiple(10, 0))

# 当然, 根据请求原谅比得到许可更容易的原则, m为0毕竟概率低, 可以用try except
def is_multiple(n: int, m: int) -> bool:
    try:
        return n % m == 0
    except ZeroDivisionError:
        return False

print(is_multiple(10, 2))
print(is_multiple(10, 3))
print(is_multiple(10, 0))