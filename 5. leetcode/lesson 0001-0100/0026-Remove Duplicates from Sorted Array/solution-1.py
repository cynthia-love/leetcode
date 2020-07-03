# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析, 有序数组去重, 要求空间复杂度O(1)
    比如[1, 1, 2], 去重后变成[1, 2, *], 返回长度2
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        pos = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                pos, nums[pos] = pos+1, nums[i]

        return pos+1


s = Solution()
print(s.removeDuplicates([1, 1, 2, 2, 2, 3]))
