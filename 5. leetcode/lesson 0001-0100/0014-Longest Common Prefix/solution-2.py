# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法1, 优化
    思路不变, 还是从第一个字符比较每个str是否一样, 一样才往下一个继续比
    但是这里不都和第一个比, 而是利用set
"""
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""

        # 利用zip特性, 纵向组合, 并截断不同长部分
        for col in zip(*strs):
            # 利用set去重
            h = set(col)
            if len(h) != 1:
                break

            ans += col[0]

        return ans


s = Solution()
print(s.longestCommonPrefix(["aca", "cba"]))