# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对象, 即类的实例
    python里类是所有数据类型的基础, 比如int, float, str都是类
"""

x1 = 1.6
y1 = float(1.6)  # 这两行代码是等价的, x/y为标识符, 右边是float类的实例对象

x2 = y2 = 1.1
x2 += 1.0  # x2引用新的float类实例, y1继续指向原来的float类实例

x3 = y3 = []
x3.append(1)  # 区别上面的例子, 这里是直接改底层对象, 而不是改别名的指向, 所以y3也会跟着变

"""内置类"""
# 分为不可变类bool, int, float, tuple, str, frozenset
# 可变类list, set, dict
# 内置类一般支持两种构造形式, 字面形式和函数形式, 1.1是字面, float(1.1)是函数

# bool
print(True, bool(), bool(True), bool(0), bool([]))
# bool()返回False, 数字0为False, 序列和容器空为False

# int
print(1, 0b1011, 0x7F, int(), int(1.1), int('888'), int("7F", 16))
# 1, 11, 127, 0, 1, 888, 127; 参数为小数时直接截断; int首参数为字符串时, 支持第二个参数指定进制

# float
print(1.1, 1., 3.8e3, float(), float(1), float("3.2"))
# 1.1, 1.0, 3800.0, 0.0, 1.0, 3.2

# 序列类型list, tuple, str
# list
x4 = 8
print([], list(), list([1, 2, 3]), [100], [x4], list("hello"))
# [], [], [1, 2, 3], [100], [8], ['h', 'e', 'l', 'l', 'o']
# tuple
print((), tuple(), (1, 2), (1,))
# (), (), (1, 2), (1, )
# str
print('hahah', 'a\\b', '\u20AC', """adfd afdkj""")

# set和frozenset
# 元素唯一, 无序, 且必须为不可变类型(tuple和frozenset都可以)
print(set(), {1, 2, 3}, {(1, 2), frozenset([8, 8])}, set("hello"))
# set(), {1, 2, 3}, {(1, 2), frozenset({8})}, {'h', 'l', 'o', 'e'}

# dict, 与set类的性质几乎相同
print({}, dict(), {1:3, 'a':8}, dict([('a', 1), ('b', 8)]), dict(x=1, y=3))
# {}, {}, {1:3, 'a':8}, {'a':1, 'b':8}, {'x':1, 'y':3}
