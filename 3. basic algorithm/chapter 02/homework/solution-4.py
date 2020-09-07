# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    编写一个Flower类, 名字str, 花瓣数量int, 价格float
    支持初始化以及3种属性的set/get方法
"""
class Flower:
    """A Flower"""
    def __init__(self, name, petal, price):
        """
        Create a new flower instance

        :param name: the name of the flower (e.g., 'rose')
        :param petal: the count of the petal
        :param price: the price of the flower (measured in dollars)
        """
        self._name = name
        self._petal = petal
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, val):
        self._name = val

    def get_petal(self):
        return self._petal

    def set_petal(self, val):
        self._petal = val

    def get_price(self):
        return self._price

    def set_price(self, val):
        self._price = val

f = Flower("rose", 100, 28)
f.set_price(88)
print(f.get_name(), f.get_price())


