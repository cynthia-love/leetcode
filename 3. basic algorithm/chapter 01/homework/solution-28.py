# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    求p范数
"""

def f(l:list, p=2):

    return sum(x**p for x in l)**(1/p)

print(f([1, 2, 3]))