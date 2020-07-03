# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法1, 外层双循环, 内层双指针
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []

        nums.sort()

        for i in range(0, len(nums)-3):
            # 四个数都跳过已处理过的值, 那么ans就不用去重了
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                l, r, t2 = j+1, len(nums)-1, target-nums[i]-nums[j]

                while l < r:

                    if l > j+1 and nums[l] == nums[l-1]:
                        l += 1
                        continue

                    if r < len(nums)-1 and nums[r] == nums[r+1]:
                        r -= 1
                        continue

                    if nums[l]+nums[l+1] > t2: break
                    if nums[r]+nums[r-1] < t2: break

                    if nums[l]+nums[r] == t2:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l, r = l+1, r-1
                        continue

                    if nums[l]+nums[r] < t2:
                        l += 1
                    else:
                        r -= 1
        return ans


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))