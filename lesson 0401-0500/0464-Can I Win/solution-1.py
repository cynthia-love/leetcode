# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 两名玩家轮流选择从 1 到 n 的任意整数，累计整数和，先使得累计整数和达到 sum 的玩家，即为胜者; 不可重复选
    比如: n为10, sum为11
    无论第一个玩家选多少, 哪怕选了1, 第二个选10就能 >= sum
    判断先出手的能否稳赢(即存在一条路, 对方怎么选都能自己赢)
    思考一下稳赢意味着什么, 比如x1, x2, x3, ... xn, 累计和sum
    第一个玩家选了xi, 子问题: 从x1...xn(不含xi)里选
"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        pass

s = Solution()
print(s.canIWin(10, 11))