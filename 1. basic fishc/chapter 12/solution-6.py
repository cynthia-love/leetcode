# -*- coding: utf-8 -*-
# Author: Cynthia
"""
    定制序列
    序列类型: 列表, 元组, 字符串; 映射类型: 字典都称为容器类型
    如果需要容器不可变, 只需要定义__len__和__getitem__
    如果可变, 需要定义__len__, __getitem__, __setitem__, __delitem__

"""

class C:
    def __init__(self, *args):
        self.l = [x for x in args]

    # len(xxx)调用时的行为
    def __len__(self):
        return len(self.l)

    # getitem, setitem, delitem, 以xx[key]的形式调用时的行为
    def __getitem__(self, item):
        return self.l[item]

    def __reversed__(self):
        return reversed(self.l)

    def __contains__(self, item):
        return item in self.l

    # __iter__, 定义迭代时的行为
    # 可以直接在这里写代码, 也可以return self, 然后去实现__next__
    # 推荐直接写, 自己实现next不好实现, 因为迭代每一次是全量调next
    # 所以想要实现下一次调next能达到下一个位置, 必须在外层设置一个next无关的位置变量
    # def __iter__(self):
    #     for i in self.l:
    #         yield i

    # 第二种方法, iter和next配合使, 不建议, 太繁琐
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        # 会发现, 配合使用这种方法, 写起来会非常没法, 还是推荐直接在__iter__里用yield实现
        if self.index <= len(self.l)-1:
            self.index += 1
            return self.l[self.index-1]
        else:
            raise StopIteration

c = C(1, 2, 3, 4, 5)
print(c[2])  # 3
# c[3] = 5, 没定义__setitem__这里会报错
print(5 in c)  # True

for item in c:
    print(item)

for item in c:
    print(item)

print("******************************")
class C:
    def __init__(self, *args, **kwargs):
        print(args, kwargs)  # 注意这俩参数的特殊性, 其会自动去适配普通参数和key-value参数
        # 比如这里args会输出([('a', 1), ('b', 2)],), kwargs会输出{'a': 1, 'b': 2, 'c': 3}
        # 先忽略args, 将kwargs存成字典
        self._d = kwargs

    def __getitem__(self, item):
        # 一般习惯先用in判断在不在
        # 其实有时候用try, except更直接, 记住这种写法
        try:
            return self._d[item]
        except KeyError:
            return -1

    def __setitem__(self, key, value):
        self._d[key] = value

    def __len__(self):
        return len(self._d)

    def __iter__(self):
        for key in self._d:
            yield key

    def __contains__(self, item):
        return item in self._d

c = C([("a", 1), ("b", 2)], a=1, b=2, c=3)
c["d"] = 8
print(c["d"])
print(len(c))
for item in c:
    print(item)

print("e" in c)
print(c["e"])
