# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    二分查找, 一种在有序数组中查找元素的算法, 每次比较中间值: 相等则返回; 大于则继续
    在左半部分查找, 小于则继续在右半部分查找.
"""
"""
    二分查找, 递归形式
"""


class Solution:

    def binary_search(self, arr: list, target)->int:
        # 定义递归函数体
        def rf(arr: list, left: int, right: int, target):
            # 递归终止条件, 待查找数组为空
            if left > right:
                return -1

            mid = int((left+right)/2)
            # 找到了直接返回
            if arr[mid] == target:
                return mid
            # 中间值大了, 递归查找左半部分
            if arr[mid] > target:
                return rf(arr, left, mid-1, target)
            # 中间值小了,递归查找右半部分
            else:
                return rf(arr, mid+1, right, target)

        return rf(arr, 0, len(arr)-1, target)


s = Solution()
print(s.binary_search([2, 3, 4, 20, 40], 20))
