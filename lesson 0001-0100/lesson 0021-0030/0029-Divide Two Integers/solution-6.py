# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法6, 结合方法4和方法5, 非递归, 但是找到头的过程中先不减dr
    100, 3
    100, 30
    100, 300

"""


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        dd, dr, r, c = abs(dividend), abs(divisor), 0, 0

        while c >= 0:
            if dd >= dr:
                dr, c = dr << 1, c + 1
            else:
                dr, c = dr >> 1, c - 1
                if dd >= dr and c >= 0:
                    dd, r = dd - dr, r + (1 << c)

        return r


s = Solution()
print(s.divide(100, 3))
