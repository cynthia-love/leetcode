# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改Vector构造函数, 同时支持传入维数和可迭代对象
    这里区分一下iterable, iterator, sequence
    iterator, 至少实现了__iter__和__next__
    iterable, 实现了__iter__或__getitem__(后一种无法用isinstance(v, Iterable)判断)
    sequence, 整数索引, 至少实现__len__, __getitem__
    (特别地, dict 同样支持 getitem() 和 len()，但它不归属于序列类型，它是映射类型，因为它
    不能根据整数下标查找，只能根据 key 来查找)

    这么理解
    iterator是iterable的第一种, 即__iter__, 继承后再实现个__next__
    sequence是iterable的第二种, 即__getitem__, 继承后再实现个__len__

    next()函数是针对iterator, 即__iter__+__next__
    如果不是同时有这俩, 只能称作iterable, 不过可以通过iter(o)转换成iterator
    iter()的参数为iterable, list()的参数也是iterable

"""
from typing import Iterable
class Vector:

    def __init__(self, v):
        if isinstance(v, int):
            self._l = [0] * v
        else:
            try:
                # 这里不用isinstance判断, 因为只实现__getitem__的iterable会认为False
                # 这里实际上是利用list函数支持可迭代对象, 能成则是, 不成抛异常
                self._l = list(v)
            except TypeError:
                raise TypeError

    def __getitem__(self, item):
        return self._l.pop()

v1 = Vector([1, 2, 3])
print(list(v1))

v2 = Vector(8)
print(list(v2))
