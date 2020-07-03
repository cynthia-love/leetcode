# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第5章 列表list、元组tuple、集合set和字符串
"""

"""
    列表list
"""

# 初始化
a = list()
print(a)

b = []
print(b)

c = [1, 2, 3]
print(c)

# python的list不要求所有元素同一类型
d = [1, 2, "a", [1, 2]]
print(d)

# 插入元素
e = [1, 2, 3, 4]
e.append(5)
print(e)
e.extend([8, 9])
print(e)
e.insert(0, 100)
print(e)

# 获取元素
f = ['a', 'b', 'c']
print(f[2])
f[1], f[2] = f[2], f[1]
print(f)

# 删除元素
# remove, 根据值删除, 只会删除最左边的第一个; 找不到则报错
g = ["a", "a", "b"]
g.remove("a")
print(g)
# del, 指定位置删除
h = ['a', 'a', 'b']
del h[2]
print(h)
# pop, 指定位置删除, 且返回值
r = ['a', 'b', 'c']
r.pop()  # 不指定位置, 删除最右
print(r)
r.pop(0)
print(r)  # 指定索引, 删除指定位置


# 列表索引, 单索引和切片; 注意切片得到的列表是原列表的一个拷贝
s = ['a', 'b', 'c', 'd', 'e', 'f']
print(s[1])
print(s[1:3])
print(s[:2])
print(s[2:])
# 切片还可以加第三个参数, 步长
print(s[2:7:2])  # 2 3 4 5 6, 6大于了5, 取小的, 2 3 4 5, 步长2, 2 4, 所以输出c e
print(s[::-2])  # 步长甚至可以是负数, 表示倒着来
print(s[7:1:-2])  # 步长为负时, 且有参数1和2, 那么参数1得比参数2大

# 列表操作符
x = [1, 2, 5]
y = [1, 2, 3, 8]
print(x > y)  # 比较运算符可以直接用于列表, 逻辑类似字符串比较, 从前往后一个个比, 谁先遇到相对大的谁就大
z = x+y  # 等价于extend, 和numpy里的对应位置相加区别开来
print(z)
print(z*2)  # 重复两次, 和numpy里的元素乘以2区别开来
z *= 3
print(z)
print(5 in x)
print(5 not in x)
k = [1, 2, [3, 4], 5]
print([3, 4] in k)  # True, list认为是基本数据类型, 直接比
print(k[2][0])

# 其他方法
print(dir(list))
l = [1, 2, 3, 4, 3, 5]
print(l.count(3))
print(l.index(3))  # 找第一个
print(l.index(3, 3, 6))  # index可以指定查找范围
l.reverse()
print(l)
l.sort(key=lambda x: x, reverse=False)
print(l)

# reverse和sort有俩对应的不改变自身的函数
# reversed比较特殊, 返回的是个迭代器
print(list(reversed(l)))  # 得强制类型转换
print(sorted(l, reverse=False))