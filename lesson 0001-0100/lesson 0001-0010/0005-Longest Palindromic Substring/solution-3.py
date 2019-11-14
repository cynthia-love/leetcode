# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 扩展中心, 长n的字符串有n+(n-1)个中心点, n-1表示两两之间的缝的个数
"""

class Solution:

    def longestPalindrome(self, s: str) -> str:

        ans, max_len = "", 0
        for i in range(len(s)):
            # 扩展以当前字符为中心的回文串
            # 注意不要拿半径k去扩展, 每次单算左右边界, 时间复杂度会增加很多
            l, r = i, i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l, r = l-1, r+1
            if r-l-1 > max_len:
                ans, max_len = s[l+1: r], r-l-1

            l, r = i, i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l, r = l-1, r+1
            if r-l-1 > max_len:
                ans, max_len = s[l+1: r], r-l-1

        return ans


s = Solution()
print(s.longestPalindrome("ab"))