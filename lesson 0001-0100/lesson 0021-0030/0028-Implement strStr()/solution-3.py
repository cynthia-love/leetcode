# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 库函数
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)


s = Solution()
print(s.strStr("mississippi", "issip"))
