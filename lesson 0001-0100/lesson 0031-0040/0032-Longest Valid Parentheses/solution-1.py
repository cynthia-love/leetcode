# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: )()()), 找到最长的子串, 符合括号规则, 输出该长度
"""
"""
    方法1, 暴力法, 对于每一个子串, 判断其是否符合括号规则, 符合记录长度, 最后选一个最长的
    至于括号规则, 记录左右括号个数p和q, 满足q始终<=p, 且最终q==p
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def isValid(s: str, start: int, end: int) -> bool:
            pass
        pass


s = Solution()
print(s.longestValidParentheses(")()())"))
