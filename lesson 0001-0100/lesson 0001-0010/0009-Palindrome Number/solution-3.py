# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 直接比较数字, 但仅对折一半
    这种方法要注意12210这种尾0的情况
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        x2, ans = x, 0
        # 1221, 121, 4321
        while ans < x2:
            ans, x2 = ans*10+x2%10, x2//10

        return True if ans == x2 or ans // 10 == x2 else False

s = Solution()
print(s.isPalindrome(0))
