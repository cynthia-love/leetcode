# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 马拉车
    思路: 和找最大不重复子串类似, 比如 abcdea, 处理a的时候找到了e, 那么处理b的时候, 在a的最大不重复
    子串的边界内, b不用从下一个字符遍历, 直接从e的下一个字符开始即可
    马拉车算法也是这么个思路, dbabababd, 比如遍历到中间a的时候其回文串边界到了右侧d, 然后下下个字符
    a, 在回文串边界范围内, 其以中间a对称的左元素a的回文串长度3, 那么因为对称性, 右a的回文串为3和到
    边界d距离的最小值
    实际编码的时候会用#把每个字符隔开, 并且用不包括当前元素在内的单侧半径代表回文长度, 便于逻辑设计

    #a#b#c#d#e#, 用#隔开可以使字符串变成奇数形式, 便于处理

    处理完之后, 马拉车算法目标可以归结为求p, p[i]表示以i为中心的最长回文半径

    char	#	a	#	b	#	b	#	a	#	b	#	b	#
    index	0	1	2	3	4	5	6	7	8	9	10	11	12
    p		0   1   0   1   4   1   0

"""


class Solution:

    def longestPalindrome(self, s: str) -> str:

        s2 = '#'+'#'.join(s)+'#'
        # m表示之前处理过的延伸最远的回文的中心, r为回文右边界
        p, m, r, len2, imax = [0]*len(s2), 0, 0, len(s2), 0

        for i in range(len2):
            # 寻找i元素起始扩散位置; i相对于m的对称点是 m-(i-m)
            ir = i+1 if i >= r else i+min(p[2*m-i], r-i)+1
            il = i*2-ir
            while il >= 0 and ir <= len2-1 and s2[il] == s2[ir]:
                il, ir = il-1, ir+1
            p[i] = ir-1-i

            # 这里记住就好, 没必要后面再遍历一次p找
            if p[i] > p[imax]:
                imax = i

            # 如果最新的回文右边界超过了之前的最右边界, 则移动中心点和右边界
            if ir-1 > r:
                m, r = i, ir-1

        return s2[imax-p[imax]:imax+p[imax]+1].replace("#", "")


s = Solution()
print(s.longestPalindrome("abadabaf"))

