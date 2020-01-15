# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    先不考虑计算过程中的溢出, 都转化成正数去算
    方法2, 左移被除数, 好处是不会损失精度
       3            3
    3|100  ->  30|100
"""


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        flag = (dividend >= 0) ^ (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)

        count = 0
        while dividend >= divisor:
            divisor <<= 1
            count += 1
        divisor >>= 1
        count -= 1

        result = 0
        while count >= 0:

            if dividend >= divisor:
                result += 1 << count
                dividend -= divisor
            divisor >>= 1
            count -= 1

        return -result if flag else 2**31-1 if result >= 2**31 else result


s = Solution()
print(s.divide(10, 3))
