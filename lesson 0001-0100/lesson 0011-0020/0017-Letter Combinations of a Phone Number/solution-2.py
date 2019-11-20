# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 利用python[]特性, 相对于方法1, 更简洁, 更pythonic
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits: return []
        ans = [""]

        for i in digits:

            ans = [m+n for m in ans for n in d[i]]

        return ans


s = Solution()
print(s.letterCombinations("234"))
