# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    等差数列, 0开始, 增量128, 计算到达2**63或更大的数时需要执行多少次
"""

from abc import ABCMeta, abstractmethod
class Progression(metaclass=ABCMeta):
    def __init__(self, first):
        self._current = first

    def _advance(self):
        """calculate next value"""

    def __iter__(self):
        while True:
            yield self._current
            self._advance()

class ArithmetricProgression(Progression):

    def __init__(self, first, step):
        super().__init__(first)
        self._step = step

    def _advance(self):
        self._current += self._step


ap = iter(ArithmetricProgression(0, 128))

res, count = 0, 0

# 按实际运行去计算是算不出来的
# 只能用取巧的办法, 计算2**63的索引位置+1
t = 2**63

if t % 128 == 0:
    print(t // 128)

else:
    print(t // 128 + 1)
