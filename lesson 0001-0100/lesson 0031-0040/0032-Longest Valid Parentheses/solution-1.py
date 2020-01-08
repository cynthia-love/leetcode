# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: )()()), 找到最长的子串, 符合括号规则, 输出该长度
"""
"""
    方法1, 暴力法, 对于每一个子串, 判断其是否符合括号规则, 符合记录长度, 最后选一个最长的
    至于括号规则, 记录左右括号个数p和q, 满足q始终<=p, 且最终q==p
"""
"""
    不出意外, 超时
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def isValid(s: str, start: int, end: int) -> bool:
            p, q = 0, 0
            for i in range(start, end + 1):
                if s[i] == '(':
                    p += 1
                else:
                    q += 1

                if q > p: return False

            return True if p == q else False

        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isValid(s, i, j):
                    ans = max(ans, j - i + 1)

        return ans


s = Solution()
print(s.longestValidParentheses(")()())"))
