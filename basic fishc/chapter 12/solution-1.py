# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    魔法方法, __xx__这种形式, 自动在适当时候被调用的方法
"""

"""
    构造和析构
"""

# __init__, 类实例化时调用的方法

class C:
    def __init__(self, x):
        print("实例被构造!!!")
        self.x = x
    def __del__(self):
        print("实例被删除")
c = C(100)
c1, c2 = c, c
del c1
del c2  # 这两个地方并不会直接去调析构函数

# 注意del关键字和这里的__del__两码事
# del关键字只是删除, 而这里的__del__是垃圾回收机制回收的时候才调


# 补充, 其实类实例化的时候调的第一个魔法方法不是ini, 而是new
"""
__new__是在实例创建之前被调用的，它的任务就是创建实例然后返回该实例对象，是个类方法。
__init__是当实例对象创建完成后初始化用的，然后设置对象属性的一些初始值，是一个实例方法。
只有在__new__返回一个cls的实例时，后面的__init__才能被调用
"""
class C:
    def __new__(cls, *args, **kwargs):
        print(args, kwargs)  # (1, 2, 3) {'x': 1, 'y': 2}
        return super().__new__(cls)
    def __init__(self, a, b, c, x, y):
        print(a, b, c, x, y)

    def f(self):
        print("hhaha")

c = C(1, 2, 3, x=1, y=2)
c.f()
