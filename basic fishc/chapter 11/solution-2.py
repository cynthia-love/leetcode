# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    面向对象编程入门
"""

class Ball:
    # self为实例自身的引用
    # 一个类可以生成无数个对象, 当一个对象的方法被调用的时候, 对象会将自身的引用作为第一个参数传给该方法
    def __init__(self, age=90):
        self.size = 0
        self.age = age
    # 这种带下划线的方法, 也称为类的魔法方法, 这类方法会在特定情况下被python自动调用, 注意是自动
    # 比如init就是实例化对象的时候调用

    def setName(self, name):
        self.name = name
        # 实例变量不要求一定在init声明, 但不建议这么干
        # 还是建议在init里初始化一下

    def setSize(self, size):
        self.size = size

    def printInfo(self):
        print(self.name , self.size)

b1 = Ball()
b1.setName("b1")
b1.printInfo()
b2 = Ball()
b2.setName("b2")
b2.setSize(100)
b2.printInfo()


# 私有变量, 无法在外部直接访问
class Ball2:
    __name = "private variable"

    def __init__(self):
        self.__age = 10

    def printInfo(self):
        print(Ball2.__name, self.__age)

b = Ball2()
b.printInfo()
# print(Ball2.__name)
# print(b.__age), 这两行都不能执行的, 要访问只能内部访问

