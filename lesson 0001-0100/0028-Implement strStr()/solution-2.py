# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 双指针
    helallo-ll, pq初始指向h和l
    h->e->l->a
    l->l->l->第二个l匹配不上, 那么重置q
    好像和方法1没有本质区别, 都是从某一个位置开始遍历比较, 没比上, 再从下一个位置遍历比较
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle: return 0
        len1, len2, p, q = len(haystack), len(needle), 0, 0

        while p < len1 and q < len2:
            # 相等后移一位
            if haystack[p] == needle[q]: p, q = p+1, q+1
            # 不相等, q后移了, p重置为这次开始匹配的下一个位置, q重置为0
            elif q != 0: p, q = p-q+1, 0
            # 不相等, 且q为0, 直接后移p
            else: p += 1

        # 如果是q比完出来的, 说明找到了子串
        if q == len2: return p-len2
        else: return -1


s = Solution()
print(s.strStr("mississippi", "issip"))
