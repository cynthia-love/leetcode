# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对于Range类, 仅提供__len__和__getitem__
    对比2 in Range(10000000) 和 9999999 in Range(10000000)的速度
    然后自己实现__contains__, 要求时间复杂度独立于规模
"""

class Range:
    # step置为1
    def __init__(self, stop):
        self.start = 0
        self.stop = stop

    def __len__(self):
        return self.stop-self.start

    def __getitem__(self, index):
        return self.start + 1*index

r = Range(10000000)

import timeit
s1 = timeit.timeit(stmt=lambda : 2 in r, number=1)
s2 = timeit.timeit(stmt=lambda : 9999999 in r, number=1)
print(s1, s2)  # 5.46600000000258e-06 1.859317502

# iterator的x in r, 会从头开始一个个去找, 导致2和9999999的存在判断时间复杂度差距很大

class Range:
    # 为简单起见, step置为+1
    def __init__(self, stop):
        self.start = 0
        self.stop = stop

    def __len__(self):
        return self.stop-self.start

    def __getitem__(self, index):
        return self.start + 1*index

    def __contains__(self, item):
        # step为1最简单, 第一个条件就行
        # 为其它正数, 要加上后面那个条件, 即在分界点上
        return self.start <= item < self.stop and (item-self.start) % 1 == 0

rr = Range(10000000)

import timeit
s1 = timeit.timeit(stmt=lambda : 2 in rr, number=1)
s2 = timeit.timeit(stmt=lambda : 9999999 in rr, number=1)
print(s1, s2)  # 3.069999999993911e-06 1.683000000030077e-06