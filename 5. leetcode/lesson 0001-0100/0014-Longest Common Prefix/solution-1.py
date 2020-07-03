# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 寻找公共前缀, 比如["flower","flow","flight"], 则输出"fl", 否则输出""
"""
"""
    方法1, 从0号位开始, 同时比较每个字符串的i号位置, 如果不完全相同则退出循环
    这种方法比较直接的思路是都和第一个字符串去比, 看相等不相等
"""
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: return ""

        # 从前往后遍历第一个字符串, 保证后面的对应位置都和第一个一样, 看能遍历到哪
        ans, i = "", 0

        while i <= len(strs[0])-1:

            flag = True
            for j in range(1, len(strs)):
                if not strs[j][i:] or strs[j][i] != strs[0][i]:
                    flag = False
                    break
            if not flag: break
            i += 1

        return strs[0][:i]


s = Solution()
print(s.longestCommonPrefix([]))
