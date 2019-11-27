# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法5, KMP
    核心思想:
    ABMMMABD
    ABMMMABX, 这里发现匹配不上, 不是从B开始重新匹配, 而是利用pattern的特点

    ABMMMABD
         ABMMMABX, 这么开始匹配, p指针还是指向D, 不变

    所以KMP算法的关键就是如果哪个字符匹配不上, 如何移动q指针

    比如这里的X, 其前面子串为ABMMMAB, 头尾最大同子串为AB-AB, 即长度2
    那么q指针匹配不上的时候, 移动到2即可
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        #if not needle: return 0 aabaaac
        # 先计算i位置之前的子串的前后公共子串长度
        # 比如ababab, 0号位-1, 1号位0, 2号位0, 3号位aba-b, 1, 4号位abab-a, 2
        step, p, q = [-1]*len(needle), 0, 0

        for i in range(1, len(needle)):

            step[i] = step[i-1]+1 if i == 1 or needle[step[i-1]] == needle[i-1] else step[i-1] if needle[i-1] == needle[i-1-step[i-1]] else 0

        while p < len(haystack) and q < len(needle):

            if haystack[p] == needle[q]: p, q = p+1, q+1
            else: p, q = (p+1, q) if q == 0 else (p, step[q])

        return p-q if q == len(needle) else -1





        # # 第一步, 先计算needle各字符匹配不上后跳转的索引
        # step = [0]*len(needle)
        #
        # i = 0
        # k = -1
        # step[0] = -1
        # while i < len(needle)-1:
        #     if k == -1 or step[i] == step[k]:
        #         i, k, step[i] = i+1, k+1, k+1
        #     else: k = step[k]
        #
        # print(step)
        #
        # i, j, slen, plen = 0, 0, len(haystack), len(needle)
        #
        # while i < slen and j < plen:
        #     if j == -1 or haystack[i] == needle[j]:
        #         i, j = i+1, j+1
        #     else: j = step[j]
        #
        # if j == plen: return i-j
        # else: return -1


s = Solution()
print(s.strStr("aabaaabaaac","aabaaac"))
