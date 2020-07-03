# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 动态规划, 写倒是好写, 直接去翻译回溯法, 问题是这题看着不像有子问题被重复计算
    不过确实用动态规划后, 速度提升显著...

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}

        def dp(i, j):
            print(i, j)
            if (i, j) in mem:
                return mem[(i, j)]
            # 如果p到头, 看s到没到头
            if not p[j:]: return not s[i:]

            fmatch = bool(s[i:]) and p[j] in {s[i], '.'}

            # 处理x*的情况
            if p[j+1:] and p[j+1] == '*':
                ans = dp(i, j+2) or (fmatch and dp(i+1, j))
            else:
                # 处理非x*的情况
                ans = fmatch and dp(i+1, j+1)

            mem[(i, j)] = ans
            return ans

        return dp(0, 0)


s = Solution()
print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))