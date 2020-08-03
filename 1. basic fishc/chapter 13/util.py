# -*- coding: utf-8 -*-

# Author: Cynthia
"""
    这里是模块帮助信息
    会进到help函数的DESCRIPTION部分
    已经自动赋给模块的__doc__属性
"""
x = 1
def f():
    """
    这里是函数的帮助信息
    """
    print("helloworld_同级目录")

class C:
    """
    这里是类的帮助信息
    """
    m = 100
    @classmethod
    def cm(cls):
        print("cm_同级目录")

    def f(self):
        print("cf_同级目录")

