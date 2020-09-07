# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    控制成员函数参数类型

"""

class CreditCard:
    def charge(self, val):
        if isinstance(val, (int, float)):
            print(val)
        else:
            raise ValueError


cc = CreditCard()
cc.charge(100)
cc.charge(1.1)
cc.charge("hello")