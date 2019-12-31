# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法5, 对方法3的进一步优化

    针对每个条线内部窗口滑动的时候, 存在以下几种情况可以进行优化:
    1. 当前hash匹配上了, 那么下一个hash只需要比较要出去的和要进来的
    2. 当前判断过程中发现不在words里的单词, 那么窗口进行大跳
    3. 之前有次数超限的单词, 那么一直要等到能够移除这个单词才能进行正常判断
    如果用这种方法, 需要对hash进行比较精细的比较, 就不能像方法3那样直接整体比较俩hash了
"""
"""
    偶尔能进到60-70ms
"""
from typing import List
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []

        lens, size, h, ans = len(words), len(words[0]), defaultdict(int), set()
        for item in words: h[item] = h[item]+1

        # 分size个条线去遍历
        for i in range(size):
            count, h_s = 0, defaultdict(int)
            for j in range(i, len(s)-size+1, size):
                rword = s[j: j+size]
                # 优化点2, 大跳
                if rword not in h:
                    count, h_s = 0, defaultdict(int)
                else:
                    h_s[rword], count = h_s[rword] + 1, count + 1
                    # 遍历前lens-1个子串, 加完hash直接continue
                    if count < lens:
                        continue
                    # 第一次遍历完lens个子串
                    if count == lens:
                        if h_s == h: ans.add(j-(lens-1)*size)
                        continue
                    if count == lens+1:
                        lword, left = s[j-lens*size: j-lens*size+size], j-lens*size
                        h_s[lword], count = h_s[lword] - 1, count - 1
                        # 优化点3, 判断移除后, 对应单词的次数是否满足要求了, 不满足直接continue
                        if h_s[lword] > h[lword]: continue
                        # 减完后次数为0的, 得把key删了, 不然直接比较hash比较不了
                        if h_s[lword] == 0: h_s.pop(lword)
                        # 如果上一个子串匹配上了, 即优化点1
                        if left in ans:
                            if rword == lword: ans.add(left+size)
                        else:
                            if h_s == h: ans.add(left+size)

        return list(ans)


s = Solution()
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))