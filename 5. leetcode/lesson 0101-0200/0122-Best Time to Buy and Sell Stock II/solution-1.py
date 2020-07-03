# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 股价[7,1,5,3,6,4], 计算能获取的最大利润, 要求再次购买前必须把之前的卖了, 即不能连续买
    看题目描述有点懵, 实际上没那么复杂, 看一眼股价曲线图, 怎么利润最高, 就是所有的增加曲线都占了
    所有曲线种类都能转化成四种情况的子问题:
    1 2 3 4, 全增
    4 3 2 1, 全减
    1 2 3 4 3 2 1, 先增再减, 情况1+情况2, 我们只考虑增加的部分
    4 3 2 1 2 3 4, 先减再增, 情况2+情况1, 我们只考虑增加的部分
    核心思路: i大于i-1, 就把这部分利润加进去, 不用担心连增
    1 2 3 4, 4-1=2-1+3-2+4-3

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
