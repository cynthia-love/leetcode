# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
def f(l: list):
    for each in l:
        each *= 2

# 该函数并不能直接改变l的元素
"""
    l[0]->xx       l[0] = 新值, 更新l[0]存储的指针指向
           ↑              
          each     each = 新值, 只是改变标识符each的指向
"""
l = [1, 2, 3, 4]
f(l)
print(l)