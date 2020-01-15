# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 要求时间复杂度 O(log (m+n)), 自然想到二分法
    思路:
    1. 假设nums1的长度为len1, nums2的长度为len2, 那么找中位数问题可以转化为找第k个值
    (1) nums1+nums2为奇数, 找第int((len1+len2+1)/2)个
    (2) nums1+nums2位偶数, 找第int((len1+len2)/2)个和第int((len1+len2+2)/2)
    2. 由于num1和num2都是有序的, 考虑最一般情况, 找到的值位于nums1的第x个, 且x小于k,那么
    nums2的第k-x个元素,和nums1的第k个元素,实际上构成了一个分界线, 左边一共k个值, 且左边最
    大小于右边最小
    3. nums1分界线可以从第一个元素递增1遍历, 也可以从中间二分遍历; 二分符合O(log (m+n))要求
    4. 题目描述nums1和nums2不会同时为空, 建议把nums1选为较短的那个, 一是二分搜索快, 二是
    需要考虑的特殊边界情况更少一些.

"""
"""
    二分法, 递归形式
"""
from typing import List
from math import floor

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findK(nums1, nums2, k):
            def rf(nums1, nums2, l, r, k):

                # 然后计算x1的值, 注意用floor不要用int, 使边界能移到nums1最左
                # 因为是左归属, 对于边界最右的情况, 计算出来的x1不会超限, 不用特殊处理
                x1 = floor((l+r)/2)
                x2 = k-x1-2
                # 注意, 算出来索引位置x2后还要处理x2的边界情况
                # 情况1, x2 < 0-1, 说明nums1中包含元素过多,要左移
                if x2 < -1:
                    return rf(nums1, nums2, l, x1-1, k)
                # 情况2, x2 > len(nums2)-1+1, 说明nums1中元素不够
                if x2 > len(nums2):
                    return rf(nums1, nums2, x1+1, r, k)
                # 计算四个边界值, 看是否满足左边始终大于右边
                # 计算的时候注意考虑, 采用的是左归属
                l1 = nums1[x1] if x1 in range(len(nums1)) else float('-inf')
                r1 = nums1[x1+1] if x1+1 in range(len(nums1)) else float('inf')
                l2 = nums2[x2] if x2 in range(len(nums2)) else float('-inf')
                r2 = nums2[x2+1] if x2+1 in range(len(nums2)) else float('inf')
                if l1 <= r2 and l2 <= r1:
                    return max(l1, l2)
                if l1 > r2:
                    return rf(nums1, nums2, l, x1-1, k)
                else:
                    return rf(nums1, nums2, x1+1, r, k)

            # 把nums1替换为短的那个, 有利于减少特殊逻辑分支, 且减少二分次数
            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1

            # 处理nums1为空的情况, 没必要带入递归
            if not nums1:
                return nums2[k-1]
            else:
                return rf(nums1, nums2, 0, len(nums1)-1, k)

        lens = len(nums1)+len(nums2)
        k1 = findK(nums1, nums2, int((lens+1)/2))
        k2 = findK(nums1, nums2, int((lens+2)/2)) if lens % 2 == 0 else k1
        return float((k1+k2)/2)


s = Solution()
print(s.findMedianSortedArrays([3], [-2, -1]))