# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现Vector类的__mul__方法, v1*v2返回点积
"""

class Vector:
    def __init__(self, l):
        self._l = l

    def __len__(self):
        return len(self._l)

    def __getitem__(self, item):
        return self._l[item]

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            l = [x*other for x in self._l]
            return Vector(l)
        elif isinstance(other, Vector):
            if len(self) == len(other):
                return sum(self[i]*other[i] for i in range(len(self)))

        raise ValueError("illegal parameter")

v1 = Vector([1, 2, 3])
v2 = Vector([1, 2, 3])
print(list(v1*3.1))
print(v1*v2)
v3 = Vector([1, 2, 3, 4])
print(v1*v3)