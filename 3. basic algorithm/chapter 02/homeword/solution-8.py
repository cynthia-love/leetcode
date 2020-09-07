# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    使得CreditCard类可用额度超过信用额度
"""

class CreditCard:
    def __init__(self, limit):
        self._limit = limit
        self._balance = 0

    def charge(self, price):
        if self._balance + price > self._limit:
            return False
        self._balance += price
        return True


cc = CreditCard(3000)
cc.charge(-100)
print(cc.charge(3100))