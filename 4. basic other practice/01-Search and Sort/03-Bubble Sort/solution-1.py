# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    最基本的排序算法, 每次冒一个最大的到右边,然后处理剩下的
    比如2 3 1 1, 两两比较, 2 3 1 1-> 2 1 3 1-> 2 1 1 3
    与选择排序的区别是, 选择排序先选出来一个大的, 和最后一个换
    而冒泡排序是一点一点冒上去的
"""
"""
    冒泡排序, 递归形式
"""
from typing import List


class Solution:
    def bubble_sort(self, arr: List[int]):
        ans = arr.copy()

        def rf(arr: List[int], r_index):
            # 思路, [1, 3, 2, 0]排序相当于确定了3位置后再排1 2 0
            if r_index <= 0: return
            for i in range(r_index):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]

            rf(arr, r_index-1)

        rf(ans, len(ans)-1)
        return ans


s = Solution()
print(s.bubble_sort([64, 34, 25, 12, 22, 11, 90]))