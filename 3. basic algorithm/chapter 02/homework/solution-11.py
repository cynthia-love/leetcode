# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    改造Vector, 不光支持v+[1, 2, 3], 还支持[1, 2, 3]+v
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

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("not the same dimension")

        res = Vector(len(self))
        for i in range(len(self)):
            res[i] = self[i] + other[i]

        return res

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError("not the same dimension")

        res = Vector(len(self))
        for i in range(len(self)):
            res[i] = other[i] + self[i]

        return res

v = Vector(3)
v[0] = 8
v[1] = 88
v[2] = 888
for each in v:
    print(each)

v1 = v + [1, 11, 111]
for each in v1:
    print(each)

v2 = [1, 11, 111] + v
print(list(v2))