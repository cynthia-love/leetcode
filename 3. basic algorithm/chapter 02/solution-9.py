# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    抽象基类
    如果一个类的唯一目的就是被继承, 那这个类就可以声明为抽象基类
    抽象基类在python里其实不是那么必要, 因为python是鸭子机制, 不显式控制数据类型

    python的抽象基类更多地是利用其模板设计模式, 节省部分公共功能的实现

    比如collections.Sequence, 把__len__和__getitem___声明为抽象方法
    而__contains__, __index__, __count__直接实现

    还要注意一点, 抽象基类里已经实现的方法, 子类同样也是可以覆盖的!!!
"""

# 自己写一个collections.Sequence

from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, i):
        """Return the element at index i of the sequence"""

    def __contains__(self, item):
        """Return True if item found in the sequence; False otherwise"""
        for i in range(len(self)):
            if self[i] == item:
                return True

        return False

    def index(self, val):
        """Return leftmost index at which val is found( or raise ValeError)"""
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError('value not in the sequence')

    def count(self, val):
        """Return the number of elements equal to given value"""
        k = 0
        for i in range(len(self)):
            if self[i] == val:
                k += 1
        return k

class MySequence(Sequence):

    def __len__(self):
        return 10

    def __getitem__(self, i):
        return i

    def index(self, val):
        return 100

ms = MySequence()
print(ms.index(8))
print(len(ms))
for i in range(len(ms)):
    print(ms[i])
