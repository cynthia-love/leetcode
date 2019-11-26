# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析, 移除指定元素的值, 要求空间复杂度O(1); 移除后数组元素顺序不作要求
"""
"""
    方法1, 双指针
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0

        # 有一个指针稳定+1向后的, 不要用while, 用for更清晰
        # 一开始p指向0, 1不等于val变成1, 2不等于变成2, 所以最终return p即可
        p = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[p], p = nums[i], p+1

        return p


s = Solution()
print(s.removeElement([1, 2, 3, 3, -1, 2], 3))
