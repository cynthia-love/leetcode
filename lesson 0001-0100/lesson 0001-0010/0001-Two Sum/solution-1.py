# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 在数组里找到两个和为target的元素, 返回他们的索引. 解唯一. 元素不能重复用.
"""
"""
    方法1, 暴力遍历
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int)->List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
