# -*- coding: utf-8 -*-

# Authro: Cynthia

"""
    方法2, 直接比较数字, 全翻转后和原值比较
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        ans, x2 = 0, x
        while x2:
            ans, x2 = ans*10+x2%10, x2//10

        return True if ans == x else False


s = Solution()
print(s.isPalindrome(121))
