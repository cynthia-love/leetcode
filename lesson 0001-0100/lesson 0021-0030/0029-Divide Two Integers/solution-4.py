# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 递归回溯
    比如: 100/3
    100, 3
        100, 30
            100, 300, return 100, 0
        100, 30, return 10, 3
    10 > 3, return 1, 3*10+3
"""


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        f, dd, dr = (dividend >= 0) ^ (divisor >= 0), abs(dividend), abs(divisor)

        def rf(dd, dr):

            # 递归回溯的头是除数左移大于了被除数
            if dd < dr: return dd, 0

            # 返回值为经递归子函数处理后被除数的剩余值和商
            dd, r = rf(dd, dr << 1)

            # 如果此时被除数大于除数, 该位为1否则为0
            # 为1, 则dd=dd-1*dr, 否则等于dd
            # 为1, 则r=(r<<1)+1, 否则等于r<<1
            return (dd-dr, (r << 1)+1) if dd >= dr else (dd, r << 1)

        # 最后一个返回的dd为余数
        left, ans = rf(dd, dr)
        return -ans if f else 2**31-1 if ans > 2**31-1 else ans


s = Solution()
print(s.divide(7, 3))


