# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    扩展Progression, 每个值是前一个数值的平方根
    构造函数默认参数65536
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

    def __init__(self, first=65536):
        super().__init__(first)

    def _advance(self):
        self._current = self._current**0.5

m = iter(MProgression())
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))

