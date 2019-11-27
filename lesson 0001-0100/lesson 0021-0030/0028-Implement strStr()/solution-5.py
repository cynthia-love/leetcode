# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法5, KMP
    核心思想, 即使匹配不上, 也有匹配上的部分, 这部分信息是可以利用的:
    ABMMMABD
    ABMMMABX, 这里发现匹配不上, 不是从B开始重新匹配, 而是利用pattern的特点

    ABMMMABD
         ABMMMABX, 这么开始匹配, p指针还是指向D, 不变, 但q指向M(有点马拉车算法的意思)

    所以KMP算法的关键就是如果哪个字符匹配不上, 如何移动q指针

    比如这里的X, 其前面子串为ABMMMAB, 头尾最大同子串为AB-AB, 即长度2
    那么q指针匹配不上的时候, 移动到2即可
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # 先计算i位置之前的子串的前后公共子串长度
        # 比如ababab, 0号位-1, 1号位0, 2号位0, 3号位aba-b, 1, 4号位abab-a, 2
        step, p, q, lenh, lenn = [-1]*len(needle), 0, 0, len(haystack), len(needle)

        # KMP算法的核心, 是怎么算出这个step数组
        for i in range(1, lenn):
            # 计算时有几种情况, 一是第二个字符, 则step值为0, 也可以利用step[0]的-1特性直接加1
            # 第二是不是第二个字符, 且右移出来的needle[i-1]刚好等于i-1字符最大前后子串下一个字符
            # 第三是不是第二个字符, 且右移出来的needle[i-1]并不等于i-1字符最大前后子串的下一个字符
            step[i] = step[i-1]+1 if i == 1 or needle[0+step[i-1]] == needle[i-1] else \
                step[i-1] if needle[i-1] == needle[i-2] else 0

        # 计算出step后, 匹配代码如下
        while p < lenh and q < lenn:

            # 匹配时有三种情况, 一是对应字符匹配上, 不用想, 各自加1
            # 第二种是needle的第一个字母就没匹配上, 那么q不变, p加1
            # 第三种是匹配了一部分, p到某个位置匹配不上了, 那么q重置0, p不变
            # 后两种匹配不上的可以在本次循环判断q是否为0做不同处理(这种更容易想)
            # 也可以利用step[0]等于-1的特点, 在下一轮循环, 判断q为-1, 那么p和q各自加1, 变成p+1和0
            """
            if haystack[p] == needle[q]: p, q = p+1, q+1
            else: p, q = (p+1, 0) if q == 0 else (p, step[q])
            """
            # 第二种写法
            if q == -1 or haystack[p] == needle[q]: p, q = p+1, q+1
            else: q = step[q]

        return p-lenn if q == lenn else -1





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
