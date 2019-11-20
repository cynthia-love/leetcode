# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, k数和通用方法, 第一种思路, 一个一个减
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def rf(nums, target, k):
            ans = []
            if k == 1:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    if nums[i] == target:
                        ans += [[nums[i]]]
                return ans

            if k == 2:
                l, r = 0, len(nums)-1
                if nums[l]+nums[l+1] > target:
                    return ans
                if nums[r]+nums[r-1] < target:
                    return ans

                while l < r:
                    if l > 0 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    if r < len(nums)-1 and nums[r] == nums[r+1]:
                        r -= 1
                        continue

                    if nums[l]+nums[r] == target:
                        ans += [[nums[l], nums[r]]]
                        l, r = l+1, r-1
                    elif nums[l]+nums[r] < target:
                        l += 1
                    else:
                        r -= 1
                return ans

            for i in range(len(nums)-(k-1)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                ts = rf(nums[i+1:], target-nums[i], k-1)
                ans += [[nums[i]]+x for x in ts]

            return ans

        nums.sort()
        print(nums)
        return rf(nums, target, 1)


s = Solution()
print(s.fourSum([-5,5,4,-3,0,0,4,-2], 4))

