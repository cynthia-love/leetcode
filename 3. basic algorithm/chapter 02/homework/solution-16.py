# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Range类里len计算
    max(0, (stop-start+step-1)//step)
    证明为什么这个式子正确
"""

"""
    分析:
    (stop-start+step-1)//step
    这个式子真的对吗, 比如: 1.1, 1.5, 0.1, step为小数的时候明显算的不对啊
    
    自己写一个试试
    1. 终点恰好是分界点
    (stop-start) / step
    2. 终点不是分界点
    (stop-start) // step + 1
    
    尝试统一:
    1. (stop-start - 0.1*step) // step
    2. (stop-start + 1.0*step) // step
    
    不行, 还是if吧
    
    if (stop-start) % step == 0:
        pass
    else:
        pass
    

"""
import math
class Range:
    def __init__(self, start, stop, step):
        self._start = start
        self._stop = stop
        self._step = step

    def __len__(self):
        # 小数的求余不能用%
        if math.fmod(self._stop-self._start, self._step) == 0:
            return int(max(0, (self._stop-self._start) // self._step))
        else:
            return int(max(0, (self._stop-self._start) // self._step + 1))

    def __getitem__(self, index):
        # 这里需要显式地控制index范围, 否则不会自动抛错
        if index >= len(self):
            raise IndexError("index out of range")
        return self._start+index*self._step


r = Range(0, 10, 0.1)
print(len(r))
print(r[0], r[1], r[99])
r = Range(0, 10, 2)
print(len(r))
r = Range(0, 10, 3)
print(len(r))
r = Range(1.1, 1.5, 0.2)
print(len(r))
print(r[2])