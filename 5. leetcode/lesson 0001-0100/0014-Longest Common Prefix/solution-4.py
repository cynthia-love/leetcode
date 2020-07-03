# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 优化
    思路不变, 还是两两比较出一个ans再和第三个比较, 只不过两两比较方法可以优化, 更简洁
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        ans = strs[0]

        for s in strs:
            # aaa, abc, 不断地截短ans
            while not s.startswith(ans):
                ans = ans[:len(ans)-1]

        return ans


s = Solution()
print(s.longestCommonPrefix(["aaa", "abc", "aef"]))