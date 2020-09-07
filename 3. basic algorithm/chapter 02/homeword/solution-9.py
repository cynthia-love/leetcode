# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现Vector的__sub__方法
"""

class Vector:
    def __init__(self, l: list):
        self._vector = l

    def __len__(self):
        return len(self._vector)

    def __getitem__(self, item):
        return self._vector[item]

    def __sub__(self, other):
        if len(self) == len(other):
            return Vector([self[i]-other[i] for i in range(len(self))])
        raise TypeError

v1 = Vector([8, 7, 6, 2])
v2 = Vector([6, 5, 4, 3])
for each in v1-v2:
    print(each)