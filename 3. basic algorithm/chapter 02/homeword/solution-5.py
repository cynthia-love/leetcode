# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    控制参数大小
"""
def make_payment(price):
    if price < 0:
        raise ValueError("price {} lower than zero".format(price))
    else:
        pass

make_payment(9)
make_payment(-9)