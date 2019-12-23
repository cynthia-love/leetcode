# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: s = "barfoothefoobarman", words = ["foo","bar"]
    找到s中所有子串的起始索引, 子串的概念为words中的所有单词拼起来(不限先后次序)
    比如这里可以找foobar也可以找barfoo, 限定每个单词长度一致
"""
import re
from typing import List


class Solution:
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        size_l, size_w = len(words), len(words[0]),
        l_index, ans = [0] * len(words), []

        for o in range(len(s)-size_l * size_w+1):
            l_index = [0] * len(words)
            for i in range(o, o+size_l * size_w):
                flag = False
                for j in range(size_l):
                    if l_index[j] > size_w - 1:
                        continue

                    if words[j][l_index[j]] == s[i]:
                        l_index[j] += 1
                        flag = True

                    if l_index[j] > size_w - 1:
                        l_index = [x if x > size_w - 1 else 0 for x in l_index]

                if not flag:
                    l_index = [0] * len(words)

                if sum(l_index) == size_l * size_w:
                    ans.append(o)
                    l_index = [0] * len(words)

        return ans


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []

        ans, index, lens, size = [], 0, len(words), len(words[0])

        while index <= len(s)-lens*size:




s = Solution()
print(s.findSubstring("", []))
