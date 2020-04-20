# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    三元操作符
"""

x = 3
y = True if x >= 5 else False
print(y)

z = 5 if x >= 5 else (8 if y else 100)
print(z)