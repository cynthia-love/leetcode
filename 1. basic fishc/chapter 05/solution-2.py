# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    元组tuple
    元祖和list最大的区别是内容不可改变, 相当于有了const声明
"""

a = (1, 2, 3, 4, 5)
print(a)
print(a[0])
print(a[1:3])
print(a[::-1])
print(a[1:5:2])

b = ()
c = (1,)  # 单个元素初始化, 这里的逗号是必须的
d = tuple()
e = 3, 2  # !!!, 其实tuple的标志不是(), 而是逗号 ,
print(b, c, c*3, d, e)

# 元组元素不可修改, 所以添加和删除得采用切片复制的方法
# 要么可能预见到修改, 就不要设置为tuple类型
# 这里注意, python原生的list tuple str用+号等效于拼接, 而不像一些数学库里是对应位置元素相加
d = a[:2]+(100,)+a[2:]
print(d)
e = a[:2]+a[3:]
print(e)

