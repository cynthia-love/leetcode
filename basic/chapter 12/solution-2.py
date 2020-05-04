# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    算数运算
    自定义对象间的算数运算
"""

x = 1
print(type(x))  # <class 'int'>, 注意这里的class, 在python里, 基本数据类型也变成类了
print(x.__add__(100))  # 等价于x+100

y = [1, 2, 3]
print(type(y))  # <class 'list'>

class C:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):  # 这里的other是没有类型规定的, 不要求必须是C类型
        if isinstance(other, int):
            return 'int'
        if isinstance(other, list):
            return other
        return -1

    def __sub__(self, other):
        return int.__sub__(self.x, other.x)  # 这么调也是可以的

    def __mul__(self, other):
        return "乘法"

    def __truediv__(self, other):
        return "真除法/"

    def __floordiv__(self, other):
        return "//"

    def __mod__(self, other):
        return "%"

    def __lshift__(self, other):
        return "<<"

    def __rshift__(self, other):
        return ">>"

    def __and__(self, other):
        return "&"

    def __or__(self, other):
        return "|"

    def __xor__(self, other):
        return "^"

    # 上述所有算数都存在对应的反运算, 左边再加个r就是
    def __radd__(self, other):
        return other

c1 = C(100)
c2 = C(200)
print(c1+c2, c1-c2, c1+[1, 2, 3], c1 | 888)  # -1, [1, 2, 3]

print(1+c1)  # 如果前对象的__add__方法没有实现或不支持相应的操作, 那么就调用后对象的__radd__方法
# 注意这里输出1, 说明虽然调用后对象的radd, 但是还是把非自身作为other的


# 一元操作符
class C2:
    def __pos__(self):
        return "pos"

    def __neg__(self):
        return "neg"

    def __abs__(self):
        return "abs"

c2 = C2()
print(+c2, -c2, abs(c2))  # pos, neg, abs



