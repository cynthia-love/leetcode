# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现Sequence的==

    ==要求长度相等且每个元素都相同

"""

class Sequence:
    def __init__(self, l):
        self._l = l

    def __len__(self):
        return len(self._l)

    def __getitem__(self, index):
        return self._l[index]

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

s1 = Sequence([1, 2, 3])
s2 = Sequence([1, 2, 3])
s3 = Sequence([1, 2, 4])
s4 = Sequence([1, 2, 3, 4])

print(s1 == s2)
print(s1 == s3)
print(s1 == s4)
