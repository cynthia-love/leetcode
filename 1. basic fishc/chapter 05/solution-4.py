# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    序列list, tuple, str统称为序列; list可变, tuple str不可变
"""

# list把一个可迭代对象转换为列表
a = list()
b = list("like")
c = list((1, 2, 3, 4, 5))
print(a, b, c)

# tuple把一个可迭代对象转换为元组
a = tuple()
b = tuple("like")
c = tuple([1, 2, 3, 4, 5])
print(a, b, c)

# str把一个对象转换为字符串
# 对象会自己定义str(obj)的行为
a = str()  # ""
b = str([1, 2, 3])  # [1, 2, 3]
print(a, b)
print(str(1), str(1.222))

# len返回列表的长度
print(len([1, 2, 3]))
print(len((1, 2, 3)))
print(len("abc"))

# max/max
print(max([1, 2, 3, -1, -2]))
print(max("I like adjfk v zk dfad"))  # z
print(max(1, 3, 8, 9))  # 即max的输入可以是个序列, 也可以是多个参数
# 注意, python里不存在char概念, 不能字符和数字直接比较
# print(max(1, "a")), 这里会报错

# sum, 序列元素必须是数字
print(sum([1, 2, 3, 4, 5]))

# sorted, 排序, 输出结果类型恒定list
a = [1, 8, 9, 2]
b = sorted(a, key=lambda x: x+1, reverse=True)
print(b)
print(sorted("aexxfeab"))  # 即使输入是str, 排序结果也会变成list

# reversed, 输出结果类型恒定迭代器iterator
a = [1, 8, 9, 2]
b = reversed(a)
print(list(b))  # 迭代器是可迭代对象, 所以可以直接强转成list

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 最关键的, enumerate, 将一个可迭代对象转换成一个二元组可迭代对象, 索引+元素
# 类似于dict里的.items()
a = ["a", "b", 8]
b = "like"
print(list(enumerate(a)))  # [(0, 'a'), (1, 'b'), (2, 8)]
print(list(enumerate(b)))  # [(0, 'l'), (1, 'i'), (2, 'k'), (3, 'e')]
# 也可以用for遍历
for s in enumerate(a):
    print(s[0], s[1])


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# 最关键的, zip, 同索引压到一起, 可以理解为一个矩阵, 行优先转为列优先
a = [1, 2, 3, 4, 5]
b = "hello"
c = (8, 100, 2)
"""
    1   2   3   4   5
    h   e   l   l   o
    8   100 2
    结果是[(1, 'h', 8), (2, 'e', 100)]   (长度取最短的那个)
"""
print(list(zip(a, b, c)))  # 输出可迭代对象, 可用list强转
for x in zip(a, b, c):
    print(x)
