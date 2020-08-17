# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    索引越界, 打印信息
"""

l = [1, 2, 3]

try:
    print(l[4])
except IndexError:
    print("Don't try buffer overflow attacks in Python!")