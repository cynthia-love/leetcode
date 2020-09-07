# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在solution-12的基础上, 再实现3*v
"""

# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现Vector类的__mul__方法, v*3返回三倍
"""

class Vector:
    def __init__(self, l):
        self._l = l

    def __mul__(self, other):

        l = [x*other for x in self._l]
        return Vector(l)

    def __rmul__(self, other):
        l = [other*x for x in self._l]
        return Vector(l)

    def __iter__(self):
        for each in self._l:
            yield each


v = Vector([1, 2, 3])
v2 = v*3
v3 = 8*v
print(list(v2), list(v3))