# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法6, BM算法, 从后往前匹配(KMP是从前往后), 核心思路:
    1. 坏字符规则
    ababcb                                                          ababcb
    maaxcb, 匹配到x的时候, 发现和b不一致, 如果模式里没有b, 则移动:               maaxcb
                                                                    ababcb
    但是这里模式里有b, 按坏字符规则, 应该让错配的位置和模式里最右该字符对齐    maaxcb
    会造成倒退
                                                                       ↓
    2. 为了避免倒退, 一种办法是, 只允许从错配的位置的左边去找最右该字符, 比如    xxbabab
                   xxbabab                                          xabmbab
    箭头位置错配,      xabmbab,  向右移动了两位, 而暴力法只会移动一位
    之所以找左边的最右而不是左边的最左, 因为按最左的最左移动, 可能会移多了       xxaabbb
                                                                    aabbbbb
    xxaabbb               xxaabbb
       aabbbbb 移多了        aabbbbb, 刚好

    3. 为了避免倒退, 还有一种办法, 即BM算法的另一个思想, 好后缀
        ↓
    bcabbabdab   只按坏字符, 会倒退; 按坏字符优化, 模式只往右移动一位, 而按好后缀能移动三位
    bbabdab         ↓
                bcabbabdab               deaba
                   bbabdab               ababa

    4. 如果好后缀找不到怎么办
        ↓
    d-abcabc    好后缀abc找不到, 退而求其次, 找bc, 注意, 找bc的时候必须从头部找, 为什么
    d-bcdabc    因为这里已经确定了没有abc, 只能舍弃a, 直接从bc开始匹配, 所以得从头部找

    然而这里bc也没有, c也没有, 那就只能  dabcabc
                                           dbcdabc了

"""
from collections import defaultdict


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        # 生成坏字符, 含有的字符, 取右索引; 不含的, 可以用-1(像KMP算法一样设置-1可以方便写代码)
        bc, lenh, lenn = defaultdict(lambda: -1), len(haystack), len(needle)
        for i in range(lenn):
            bc[needle[i]] = i
        print(bc)

        # 生成后缀对应的前面的索引, 注意, 由于可能有多个, 所以没法根据是否为0判断是不是前缀
        # 需要单独生成一个前缀数组存, 比如: cabcabcab, 那么suffix[3]先算出来0, 后面又算出来3
        # 那么在算出来0的时候, 就要置prefix[3]为True了, 有长度又是0开始, 没必要存尾索引
        suffix, prefix = [-1]*lenn, [False]*lenn
        # 思路, cabcab, 先c-b, 再ca-ab, 再cab-cab, 再cabc-bcab, 再cabca-abcab
        # 思考下为什么这样可以求出suffix
        for i in range(lenn-1):
            p, k = i, 1
            while p >= 0 and needle[p] == needle[lenn-k]:
                suffix[k] = p
                p, k = p-1, k+1
            if p == -1: prefix[k-1] = True

        i = 0

        while i <= lenh-1:
            p, q = i+lenn-1, lenn-1
            """
                0123, 坏字符不行, 好后缀没有, 前缀没有
                aabaa
                bddaa
            """
            while p >= i and q >= 0 and haystack[p] == needle[q]:
                p, q = p-1, q-1

            if q < 0: break

            # 没有匹配上, 那么haystack[p]为坏字符, 取其bc值
            print(haystack[p])
            # 情况1, bc值不为-1, 比如为2, 那么2号位要和p对齐, 即i=p-2
            # 如果为-1, i=p+1=p-(-1)
            i1 = p-bc[haystack[p]]

            # 没有匹配上, 处理好后缀, suffix[lenn-q-1]
            k = lenn-q-1
            # 情况1, suffix不为-1, 即存在, 比如为2, 那么2号位要和p+1对齐, 即i=p+1-suffix[k]
            i2 = p+1-suffix[k]
            i3 = -2
            # 情况2, suffix为-1, 即不存在, 那么取看前缀, 假如k=2的时候找到了
            if suffix[k] == -1:
                while k >= 1:
                    if prefix[k]:
                        i3 = i+lenn-k
                        break
                    k = k-1
                if k == 0:
                    i3 = i+lenn
            # 如果k=0, 即取不到前缀
            i = max(i1, i2, i3, i+1)

        if i > lenh-1: return -1
        else: return i



s = Solution()

print(s.strStr("aabaaabaaac", "aaac"))

