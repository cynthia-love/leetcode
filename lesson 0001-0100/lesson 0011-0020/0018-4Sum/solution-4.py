# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, k数和通用方法, 第一种思路, 一个一个减
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        def rf(nums, target, k):
            print(nums)
            ans = []

            if k == 1:
                return [[i] for i, v in enumerate(nums) if v == target]

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                ts = rf(nums[i:], target-nums[i], k-1)
                ans += [[i]+x for x in ts]


            return ans

        return rf(nums, target, 4)



s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))

