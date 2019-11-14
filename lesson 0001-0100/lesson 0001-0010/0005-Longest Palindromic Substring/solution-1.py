# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 寻找最大回文子串
"""
"""
    方法1, 暴力遍历, 会超时
    遍历所有子串, 判断是不是回文
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(subs: str):

            for i in range(int(len(subs)/2)):
                j = len(subs)-i-1

                if subs[i] != subs[j]:
                    return False
            return True

        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i: j+1]) and j-i+1 > len(ans):
                    ans = s[i: j+1]

        return ans


s = Solution()
print(s.longestPalindrome("aaa"))
