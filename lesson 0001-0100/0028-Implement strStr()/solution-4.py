# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 切片
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


s = Solution()
print(s.strStr("mississippi", "issip"))
