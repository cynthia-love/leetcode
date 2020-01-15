# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析:　两个有序数组, 找到其中位数; 不同时为空; 要求时间复杂度O(log (m+n))

"""
"""
    方法1, 归并成一个, 但是时间复杂度为O(m+n), 不符合要求
"""
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lm, i, j, k = [0]*(len(nums1)+len(nums2)), 0, 0, 0

        while nums1[i:] and nums2[j:]:
            if nums1[i] < nums2[j]:
                lm[k], i, k = nums1[i], i+1, k+1
            else:
                lm[k], j, k = nums2[j], j+1, k+1

        # 这里注意, 不能根据原数组长短判断哪个先到头
        while nums1[i:]:
            lm[k], i, k = nums1[i], i+1, k+1
        while nums2[j:]:
            lm[k], j, k = nums2[j], j+1, k+1

        # 分长度为奇数, 偶数不同情况考虑
        # 虽然这俩可以合并为一句, 但逻辑上不好理解, 没必要
        if len(lm) % 2 == 1:
            return float(lm[int(len(lm)/2)])
        else:
            return float((lm[int(len(lm)/2)-1]+lm[int(len(lm)/2)])/2)


s = Solution()
print(s.findMedianSortedArrays([1], [1]))
