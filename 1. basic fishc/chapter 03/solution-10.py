# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    常用运算符
"""

# 算数操作符
a, b = 1, 2
c = d = 3
a += 1
b = b-1
c *= 2
d /= 2
print(a, b, c, d)

print(3 // 2, 3 % 2)  # 商 1, 余 1
print(3.0 // 2, 3.0 % 2)  # 商 1.0, 余 1.0, 即运算自动往细了做类型转换
print(-3 // 2, -3 % 2)  # 商 -2, 余 1, //取比实际商小的最大整数

# 注意一个特殊的**, 比左侧一元操作符优先级高, 比右侧一元操作符优先级低
print(-3**2)  # -9
print(-3**-2)  # -0.1111111111111111


# 比较操作符
print(1 < 2, 1 > 2, 1 <= 2, 1 >= 2, 1 == 2, 1 != 2)

# 逻辑运算符
print(True and False)
print(True or False)
print(not False)
print(3 < 4 < 5)  # python里允许这么写, 表示3 < 4 and 4 < 5

# 注意python里没有&&, ||, 请用and和or

# 按位运算符
print(3 & 2)
print(3 | 2)
print(3 ^ 2)
print(2 << 1)
print(2 >> 1)


