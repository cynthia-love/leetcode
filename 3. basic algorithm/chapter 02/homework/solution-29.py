# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改PredatoryCreditCard, 增加参数最低付款额, 如果客户在下一个月周期之前没有连续地支付最低金额,
    则要评估延迟的费用
    基本思路: 增加字段, 最低还款额和是否已还最低
    1. 消费, 没还, flag为False, 月底有欠款, 正常计息, 且收取额外费用
    2. 消费, 还了, flag置为True, 月底有欠款, 正常计息, 不收取额外费用
    3. 没欠款, 那月底也得清空flag标志
    4. flag初始置为True, 以处理首月特殊情况, 月底不收取额外费用
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

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr, min):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._month = date.today().strftime("%Y-%m")
        self._min = min
        self._flag = True

    # 这里charge其实有点decorator的意味
    def charge(self, price):
        state = super().charge(price)
        if not state:
            self._balance += 5
        return state

    def makePayment(self, amount):
        super().makePayment(amount)
        if amount >= self._min:
            self._flag = True

    def process_month(self):
        if self._balance > 0:
            mpr = (1+self._apr)**(1/12)
            self._balance *= mpr

            if not self._flag:
                self._balance += 5

        self._flag = False


pr = PredatoryCreditCard("aaa", "aaa", "aaa", 3000, 0.12683, 30)
pr.charge(800)
pr.charge(200)
print(pr.getBalance())
pr.process_month()
print(pr.getBalance())
pr.process_month()
print(pr.getBalance())
pr.makePayment(30)
pr.process_month()
print(pr.getBalance())