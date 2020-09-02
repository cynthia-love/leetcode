# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    重载示例: 迭代器

    只是为了演示, 建议采用更先进的generator
"""

class Iterator:
    def __init__(self, sequence):
        self.l = sequence
        self.k = -1  # 注意这里是-1

    def __next__(self):
        self.k += 1
        if self.k >= len(self.l):
            raise StopIteration()
        return self.l[self.k]

    def __iter__(self):
        return self

l = [1, 2, 3, 8]
it = Iterator(l)
for each in it:
    print(each)


# 自己实现一个range, 注意要实现其惰性求值
# 先试一下几种实现iter的方法
# 注意前两种可以for遍历, 但不支持数字下标直接访问

# 方式1, 只实现__iter__, 结合yield, 最简单
class A:
    def __init__(self):
        self.l = [8, 7, 2, 1]

    def __iter__(self):
        for each in self.l:
            yield each

a = A()
for each in a:
    print(each, end=", ")

# 方式2, 实现__next__和__iter__
class B:
    def __init__(self):
        self.l = [1, 2, 7, 8]
        self.k = -1

    # next是每次重新调, 不会从其上次状态继续执行
    # 所以这里不能用yield
    def __next__(self):
        self.k += 1
        if self.k < len(self.l):
            return self.l[self.k]
        else:
            raise StopIteration

    def __iter__(self):
        return self

b = B()
for each in b:
    print(each, end=", ")

# 方式3, 实现__len__和__getitem__
class C:
    def __init__(self):
        self.l = [100, 200, 300, 400]

    def __len__(self):
        return len(self.l)

    def __getitem__(self, item):
        return self.l[item]

c = C()
for each in c:
    print(each, end=", ")

# 那么, 实现range就有这么几种思路了
# 思路1, __iter__配合yield

class D:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield i

d = D(5)
for each in d:
    print(each)

# 思路2, __iter__配合__next__, 演示更复杂的range
class E:
    """A class that mimic's the built-in range class"""
    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance
        Semantics is similar to built-in range class
        """
        if stop:
            self.start = start
            self.stop = stop
            self.step = step
        else:
            self.start = 0
            self.stop = start
            self.step = step

        self.k = self.start-self.step

    def __next__(self):

        self.k += self.step

        if self.k < self.stop:
            return self.k
        raise  StopIteration

    def __iter__(self):
        return self

e = E(100, 200, 20)
for each in e:
    print(each)

# 思路三, __len__配合__getitem__
# 这种方式实际上是变成了sequence, 所以同时支持iter遍历和数字下标访问
class F:
    """A class that mimic's the built-in range class"""
    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance
        Semantics is similar to built-in range class
        """
        if step == 0: raise ValueError("step cannot be 0")
        self.start, self.stop = (start, stop) if stop else (0, start)

        self.step = step

    def __len__(self):
        # calculate the effective length
        # 比如2, 10, 3, 有效数字: 2 5 8; 2, 12, 3, 有效数字: 2 5 8 11
        # 开头start, 结尾stop-1,
        return (self.stop-1-self.start) // self.step + 1

    def __getitem__(self, item):
        if item < 0:
            item = len(self)+item

        if item > len(self)-1:
            raise IndexError("index out of range")

        return self.start + item * self.step

f = F(2, 10, 3)
print(f[0], f[1], f[2])
for each in f:
    print(each)
print(list(f))
print(list(range(2, 10, 3)))