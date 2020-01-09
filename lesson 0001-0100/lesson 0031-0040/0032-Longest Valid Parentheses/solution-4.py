# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 动态规划
"""
from collections import defaultdict

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if not s or not s[1:]: return 0
        mem = defaultdict(int)

        for l in range(2, len(s)+1, 2):

            for i in range(len(s)-l+1):

                j = i+l-1

                if l == 2:
                    mem[(i, j)] = j-i+1 if s[i] == '(' and s[j] == ')' else 0
                else:

                    if mem[(i+1, j-1)] and s[i] == '(' and s[j] == ')':
                        mem[(i, j)] = j-i+1
                    else:
                        for p in range(i+2, j, 2):
                            if mem[(i, p-1)] and mem[(p, j)]:
                                mem[(i, j)] = j-i+1
                                break

                # print(l, len(s), i, j, s[i: j+1], mem[(i, j)])
        return max(mem.values())


s = Solution()
print(s.longestValidParentheses(")(((((()())()()))()(()))("))
