# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    题目分析: 升序数组找到目标值的第一个索引和最后一个索引, 要求O(log n), 找不到返回[-1, -1]
    看到log n, 不能直接左右线性遍历, 不用想了, 递归分治
    区别无非是找到后继续找向前向后遍历, 直到找到最左索引最右索引
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def rf(left, right):
            if left > right: return [-1, -1]
            mid = int((left+right)/2)

            if nums[mid] == target:
                # 找到目标值后, 直接向左向右遍历, 会比继续递归左右快个100ms吧
                p, q = mid, mid
                while p-1 >= 0 and nums[p-1] == target:
                    p -= 1
                while q+1 <= len(nums)-1 and nums[q+1] == target:
                    q += 1
                return [p, q]
            elif nums[mid] > target:
                return rf(left, mid-1)
            else:
                return rf(mid+1, right)

        return rf(0, len(nums)-1)


s = Solution()
print(s.searchRange([5, 6, 7, 8, 8, 10], 8))
