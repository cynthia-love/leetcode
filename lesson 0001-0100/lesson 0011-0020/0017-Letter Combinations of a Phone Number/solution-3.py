# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 递归回溯
    深度遍历, 到头了再继续另外一个分支
    比如234, adg->adh->adi->aeg...
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

        ans = []

        def rf(s, digits):
            if not digits:
                ans.append(s)
                return

            for i in d[digits[0]]:
                rf(s+i, digits[1:])

        rf("", digits)
        return ans


s = Solution()
print(s.letterCombinations("234"))