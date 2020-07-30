# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    集合, 字典的表亲, 相当于只有key没有value的字典, 也是无序的
    集合的元素不可重复, 且集合会自动去重
"""
# 集合初始化
# 注意空集合初始化只能用set(), 不能用{}
s = set()
print(s)

s1 = {1, 2, 3, 4, 1, 2}
print(s1)  # {1, 2, 3, 4}

s2 = set([1, 2, 3, 4, 5, 2])   # 也可以用可迭代对象初始化, 但一般不这么干
print(s2)

# 利用set的不重复特性, 对list去重, 这种方法非常常见
l = [1, 2, 3, 4, 5, 2, 1]
print(list(set(l)))   # 这里要注意, set是无需的, 经这么一转, 最终结果list里元素的顺序可能会变

# list用append, insert, extend插入, remove, pop去除
# set用add插入, remove去除
s3 = {1, 2, 3, 4, 5}
s3.add(8)
print(s3)
s3.remove(2)
print(s3)

# list有对应的不可变形式tuple, set也有, 用frozenset
s4 = frozenset([1, 2, 3, 1])  # frozenset({1, 2, 3})
print(s4)
s4.add(100)  # AttributeError: 'frozenset' object has no attribute 'add'



