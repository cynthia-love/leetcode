# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    lambda表达式, 一种精简的函数书写方式
    结合filter和map用, 强的一匹
"""

l = lambda x, y, z: x+y+z  # 冒号隔开, 左边参数, 右边返回值
print(l(1, 2, 3))

# lambda在filter中的应用
# filter有俩参数, 第一个是过滤条件, 第二个是列表
# 如果过滤条件不指定, 则默认过滤值为True的
x = [1, 2, 3, -1, -2, 0, 0, 8]
x_f = list(filter(None, x))  # 就把俩0过滤掉了
print(x_f)
# 也可以显式指定过滤条件
x_f = list(filter(lambda x: x > 0, x))
print(x_f)  # [1, 2, 3, 8]

# lambda在map中的应用; filter是过滤掉某些元素, 而map则是按照一定规则批量映射
x_m = list(map(lambda i: i**2, x))
print(x_m)
