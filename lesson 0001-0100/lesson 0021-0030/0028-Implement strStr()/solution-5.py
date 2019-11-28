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
        next, p, q, lenh, lenn = [-1]*len(needle), 0, 0, len(haystack), len(needle)

        # KMP算法的核心, 是怎么算出这个next数组

        i = 1
        while i < lenn:
            # 注意, 计算next的时候, 其实就已经用到了后面的匹配思想用于加速计算
            # 比如: dabcdabde, 计算到d的时候 dabcdab-de, 其next值为3, 即next[7]=k=3
            # 下面计算next[8], dab-c-dab-d-e, 如果needle[k]=needle[i-1], 那么
            # next[8]=next[7]+1; 如果不等于, 换个例子, dad-c-dad-d-e
            # 那么q索引置为next[k]=1
            # dadd      dadd
            #   dadc       dadc
            # aabaaac
            k = next[i-1]
            # next[0]=-1, 这里边界取-1, 表示next[0]也没匹配上再进一次循环处理这种情况
            while k >= -1:
                if k == -1 or needle[i-1] == needle[k]:
                    next[i] = k+1
                    break
                else:
                    k = next[k]
            i += 1

        # j, k = 0, -1
        # while j < lenn-1:
        #     if k == -1 or needle[j] == needle[k]:
        #         k, j = k+1, j+1
        #         next[j] = k
        #     else:
        #         k = next[k]

        # 计算出next后, 匹配代码如下
        while p < lenh and q < lenn:

            # 匹配时有三种情况, 一是对应字符匹配上, 不用想, 各自加1
            # 第二种是needle的第一个字母就没匹配上, 那么q不变, p加1
            # 第三种是匹配了一部分, p到某个位置匹配不上了, 那么q重置0, p不变
            # 后两种匹配不上的可以在本次循环判断q是否为0做不同处理(这种更容易想)
            """
            if haystack[p] == needle[q]: p, q = p+1, q+1
            else: p, q = (p+1, 0) if q == 0 else (p, next[q])
            """
            # 第二种写法, 利用next[0]等于-1的特点, 在下一轮循环, 判断q为-1, 那么p和q各自加1,
            # 变成p+1和0
            # if q == -1 or haystack[p] == needle[q]: p, q = p+1, q+1
            # else: q = next[q]

            # 第三种写法, 逻辑上更好想
            while q >= -1:
                if q == -1 or haystack[p] == needle[q]:
                    q = q+1
                    break
                else:
                    q = next[q]
            p += 1

        return p-lenn if q == lenn else -1


s = Solution()
print(s.strStr("aabaaabaaac","abaaa"))
