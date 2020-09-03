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
class Progression:
    """Iterator producing a generic progression
    Default iterator produces the whole number 1, 2, 3
    """

    def __init__(self, start=0):

        """Initialize current to the first value of the progression"""
        self._current = start

    def _advance(self):
        """
        Update self._current to a new value
        This should be overridden by a subclass to customize progression
        By convention, if current is set to None, this designates the end of a finite progression
        :return:
        """
        self._current += 1

    def __iter__(self):
        while self._current is not None:
            yield self._current
            self._advance()

        raise StopIteration
    # 注意, 如果直接在__iter__里用yield返回值, 而不写__next__函数
    # 那么其instance就不能直接用next()函数, 得写一步it = iter(p)之后才能调用next
p = iter(Progression(0))
print([next(p) for _ in range(5)])

class ArithmeticProgression(Progression):
    def __init__(self, start=0, increment=1):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

p = iter(ArithmeticProgression(1, 3))
print([next(p) for _ in range(5)])

class GeometricProgression(Progression):
    def __init__(self, start=1, base=2):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

p = iter(GeometricProgression(2, 4))
print([next(p) for _ in range(5)])

# 斐波那契
class FibonacciProgression(Progression):
    def __init__(self, start1, start2):
        super().__init__(start1)
        self._next = start2

    def _advance(self):
        self._current, self._next = self._next, self._current+self._next

    def show(self, n):
        it = iter(self)
        for _ in range(n):
            print(next(it))

p = iter(FibonacciProgression(2, 4))
print([next(p) for _ in range(5)])
p = FibonacciProgression(2, 4)
p.show(5)


