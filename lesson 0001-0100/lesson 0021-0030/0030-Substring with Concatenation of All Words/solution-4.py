# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 比较思路还是hash, 但是方法2每次截断后再去比较, 不够丝滑
    比较丝滑的方法是一次遍历s就得出答案
    abcabcbacacb, ['abc', 'bac']
    起始点有3个, 每条线只跟自己内部比
    abc-abc-bac-acb
     bca-bcb-aca
      cab-cba-cac

"""
from typing import List
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        ans, lens, size, h = [], len(words), len(words[0]), defaultdict(int)

        for word in words: h[word] += 1

        h_s = [defaultdict(int) for i in range(size)]

        # h_s 初始化, 省去后面多余的判断
        for i in range(min(len(s), lens*size)):
            h_s[i % size][s[i: i + size]] += 1
        for i in range(size):
            if h_s[i] == h: ans.append(i)

        for i in range(min(len(s), lens*size), len(s)-size + 1):
            b = i % size
            h_s[b][s[i: i + size]] += 1
            word = s[i - lens*size: i - lens*size + size]
            h_s[b][word] -= 1
            if h_s[b][word] == 0: h_s[b].pop(word)
            if h_s[b] == h: ans.append(i-(lens-1)*size)

        return ans



s = Solution()
print(s.findSubstring("barfoothefoobarman"
                      , ["foo", "bar"]))
