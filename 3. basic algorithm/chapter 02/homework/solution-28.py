# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改PredatoryCreditCard
    增加功能, 在本月内, 一旦用户完成十次呼叫, 就需要对其收取费用
    每增加一个额外的呼叫, 收取一美元的附加费
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
            self._balance += 5
        return state

    def process_month(self):
        if self._balance > 0:
            mpr = (1+self._apr)**(1/12)
            self._balance *= mpr

    def process_tel(self):
        month = date.today().strftime("%Y-%m")
        if month == self._month:
            self._count += 1
            if self._count > 10:
                self._balance += 1
        else:
            self._month = month
            self._count = 0

    def get_balance(self):
        return self._balance

pc = PredatoryCreditCard("aaa", "bbb", "111", 1000, 0.12)
for _ in range(15):pc.process_tel()
print(pc.get_balance())
