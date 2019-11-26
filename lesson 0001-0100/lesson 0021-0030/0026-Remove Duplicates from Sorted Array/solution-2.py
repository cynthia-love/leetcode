# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法1的优化
    猛一看, 似乎没有优化的空间
    [1, 2, 2, 2, 3, 4]
    对于这种, 是没有, 但是对于[1, 2, 3, 4, 5]这种, 有
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        p = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                p = p+1
                if p != i: nums[p] = nums[i]

        return p+1


s = Solution()
print(s.removeDuplicates([1, 1, 2, 2, 2, 3]))