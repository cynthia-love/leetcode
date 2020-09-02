# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    继承

    注意python里异常类的层次结构
    BaseException
        SystemExit
        KeyboardInterrupt
        Exception
            ValueError
            ArithmeticError
                ZeroDivisionError
            LookupError
                IndexError
                KeyError

"""
class BaseException:
    def f(self):
        print("base exception")

class SystemExit(BaseException):
    # 父类中有f, 这里再重写f, 称为override
    def f(self):
        print("system exit")

    # 父类没有, 子类自己加的方法, 称为extend
    def f1(self):
        print("第一级子类的扩展方法")

class Exception(BaseException):
    def f(self):
        print("normal exception")

class KeyboardInterrupt(BaseException):
    def f(self):
        print("keyboard interrupt")


o1 = BaseException()
o2 = Exception()
print(o1 == o2, o1 is o2, isinstance(o1, BaseException))
print(issubclass(Exception, BaseException), isinstance(o2, BaseException))  # True, True


# 下面演示另外一个例子
# 给CreditCard增加每月对欠款收取利息的机制, 且当charge失败时, 扣5块钱的费用


class CreditCard:
    """A consumer credit card"""
    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance

        The initial balance is zero

        :param customer: the name of consumer
        :param bank: the name of the bank
        :param account: the account identifier
        :param limit: credit limit
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return the bank's name"""
        return self._bank

    def get_account(self):
        """Return the card identifying number"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed; False if charge was denied
        """
        # balance存的是已经消费了多少钱, 而非余额
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price

    def revoke(self, price):
        """Process customer payment that reduces balance"""
        self._balance -= price

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""
    def __init__(self, customer, bank, account, limit, apr):
        """
        Create a new predatory credit card instance

        :param customer: the name of the customer (e.g., 'Jim')
        :param bank: the name of the bank (e.g., 'BOCOM')
        :param account: the account identifier
        :param limit: credit limit (measured in dollars)
        :param apr: annual percentage rate
        """
        super().__init__(customer, bank, account, limit)

        self._apr = apr

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit
        If charge is denied, assess $5 fee

        :param price:
        :return: True if charge was processed, False if charge is denied
        """
        # 即使覆盖了, 也可以通过super()调用父类种的同名实例函数
        if super().charge(price):
            return True
        else:
            self._balance += 5  # 这里父类没提供set_balance, 而charge又限制额度, 而费用可以超额度, 所以直接访问_balance
            return False

    def process_month(self):
        """
        Assess monthly interest on outstanding balance
        :return:
        """
        # convert APR to monthly multiplicative factor
        mpr = (1+self._apr)**(1/12)-1
        print(mpr)
        if self.get_balance() > 0:
            # 这里父类没提供set_balance, 而charge又限制不能超过信用额度, 所以只能直接改_balance
            self._balance *= (1+mpr)


# 再演示一个例子, 数列, 数字的序列, 每个数字都依赖于一个或更多前面的数字
# 抽象等差数列, 等比数列, 斐波那契额数列得到数列基类

