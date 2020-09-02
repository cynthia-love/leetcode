# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    重载示例: 多维向量类
"""
class Vector:
    """Represent a vector in a multidimensional space"""

    def __init__(self, d: int):
        """Create d-dimensional vector of zeros"""
        self._vector = [0]*d

    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._vector)

    def __getitem__(self, i):
        """Return the i-th coordinate of the vector"""
        return self._vector[i]

    def __setitem__(self, i, value):
        """Set the i-th coordinate of vector to a given value"""
        self._vector[i] = value

    def __eq__(self, other):
        """Return True if vector has same coordinates as other"""
        return self._vector == other._vector

    def __ne__(self, other):
        """Return True if victor differ from other"""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector"""
        return str(self._vector)

    # 这里用到了python的鸭子机制, 即不要求other为Vector类型
    # 只要其有__len__和__getitem__方法, 且长度相等, 就允许相加
    def __add__(self, other):
        # Return sum of two vectors
        # other doesn't have to be type of Vector
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError("dimensions must agree")

        res = Vector(len(self))
        for i in range(len(self)):
            res[i] = self[i] + other[i]

        return res

v = Vector(5)
print(v)
v[1] = 8
v[-1] = 10
print(v)

u = v + v
print(u)
u = v + [8, 100, 888, 11, 10]
print(u)

for each in v:  # implicit iteration via __len__ and __getitem__
    print(each)
