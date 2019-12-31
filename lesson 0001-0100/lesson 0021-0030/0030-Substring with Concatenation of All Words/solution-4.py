# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 相对于方法3, 先把第一组求出来, 这样就不用每次循环里判断长度了

"""
"""
    80ms左右
"""
from typing import List
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        ans, lens, size, h = [], len(words), len(words[0]), defaultdict(int)

        for word in words: h[word] += 1

        # word长度是多少, 就有多少个条线, h_s的长度就是多少
        h_s = [defaultdict(int) for i in range(size)]

        # h_s 初始化, 省去后面多余的判断
        for i in range(min(len(s), lens*size)):
            h_s[i % size][s[i: i + size]] += 1
        for i in range(size):
            if h_s[i] == h: ans.append(i)

        for i in range(min(len(s), lens*size), len(s)-size + 1):
            b = i % size  # 归属哪个条线
            # 最右word入hash, 最左word出hash
            h_s[b][s[i: i + size]] += 1
            word = s[i - lens*size: i - lens*size + size]
            h_s[b][word] -= 1
            # 对于出之后数量为0的, 需要删了, 不然没法直接比较
            if h_s[b][word] == 0: h_s[b].pop(word)
            if h_s[b] == h: ans.append(i-(lens-1)*size)

        return ans


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
