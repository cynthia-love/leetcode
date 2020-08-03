# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    迭代器深入
    所谓迭代, 类似于循环, 每一次迭代后的状态会作为下一次迭代的初始状态
"""

# 两个内嵌函数迭代
# 注意这俩函数能生效, 那么对应对象里一定有相应的__iter__函数(__next__不一定, 可能__iter__里直接用了yield)
s = "hello world"
it = iter(s)
try:
    while True:
        print(next(it))
except StopIteration as e:
    print("迭代结束")


class C:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 10:
            self.index += 1
            return "hahaha"
        else:
            raise StopIteration

c = C()
for x in c:
    print(x)
