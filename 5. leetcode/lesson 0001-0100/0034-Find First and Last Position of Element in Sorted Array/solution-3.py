# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    方法3, 方法1和方法2的递归分治和非递归分治多次运行还是在90ms左右徘徊
    看有没有办法进行极限优化
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def rf(left, right):
            if left > right: return [-1, -1]

            mid = int((left+right)/2)
            if nums[mid] < target:
                return rf(mid+1, right)
            elif nums[mid] > target:
                return rf(left, mid-1)
            else:
                # 情况1, 左边没有右边有
                # 情况2, 左边有, 右边没有
                # 情况3, 左右都有
                # 情况4, 左右都没有
                # 注意数组是有序的, 所以左右的肯定会往中间靠
                l = rf(left, mid-1)
                r = rf(mid+1, right)
                return [mid if sum(l) == -2 else l[1] if l[0] == -1 else l[0], mid if sum(r) == -2 else r[0] if r[1] == -1 else r[1]]

        return rf(0, len(nums)-1)

s = Solution()
print(s.searchRange([5, 6, 7, 8, 8, 10], 8))
