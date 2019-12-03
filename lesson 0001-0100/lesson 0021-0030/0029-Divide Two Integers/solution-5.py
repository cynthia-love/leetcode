# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法5, 大神的5行神仙解法, 学习一下
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b, r, t = abs(dividend), abs(divisor), 0, 1
        while a >= b or t > 1:
            if a >= b: r += t; a -= b; t += t; b += b
            else: t >>= 1; b >>= 1
        return min((-r, r)[dividend ^ divisor >= 0], (1 << 31) - 1)


s = Solution()
print(s.divide(7, 3))