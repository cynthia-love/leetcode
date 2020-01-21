# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    方法2, 思路不变, 非递归形式
    非递归没法并行分治, 所以找到值后直接向左向右遍历
    和递归相比, 好像没啥变化, 还是90ms左右
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, p, q = 0, len(nums)-1, -1, -1

        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                left += 1
            else:
                p, q = mid, mid
                while p-1 >= 0 and nums[p-1] == target:
                    p -= 1
                while q+1 <= len(nums)-1 and nums[q+1] == target:
                    q += 1
                break
        return [p, q]


s = Solution()
print(s.searchRange([5, 6, 7, 8, 8, 10], 8))
