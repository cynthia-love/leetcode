# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 整数转罗马数字, 从最大进制去枚举, 比如3000, 'M'*3
    看评论说这其实就是贪心思想?在对问题求解时，总是做出在当前看来是最好的选择
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        ans = ""
        for k, v in d:

            if num // k:
                ans, num = ans+v*(num // k), num % k

        return ans


s = Solution()
print(s.intToRoman(3))
