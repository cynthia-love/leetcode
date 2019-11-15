# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 输入一个字符串和一个最大高度, 输出对应z字形的横向字符串, 比如:
    输入 "PAYPALISHIRING", 3, 输出横向: "PAHNAPLSIIGYIR"
    P   A   H   N
    A P L S I I G
    Y   I   R
    思路, 整三个数组, 0-1-2-1-0-1-2-1-0这么来回折向append
    最后把三个数组拼一起即可(不整数组直接拿三个空字符串去拼接也可以)

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ls, tp = [""]*numRows, {0, numRows-1}
        p, i = 0, -1  # 如果第一个p==0也要拐的话那这里得初始化-1而不是1
        for c in s:

            ls[p] += c
            if p in tp:
                i = -i
            p += i

        return "".join(ls)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
