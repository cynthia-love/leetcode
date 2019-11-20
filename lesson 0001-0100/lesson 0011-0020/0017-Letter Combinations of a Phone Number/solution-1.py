# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 2-9各有自己代表的字母(9键), 给定一个数字字符串, 输出所有可能的字母组合
    比如23, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""
"""
    方法1, 暴力遍历, 比如2的时候ans是['a', 'b', 'c'], 再来个3, 对于3对应的每个
    字符, 遍历ans往后拼, 每有一个字符来个ans的副本, 然后再拼到一起成为新的ans
    另外, 感觉这有点像是广度优先遍历?
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
        ans = ['']

        for i in digits:
            ans_cur = []

            for s in d[i]:
                ans_cur.extend([x+s for x in ans])
            ans = ans_cur

        return ans


s = Solution()
print(s.letterCombinations("234"))