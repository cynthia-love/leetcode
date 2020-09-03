# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    浅拷贝深拷贝
"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l = [l1, l2]

ll1 = l  # 只是创建一个别名, 没有拷贝
print(id(ll1), id(l))

ll2 = list(l)  # 浅拷贝
print(id(l), id(ll2))
print(id(l[0]), id(ll2[0]))

import copy
ll3 = copy.deepcopy(l)  # 深拷贝
print(id(l), id(ll3))
print(id(l[0]), id(ll3[0]))