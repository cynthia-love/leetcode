# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 借助哈希存索引, 一次遍历向回找
    以1 2 2 3 4, 4为例, 初始哈希空, 然后:
    遍历到1时去哈希里找4-1存不存在
    遍历到2时去哈希里找4-2存不存在
    遍历到第二个2, 发现哈希里有4-2, 找到解
    由于哈希的特性, 向回找是O(1)的, 所以总时间复杂度为O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int)->List[int]:
        h = {}
        for i in range(len(nums)):
            v = target-nums[i]
            if v in h:
                return [h[v], i]
            h[nums[i]] = i


s = Solution()
print(s.twoSum([1, 2, 2, 3, 4], 4))