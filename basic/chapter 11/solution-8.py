# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    到底什么是绑定
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