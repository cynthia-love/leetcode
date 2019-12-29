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
        ans, lens, size = [], len(words), len(words[0])

        h = defaultdict(int)
        for word in words: h[word] += 1
        h_s, c_s = [defaultdict(int) for i in range(size)], [0]*size

        for i in range(len(s)-size+1):
            # 归属哪个序列
            b = i % size
            h_s[b][s[i: i+size]] += 1
            c_s[b] += 1

            if c_s[b] == lens:
                if h_s[b] == h:
                    ans.append(i-(lens-1)*size)
                word = s[i-(lens-1)*size: i-(lens-1)*size+size]
                h_s[b][word] -= 1
                if h_s[b][word] == 0: h_s[b].pop(word)
                c_s[b] -= 1
        return ans



s = Solution()
print(s.findSubstring("barfoothefoobarman"
, ["foo","bar"]))

