# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 排序后比较第一个和对后一个
    注意["a"]输出"a"
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: return ""

        strs.sort()

        ans = strs[0]

        while not strs[len(strs)-1].startswith(ans):
            ans = ans[:len(ans)-1]

        return ans


s = Solution()
print(s.longestCommonPrefix(["aaa", "aabcde", "acx"]))