# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    基于Python的解析语法和内置函数sum, 写一个单独的命令来计算1~n的平方和
"""
# solution-4的第一种写法好像就符合这个要求
f = lambda n: sum(x*x for x in range(1, n+1))
print(f(10))
print(f(2))