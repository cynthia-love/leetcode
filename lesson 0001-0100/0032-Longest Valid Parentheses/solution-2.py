# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: )()()), 找到最长的子串, 符合括号规则, 输出该长度
"""
"""
    方法2, 暴力法的第二种实现, 栈; 除了isValid方法, 对外层遍历也做一下小优化
"""
"""
    相对于第一种实现, 耗时上好像没啥变化
"""
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        def isValid(s, start, end):
            stack = deque()
            for i in range(start, end+1):
                # 如果stack为空， 看s[i]， 为）直接退出， 否则入栈
                if not stack:
                    if s[i] == '(': stack.append(s[i])
                    else: return False
                # 如果stack不为空， ((， s[i]为（， 继续入栈， 为）， 出栈
                else:
                    if s[i] == '(': stack.append(s[i])
                    else: stack.pop()
            # 全部遍历完， 符合要求的情况为栈为空
            return True if not stack else False

        ans = 0

        # 遍历2 4 6 8 10 len(s)
        # 外层用长度而不是i， j的好处是不用再判断max ans了， 后面的符合条件的肯定比前面的优
        for l in range(2, len(s)+1, 2):
            for i in range(len(s)-l+1):
                # 由于l是递增的, 这里无脑赋值ans就行
                if isValid(s, i, i+l-1):
                    ans = l
        return ans


s = Solution()
print(s.longestValidParentheses(")()())"))
