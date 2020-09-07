# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现Sequence的<
    字典顺序
    即有限长度内比不出来才去比长度

"""

class Sequence:
    def __init__(self, l):
        self._l = l

    def __len__(self):
        return len(self._l)

    def __getitem__(self, index):
        return self._l[index]

    def __lt__(self, other):
        for i in range(min(len(self), len(other))):
            if self[i] > other[i]:
                return False
            if self[i] < other[i]:
                return True

        return len(self) < len(other)

s1 = Sequence([1, 2, 3])
s2 = Sequence([1, 2, 3])
s3 = Sequence([1, 3, 4])
s4 = Sequence([1, 1, 2])
s5 = Sequence([1, 2, 3, 4])
print(s1 < s2, s1 < s3, s1 < s4, s1 < s5)
