# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析, 四数相加等于target, 去重
"""
"""
    方法1, 外层俩循环, 中间用hash做2sum; 貌似除了2数和, hash表现并不好, 越多数和hash表现越不好
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, h1 = set(), set()
        for i in range(len(nums)-3):
            if nums[i] in h1: continue
            h1.add(nums[i])

            h2 = set()
            for j in range(i+1, len(nums)-2):
                if nums[j] in h2: continue
                h2.add(nums[j])

                h3 = set()
                for k in range(j+1, len(nums)):
                    num4 = target-nums[i]-nums[j]-nums[k]
                    if num4 in h3:
                        l = [nums[i], nums[j], nums[k], num4]
                        l.sort()
                        ans.add(tuple(l))
                    h3.add(nums[k])

        return [list(i) for i in ans]


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))