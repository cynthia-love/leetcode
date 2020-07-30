# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第7章 字典和集合
"""

"""
    字典, 当数字索引不好用时
    (平时说的哈希, 关系数组其实就是字典)
    字典是python中唯一的映射类型(不像java里一堆hashMap, hashTable什么的)
"""

# 字典初始化
d1 = {}  # 字典把{}占了那set初始化就不能这么写了
print(type(d1))  # 字典和set的标志都是{}, 直接用{}声明的空是字典而不是set; <class 'dict'>
d2 = {"a": 1, "b": "hahah", (1, 2): "3"}
print(d2)  # 字典没有顺序, 字典的键必须是不可变类型, 比如可以是tuple不能是list
# 可以是tuple这种复杂类型, 这一点记好, 关键时候有用

# 其他初始化方式
# 传入可迭代对象
l = [("A", 2), ("B", 3)]
d3 = dict(l)
print(d3)
# 传入具有映射关系的参数
d4 = dict(A=2, B=3)  # 函数**参数就是这么传的, 不过不能f([(),()])这么传
print(d4)

# 总结
d5 = {"a": 1, "b": 2}
d6 = dict(a=1, b=2)
d7 = dict([("a", 1), ("b", 2)])
print(d5 == d6 == d7)

# dict的各种内置方法
# 快速创建同一个value的多个key的dict
d8 = dict.fromkeys(["a", "b", "c"], 8)  # 如果第二个参数不指定, 则value都为None
print(d8)

# 遍历方法, 返回可迭代对象
d9 = {"a": 8, "b": 12, "c": 1}
print(d9.keys())
print(d9.values())
print(d9.items())

# 判断一个键是否存在
d10 = {"a": 8, "b": 12, "c":1}
print(d10.get("e"))  # 不存在, 取到的值为None
print(d10.get("e", 88888))  # 不存在, 取到的值指定值, 这不就是defaultdict吗
print("e" in d10)  # 不存在, 输出False

# 清空字典
d11 = {"a": 8, "b": 10}
d11.clear()
print(d11)

# 复制字典
d12 = {"a": 8, "b": 10}
d13 = d12.copy()  # 后面还有一种深度拷贝方法, copy.deepcopy(xxx)
print(d13, id(d12), id(d13))

# pop
d14 = {"a": 8, "b": 10}
d14.pop("b")  # 根据键值pop, 找不到则抛异常
print(d14)
d15 = {"a": 8, "b": 10}
d15.popitem()  # 抛出字典顺序的最后一个???
print(d15)

# update
d16 = {"a": 8, "b": 10}
d16.update(b=100)
print(d16)
d16['b'] = 1000   # 可以直接这么赋值, 没必要用update
print(d16)

# 字典传参的打包解包, 元组是*, 字典是**
# 不要这么记, 永远把**理解成解包就行, 作为函数参数表示解包后是a=1, b=2, c=3
# 形参加**, 表示把后面传入的参数打包成字典
def f(**params):
    print(params)  # {'a': 1, 'b': 2, 'c': 3}

f(a=1, b=2, c=3)
# 实参加**, 表示把传入的字典解包
f(**{"a": 1, "b": 2, "c": 3})



