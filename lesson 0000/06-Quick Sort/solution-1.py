# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    快速排序, 每次找到一个值的位置, 使数组前半部分小于它, 后半部分大于它; 重复此操作
    归并排序, 前半部分排序, 后半部分排序, 然后合并前半部分后半部分. 这俩有点思路上的类似.
    这两种排序好像只有递归写法.
"""
from typing import List


class Solution:
    def quick_sort(self, arr: List[int]):
        ans = arr.copy()

        def rf(arr: List[int], left: int, right: int):
            # 递归退出条件, 小于等于一个元素
            if left >= right: return
            mid = int((left+right)/2)
            # 交换中间元素和首元素以兼容有序1 2 3 4 6->3 2 1 4 6
            arr[left], arr[mid] = arr[mid], arr[left]

            value = arr[left] # 挖第一个坑

            l, r = left, right
            while l < r:
                # 先填左边的坑
                while r > l and arr[r] >= value:
                    r -= 1
                arr[l] = arr[r]
                # 再填右边的坑
                while l < r and arr[l] <= value:
                    l += 1
                arr[r] = arr[l]
            arr[l] = value
            # 先找到一个值的位置, 然后排前面, 后面
            # 而归并则是先排前面, 后面, 再归并
            rf(arr, left, l-1)
            rf(arr, l+1, right)

        rf(ans, 0, len(ans)-1)
        return ans


s = Solution()
print(s.quick_sort([10, 7, 8, 9, 1, 5]))
