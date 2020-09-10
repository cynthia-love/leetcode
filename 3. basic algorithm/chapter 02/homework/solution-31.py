# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    扩展Progression, 每个值是前两个值差的绝对值
    构造函数接收两个数, 默认2和200
"""
from abc import ABCMeta, abstractmethod
class Progression(metaclass=ABCMeta):
    def __init__(self, first=0):
        self._current = first

    @abstractmethod
    def _advance(self):
        """to be implemented by subclass"""

    def __iter__(self):
        while True:
            yield self._current
            self._advance()

class MProgression(Progression):

    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._next = second

    def _advance(self):
        self._current, self._next = self._next, abs(self._next-self._current)

m = iter(MProgression())
print(next(m))
print(next(m))
print(next(m))
print(next(m))