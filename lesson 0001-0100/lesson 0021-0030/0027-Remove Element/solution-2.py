# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 关键, "移除后数组元素顺序不作要求"
    主要是考虑 3 1 2 4 5 6, 3这种情况, 按方法1会有大量冗余赋值
    那么我们的目标就是尽可能不移动元素
    让1不动, 但删除3, 方法, 和6换, 数组长度减1
    变成: 6 1 2 4 5; 3
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        p, q = 0, len(nums)-1

        while p <= q:
            if nums[p] != val: p += 1
            else: nums[p], nums[q], q = nums[q], nums[p], q-1

        return p


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
