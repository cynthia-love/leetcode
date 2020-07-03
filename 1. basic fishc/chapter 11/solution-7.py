# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    类, 类对象和实例对象
"""
class C:
    x = 0

a, b, c = C(), C(), C()

print(C.x, a.x, b.x, c.x)  # 只是访问类变量, 都一样
C.x += 1
print(C.x, a.x, b.x, c.x)  # 通过类名去改类变量, 一改都改
a.x = a.x+1
print(C.x, a.x, b.x, c.x)  # 不要被右侧的a.x迷惑了, 简单看这里就是声明了实例变量, 覆盖, 原类变量还继续存在
