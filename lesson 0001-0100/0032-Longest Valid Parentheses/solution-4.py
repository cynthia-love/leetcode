# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 动态规划
    如果直接按长度2， 4， 6， 8去做动规， 效果有限， 尤其对于(())((()))这种4+6很麻烦
    一个比较好的思路是按结尾算， 记以i结尾的最长子字符串长度, 这样一次遍历就完事
    另外， 这么考虑还有个好处是， 对于结尾为(的， 求都不用求

    动规方程情况1， ......()， m[i] = m[i-2]+2 if s[i-1]=="(" and s[i] == ")"
    动规方程情况2， ......)),
        比如((())), m[i] = m[i-1]+2 if s[i-m[i-1]-1]=="(" and s[i] ==")", 特别地m[i-1]为0也符合该式子
        比如(())((())), 相较于上式， 改成m[i] = m[i-1]+2+m[i-m[i-1]-2], 这是最一般的情况
    合并一下：m[i] = 2+m[i-1]+m[i-m[i-1]-2] if s[i-m[i-1]-1]=="(" and s[i] == ")"
    该式子三种情况都适用
"""
from collections import defaultdict


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        m = defaultdict(int)

        for i in range(1, len(s)): m[i] = 2+m[i-1]+m[i-m[i-1]-2] if s[i] == ")" and i-m[i-1]-1 >= 0 and s[i-m[i-1]-1] == "(" else 0

        return max(m.values()) if m else 0


s = Solution()
print(s.longestValidParentheses("((())((())))"))
