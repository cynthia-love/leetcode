# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    斐波那契, 前两个数为2, 2, 找到第8个
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

class FibonacciProgression(Progression):
    def __init__(self, first, second):
        super().__init__(first)
        self._next = second

    def _advance(self):
        self._current, self._next = self._next, self._current+self._next

fp = iter(FibonacciProgression(2, 2))
print([next(fp) for _ in range(8)][-1])