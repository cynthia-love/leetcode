# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 滑动窗口
    暴力法最大的问题是遍历了两次, 第一次截取子串, 第二次判断子串是否符合括号规则
    实际上可以在一次遍历中完成
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        p, q, ans, h = 0, 0, 0, {')': 0, '(': 0}

        while p <= len(s)-1 and q <= len(s)-1:

            if q < len(s)-1:
                h[s[q]] += 1

                if h['('] > h[')']:
                    q += 1
                elif h['('] < h[')']:
                    p, q, h['('], h[')'] = p + 1, q + 1, 0, 0
                else:
                    ans, q = max(ans, q - p + 1), q + 1

            else:
                if h['('] > h[')']:
                    h[s[p]], p = h[s[p]]-1, p+1




        return ans


s = Solution()
print(s.longestValidParentheses("(()"))
