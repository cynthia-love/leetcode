# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, k数和通用方法, 第一种思路, 一个一个减
    另外, 个别题目要索引, 所以递归先返回索引, 拿到最终值再转值, 这么写更通用
    实际上不要索引的话, 可以不要index参数, 用nums[i+1:]方式传参
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        def rf(nums, index, target, k):

            ans, size = [], len(nums)
            if k == 1:
                for i in range(index, size):
                    if i > index and nums[i] == nums[i-1]:
                        continue
                    if nums[i] == target:
                        ans += [[i]]
                return ans

            if k == 2:

                l, r = index, size-1
                if nums[l]+nums[l+1] > target:
                    return []
                if nums[r]+nums[r-1] < target:
                    return []

                while l < r:
                    if l > index and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    if r < size-1 and nums[r] == nums[r+1]:
                        r -= 1
                        continue

                    if nums[l]+nums[r] == target:
                        ans += [[l, r]]
                        l, r = l+1, r-1
                    elif nums[l]+nums[r] < target:
                        l += 1
                    else:
                        r -= 1
                return ans

            for i in range(index, size-(k-1)):
                # 每一层的遍历都跳过本层已处理过的值
                # 这样最终获得的ans不需要去重
                if i > index and nums[i] == nums[i-1]:
                    continue

                ts = rf(nums, i+1, target-nums[i], k-1)
                ans += [[i]+x for x in ts]

            return ans

        nums.sort()
        ans = rf(nums, 0, target, 4)
        return [[nums[x] for x in y] for y in ans]


s = Solution()
print(s.fourSum([0, 0, 0, 0], 0))

