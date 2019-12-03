# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 递归形式
       3
    3|100
    3->30->300, 发现大了, 回去
"""


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        flag = (dividend >= 0) ^ (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0

        def rf(divisor):
            nonlocal dividend
            nonlocal result

            if divisor > dividend: return

            rf(divisor << 1)

            if dividend >= divisor:
                dividend -= divisor
                result = (result << 1)+1
            else:
                result = result << 1

        rf(divisor)

        return -result if flag else 2**31-1 if result >= 2**31 else result


s = Solution()
print(s.divide(1, 3))


