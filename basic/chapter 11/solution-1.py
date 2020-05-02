# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第11章 类和对象
"""

"""
    对象 = 属性+方法
    对一类对象进行抽象, 即得到类Class(模具), 每一个具体的对象称为实例Instance
"""

# Python里类以大写字母开头, 函数以小写字母开头
class Turtle:
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = "大嘴"
    # 在init外声明的为类成员变量, 通过类名访问

    def __init__(self):
        self.color = "yellow"
        self.haha = "haha"
        # 在init里以self声明的为实例变量, 通过self或者实例名访问
        print(self.weight, Turtle.weight)
        # 这里发现用self也能访问到类变量
        # 其实这个机制有点像是内嵌函数
        # 如果self.类变量只是访问是可以访问到的
        # 但是如果尝试修改, 那么就会出现一个同名实例变量, self.color和Turtle.color同时存在
        # 为了简化逻辑处理, 建议类变量一律用类名访问, 不要用self访问; 且不要取同名变量
        # 除了个别常量, 尽量不要声明类成员变量, 都放init里用self声明
    def climb(self):
        # 这里self
        print("我正在爬")
    def sleep(self):
        print("我正在睡")


t = Turtle()
print(Turtle.color)
print(t.color)
print(Turtle.color)
t.climb()

# 重新规划一下
class Turtle:
    leg = 4  # 所有王八都是四条腿, 实例不会去改它, 可以声明为类变量
    shell = True

    def __init__(self, color, weight):
        # 实例变量一般都在init里声明, 当然也可以在其他函数里
        # 建议在init里初始化, 即使其他函数也可以声明
        self.color = color
        self.weight = weight

    def printInfo(self):
        print(Turtle.leg, Turtle.shell, self.color, self.weight)

t = Turtle("yellow", 100)
t.printInfo()