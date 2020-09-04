# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现Vector类的__neg__方法
"""
class Vector:
    def __init__(self, n):
        self._vector = [0]*n

    def __len__(self):
        return len(self._vector)

    def __getitem__(self, item):
        return self._vector[item]

    def __setitem__(self, key, value):
        self._vector[key] = value

    def __neg__(self):
        res = Vector(len(self))

        for i in range(len(self)):
            res[i] = -self[i]
        return res

v1 = Vector(5)
v1[1] = 8
v1[4] = 88
v2 = -v1
print([v2[i] for i in range(len(v2))])