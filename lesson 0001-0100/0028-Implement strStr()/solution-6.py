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

        p = lenn-1

        while p <= lenh-1:

            k = 0
            while k <= lenn-1:
                p1, p2 = p-k, lenn-1-k
                if haystack[p1] == needle[p2]:
                    k += 1
                else:
                    # 先处理坏字符
                    # 如果该坏字符在needle没有, 移动距离(把0号位移动到p2下一个位置)p2+1-0=p2-(-1)
                    # 如果该坏字符在needle里有, 移动距离p2-bc[haystack[p1]]
                    p_next = max(p+1, p+p2-bc[haystack[p1]])
                    # 仅利用坏字符特性和p+1取max, 即可完成匹配

                    # 坏字符处理完处理好后缀, 如果存在, 移动距离p2+1-suffix[k]
                    if suffix[k] != -1: p_next = max(p_next, p+p2+1-suffix[k])
                    # 仅利用坏字符特性和好后缀, 再算上p+1取max, 也可以完成匹配

                    else:
                        # 如果不存在, 去找存在的前缀, 找到了, 移动距离lenn-1-(k-1)-0
                        while k >= 1:
                            if prefix[k]:
                                p_next = max(p_next, p+lenn-k)
                                break
                            k -= 1

                    p = p_next
                    break

            if k > lenn-1: break

        return p-lenn+1 if p <= lenh-1 else -1


s = Solution()

print(s.strStr("babbbbbabb", "bbab"))

