# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: (){}[]判断是否是合法的括号字符串
    栈
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack, d = [], {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "["}
        for v in s:
            if not stack or stack[-1] != d[v]:
                stack.append(v)
            else: stack.pop()
        return True if not stack else False


s = Solution()
print(s.isValid("[{}][]"))