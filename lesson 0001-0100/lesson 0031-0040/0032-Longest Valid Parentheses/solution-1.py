# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: )()()), 找到最长的子串, 符合括号规则, 输出该长度
"""
"""
    方法1, 暴力法, 对于每一个子串, 判断其是否符合括号规则, 符合记录长度, 最后选一个最长的
    至于括号规则, 记录左右括号个数p和q, 满足p始终>=q, 且遍历完p==q
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

                # 遍历的过程中如果发现右括号个数大于左括号， 说明肯定不符合要求
                if q > p: return False

            # 全部遍历完， 满足p==q， 符合规则； 否则， 不符合要求
            return True if p == q else False

        ans = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if isValid(s, i, j):
                    ans = max(ans, j - i + 1)

        return ans


s = Solution()
print(s.longestValidParentheses(")()())"))
