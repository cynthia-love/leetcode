# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    一个简单的类定义
"""

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


if __name__ == "__main__":
    wallet = [
        CreditCard("BB", "BOCOM", "6222 2000002 122", 1000),
        CreditCard("BB", "BOCOM", "6222 2000002 123", 2000),
        CreditCard("BB", "BOCOM", "6222 2000002 124", 3000),
        CreditCard("BB", "BOCOM", "6222 2000002 125", 4000),
    ]

    wallet[0].charge(100)
    wallet[1].charge(200)
    wallet[2].charge(300)

    for i in range(4):
        print(wallet[i].get_account(), wallet[i].get_limit()-wallet[i].get_balance())

    wallet[0].revoke(10)
    print(wallet[0].get_account(), wallet[0].get_limit()-wallet[0].get_balance())