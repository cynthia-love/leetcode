# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    选择排序, 每次从数组剩余部分中选一个最小的加到前面的有序数组后面
    [10, 7, 8, 9, 1, 5], 遍历找到最小index, 和0号位互换
"""
"""
    选择排序, 递归形式
"""
from typing import List


class Solution:

    def selection_sort(self, arr: List[int]) -> List[int]:

        def rf(arr: List[int], left: int):

            # 递归退出条件, 数组只有一个元素
            if left >= len(arr)-1:
                return

            min_i = left
            for i in range(left+1, len(arr)):
                if arr[i] < arr[min_i]:
                    min_i = i

            arr[left], arr[min_i] = arr[min_i], arr[left]

            rf(arr, left+1)

        ans = arr.copy()
        rf(ans, 0)
        return ans


s = Solution()
print(s.selection_sort([10, 7, 8, 9, 1, 5]))
