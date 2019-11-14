# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    二分查找, 非递归形式
"""


class Solution:

    def binary_search(self, arr: list, target)->int:

        left, right = 0, len(arr)-1

        # 注意, 只剩一个元素时还得继续比较,所以这里是<=而不是<
        while left <= right:
            mid = int((left+right)/2)
            # 找到直接返回
            if arr[mid] == target:
                return mid
            # 中间值大了, 继续去左半部分查找
            if arr[mid] > target:
                right = mid-1
            # 中间值小了, 继续去右半部分查找
            else:
                left = mid+1

        return -1


s = Solution()
print(s.binary_search([2, 3, 4, 10, 40], 0))
