# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 考虑计算过程中的溢出
    本来想用负数计算的, 但是负数的位移运算搞不太明白, 还是先进行特例预处理吧
"""


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        # 结果溢出: -2**31/(-1); 取正溢出: -2**31
        # 另外, 算count的时候, 需要右移dividend而不能左移divisor, 不然也可能溢出
        MAX_INT, MIN_INT = 2**31-1, -2**31
        FLAG = (dividend >= 0) ^ (divisor >= 0)

        # 处理除数取正溢出, 处理完之后可以确保除数不为MIN_INT
        if divisor == MIN_INT:
            if dividend == MIN_INT:
                return 1
            else:
                return 0

        # 处理结果溢出及被除数取正溢出
        if dividend == MIN_INT and divisor == -1: return MAX_INT

        f1 = (dividend >= 0)
        # 比如8/2, 先变成6/2, 再比如-8/2, 变成-6/2, 8/-2变成6/-2, -8/-2, -6/-2
        dividend = dividend+divisor if FLAG else dividend-divisor
        f2 = (dividend >= 0)

        # 1/-1, 1/-2这种情况
        if f1 ^ f2: return 0 if dividend != 0 else -1 if FLAG else 1

        dividend, divisor = abs(dividend), abs(divisor)

        d, count = dividend, 0
        while d >= divisor:
            d, count = d >> 1, count+1

        count -= 1

        result = 0
        while count >= 0:
            d = dividend >> count
            if d >= divisor:
                result += 1 << count
                dividend -= divisor << count
            count -= 1

        result += 1

        return -result if FLAG else result


s = Solution()
print(s.divide(-2147483648, -1))