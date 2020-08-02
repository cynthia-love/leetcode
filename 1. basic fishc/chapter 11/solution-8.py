# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    到底什么是绑定
    类绑定方法(默认传参类自己), 实例绑定方法(默认传参实例自己), 非绑定方法(无默认传参)
"""

class C:
    @classmethod
    def cm(cls):
        print("cm")
    @staticmethod
    def sm():
        print("sm")
    def f(self):
        print("f")
c = C()
c.cm()
c.sm()
c.f()  # 这里好像都可以访问