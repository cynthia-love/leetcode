# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 和问题12相反, 罗马数字转整数; 范围: 1-3999
    问题12里, 要从大到小去贪心, 所以映射存成[(int: str)...]最合适
    而这题需要知道某子串是不是能映射成数字, 用字典存最合适
"""


class Solution:
    def romanToInt(self, s: str) -> int:

        d = {'XL': 40, 'V': 5, 'M': 1000, 'C': 100, 'IV': 4, 'I': 1, 'IX': 9,
             'CD': 400, 'L': 50, 'X': 10, 'D': 500, 'XC': 90, 'CM': 900}

        ans, i = 0, 0
        while i <= len(s)-1:
            if s[i:i+2] and s[i:i+2] in d:
                ans, i = ans+d[s[i:i+2]], i+2
            else:
                ans, i = ans+d[s[i]], i+1

        return ans


s = Solution()
print(s.romanToInt("IX"))
