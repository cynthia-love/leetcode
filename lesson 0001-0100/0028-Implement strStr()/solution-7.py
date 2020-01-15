# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法7, Sunday算法, 顺序上和KMP一样是从前往后, 思路上则是类似BM算法
    只不过其在找坏字符的时候, 是从匹配串的下一位去找
    aaabbbxcd
    aaadbb      匹配到第一个b的时候, 没匹配上, 直接去找x看模式串里有没有
    如果没有, 则直接移动lenn+1个位置, 如果有:
    aaabbbxcd   移动距离3, 即lenn-最右x的索引
    aaaxbb
"""
from collections import defaultdict


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        lenh, lenn = len(haystack), len(needle)
        shift = defaultdict(lambda: lenn+1)

        for i in range(lenn):
            shift[needle[i]] = lenn-i
        print(shift)

        p = 0
        while p <= lenh-lenn:
            p1, p2 = p, 0
            while p2 <= lenn-1:
                if haystack[p1] != needle[p2]:
                    p += shift[haystack[p+lenn]] if p+lenn < lenh else lenn
                    break
                p1, p2 = p1+1, p2+1

            if p2 > lenn-1: break

        return p if p <= lenh-lenn else -1


s = Solution()

print(s.strStr("aaaaa", "bba"))