# -*- coding: utf-8 -*-
# Author: Cyntia

"""
    闲聊数据类型
"""

# 整型, python3 整型长度不受限制
print(1111111111111111111111111111111111111111111111111111111111111111111111)

# 浮点型, 2.5e-54
print(0.0000000000000000000000000000000000000000000000000000025)

# 布尔类型True/False, 可以与整型一起运算, 相当于1/0
print(True+True)
print(bool(8))  # True
print(bool(-7))  # True, 只要不是0, 负数也是True
print(bool(1.2))  # True

# int可以把str和float转换成整数类型
print(int("123"))
print(int(1.23))  # 1, 直接舍弃小数点后的内容, 而不是四舍五入

# float可以把str和int转换成浮点类型
print(float("3.12"))  # 3.12
print(float(18))  # 18.0

# str可以将任何类型转换成字符串
print(str(128))
print(str(5.99))
print(str(2e2))  # 200.0


# 类型判断, 两种方法
print(type(100))  # <class 'int'>
print(type(100) == int)  # True
print(isinstance(100, int))  # True
print(isinstance(True, int)) # 注意这里会输出True, 说明bool就是一种特殊的int
