# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 比如 [3, 8, 7, 2], 以3和8作为二维容器边界高度, 3和8的距离1作为容器宽, 那么容器容量
    为1*3, 同理3和2, 宽3高2, 3*2; 找到这个最大容量
"""
"""
    方法1, 不用想, 遇题不决暴力枚举, 不出意外, 超时
    对暴力枚举进行优化, 切入点有2:
    1. 在左边界确定的情况下, j不从i+1开始, 而是从保证当前容量不小于之前最大容量的右界的下一个位置开始
    2. 左边界是不断往右的, 也就是宽度在降低, 那么高度至少大于原左边界容量才有可能不降低(有点难想, 用
    控制变量法, 假定右边界不动, 一是右大于左, 容量受左边界控制, 显然右移宽度少了, 高度只能增加才有可能
    容量增加; 二十右小于左, 容量受右边界控制, 那么左边右移宽度减少高度不变, 容量只减不增
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, maxl = 0, 0
        for i in range(len(height)-1):
            if height[i] <= maxl: continue
            maxl = height[i]
            for j in range(i+int(ans/height[i])+1, len(height)):
                ans = max(ans, min(height[i], height[j])*(j-i))
        return ans


s = Solution()
print(s.maxArea([1, 1, 3]))

