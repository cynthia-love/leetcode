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
            # abc, abcd, 3到0, 4到1, 都是len/2-1
            for i in range(int(len(subs)/2)):
                # 0堆len-1, 1对len-1-1
                j = len(subs)-1-i

                if subs[i] != subs[j]:
                    return False
            return True

        ans = ""
        for i in range(len(s)):
            # 注意j要从i开始, 因为也要判断单个字符的情况
            for j in range(i, len(s)):
                if isPalindrome(s[i: j+1]) and j-i+1 > len(ans):
                    ans = s[i: j+1]

        return ans


s = Solution()
print(s.longestPalindrome("aaa"))
