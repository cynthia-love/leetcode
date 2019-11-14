# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    二分法, 非递归形式
    注意, 不是所有的递归都有非递归形式, 只有单项递归才有. 比如二分查找, 每次二分后只会选一边继续,
    而像是归并排序这种, 每次要同时递归左半部分和右半部分, 就无法写出非递归形式了
"""
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findK(nums1, nums2, k):

            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1

            if not nums1:
                return nums2[k - 1]

            # 这里一定要想清楚查找目标索引的范围
            # 因为边界线采用左归属, 比如nums1长度3, 那么目标索引范围: -1, 0, 1, 2
            l, r = -1, len(nums1)-1  # 考虑下为什么l初始化为-1, 这么逻辑最简单

            while l <= r:
                x1 = int((l+r)/2)
                x2 = k-x1-2

                # 如果nums2超过了最左边界-1, 说明nums1选多了
                if x2 < -1:
                    r = x1-1
                    continue
                # 如果nums2超过了最右边界len(num2)-1, 说明nums1选少了
                if x2 > len(nums2)-1:
                    l = x1+1
                    continue

                l1 = nums1[x1] if x1 in range(len(nums1)) else float('-inf')
                r1 = nums1[x1+1] if x1+1 in range(len(nums1)) else float('inf')
                l2 = nums2[x2] if x2 in range(len(nums2)) else float('-inf')
                r2 = nums2[x2+1] if x2+1 in range(len(nums2)) else float('inf')

                if l1 <= r2 and l2 <= r1:
                    return max(l1, l2)
                if l1 > r2:
                    r = x1-1
                else:
                    l = x1+1

        lens = len(nums1)+len(nums2)
        k1 = findK(nums1, nums2, int((lens+1)/2))
        k2 = findK(nums1, nums2, int((lens+2)/2)) if lens % 2 == 0 else k1

        return float((k1+k2)/2)


s = Solution()
print(s.findMedianSortedArrays([1], [1, 2, 3]))
