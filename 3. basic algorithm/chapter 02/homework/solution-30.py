# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给CreditCard类增加_setBalance
"""


from datetime import date
class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def charge(self, price):
        if price+self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def makePayment(self, amount):
        self._balance -= amount

    def getBalance(self):
        return self._balance

    # _开头的成员函数子类访问没任何问题
    # instance访问会提示方法protected
    def _setBalance(self, val):
        self._balance = val

    def _addBalance(self, val):
        self._balance += val

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._month = date.today().strftime("%Y-%m")
        self._count = 0

    # 这里charge其实有点decorator的意味
    def charge(self, price):
        state = super().charge(price)
        if not state:
            self._addBalance(5)
        return state

    def process_month(self):
        if self._balance > 0:
            mpr = (1+self._apr)**(1/12)
            self._balance *= mpr

pc = PredatoryCreditCard("jim", "bocom", "377", 3000, 0.12683)
pc.charge(3001)
print(pc.getBalance())