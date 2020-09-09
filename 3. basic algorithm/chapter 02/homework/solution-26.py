# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现一个反向迭代器
"""
class ReversedIterator:

    def __init__(self, l):
        self._l = l

    def __iter__(self):
        for each in self._l[::-1]:
            yield each

rt = iter(ReversedIterator([1, 2, 3, 4, 5]))
print(list(rt))