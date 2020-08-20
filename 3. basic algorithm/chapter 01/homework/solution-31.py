# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    找零钱(最多到角)
    输入给的钱和需要支付的钱, 返回找零情况
    按现有货币面值: 100 50 20 10 1 0.5 0.2 0.1

    典型贪心算法

    比如给了200, 价钱168, 要找零32

"""

def f(pay, price):

    face = [100, 50, 20, 10, 1, 0.5, 0.2, 0.1]

    remain = pay - price

    res = {}

    for each in face:
        res[each] = remain // each
        remain = remain % each

    return res

print(f(200, 168))
print(f(200, 168.2))