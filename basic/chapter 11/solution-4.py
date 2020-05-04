# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    多重继承
    不建议用, 容易出现代码混乱
    尤其继承层级超过2层时, 什么经典类新式类, 深度优先广度优先什么的, 还是不要去记了
    建议参照solution-6, 尽量用Mixin, 给基类添加特性组件, 而不是继承一堆类
"""

class Base1:
    @classmethod
    def cf(cls):
        print("cf1")
    def f(self):
        print("base1f")
    def f1(self):
        print("base1")

class Base2:
    @classmethod
    def cf(cls):
        print("cf2")
    def f(self):
        print("base2f")
    def f2(self):
        print("base2")

class Child1(Base1, Base2):
    def f3(self):
        print("child")

c = Child1()
c.f1()
c.f2()
c.f3()  # 这里是实例函数, self/实例名可以访问全部实例函数
c.f()  # 这里会输出base1f, 即子类里没有, 会从左往右找父类
c.cf()  # 这里也会输出cf1