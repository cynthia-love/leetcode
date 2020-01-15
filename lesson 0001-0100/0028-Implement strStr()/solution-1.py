# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 寻找第一个子串的索引, 比如hello, ll, 则返回2
"""
"""
    方法1, 第一反应是全遍历
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle: return 0

        for i in range(len(haystack)-len(needle)+1):

            p, q = i, 0
            while q < len(needle):
                if haystack[p] != needle[q]: break
                else: p, q = p+1, q+1

            if not needle[q:]: return i

        return -1


s = Solution()
print(s.strStr("hello", "ll"))