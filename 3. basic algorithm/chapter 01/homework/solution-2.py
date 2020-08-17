# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    is_even(k)判断k是不是偶数
    函数中不能使用乘法, 除法, 取余
"""
# 思路, 按位与取最后一位
def is_even(k: int) -> bool:

    return k & 1 == 0


print(is_even(0))
print(is_even(1))
print(is_even(2))
print(is_even(3))
print(is_even(12128))
print(is_even(11928398493829483))