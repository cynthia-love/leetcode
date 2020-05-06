# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    组合, 比如水池里有鱼和乌龟
    其实没啥特别的, 无非是把类当成了自定义数据类型, 和list, dict啥的没区别
"""

class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, y):
        self.num = y

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
        self.length = list()  # 这里Turtle, Fish和list都只是一种类型而已

    def status(self):
        print("水池里有{}只乌龟, {}只鱼".format(self.turtle.num, self.fish.num))

p = Pool(10, 100)
p.status()
