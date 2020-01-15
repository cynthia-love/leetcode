# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 两遍滑动窗口


"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        ans = 0
        # 正向来一次, 处理左括号大于等于右括号的情况(()), ((())
        p, q, h = 0, 0, {')': 0, '(': 0}
        while p <= len(s)-1 and q <= len(s)-1:

            h[s[q]] += 1
            # 此时分为三种情况, 一是左等于右, 二是小于, 三是大于
            # 等于时, 添加ans, 然后q右移
            if h['('] == h[')']:
                ans = max(ans, q - p + 1)
                q += 1
            # 大于时, q右移
            elif h['('] > h[')']:
                q += 1
            # 小于时, 左右边界同时大跳
            else:
                p, q = q + 1, q + 1
                h[')'], h['('] = 0, 0
        # 反向来一次, 处理(小于等于)的情况, (()))
        p, q, h = len(s)-1, len(s)-1, {')': 0, '(': 0}
        while p >= 0 and q >= 0:
            h[s[p]] += 1
            if h[')'] == h['(']:
                ans = max(ans, q-p+1)
                p -= 1
            elif h[')'] > h['(']:
                p -= 1
            else:
                p, q = p-1, p-1
                h[')'], h['('] = 0, 0

        return ans


s = Solution()
print(s.longestValidParentheses(")(((((()())()()))()(()))("))
