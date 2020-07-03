# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    断言
"""

# 当assert后边的条件为假的时候程序自动崩溃并抛出AssertionError异常
# 感觉没啥用, if也能实现
x = 1.1

assert isinstance(x, int)

print("断言过了")