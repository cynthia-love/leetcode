# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    希尔排序, 又称递减增量插入排序, 比如:
    [10, 7, 8, 9, 1, 5]
    先10和9, 7和1, 8和5分别插入排序, 变成9 1 5 10 7 8
    然后9和5和7, 1和10和8分别插入排序, 变成5 1 7 8 9 10
    然后就是普通的增量为1的插入排序了
    当然, 这里递减不一定按1递减, 也可以每次砍一半
"""
"""
    希尔排序, 递归形式
"""
from typing import List


class Solution:

    def shell_sort(self, arr: List[int]) -> List[int]:

        # 相对于普通插入排序, 整体写法没太大差异, 还是从第一个待插入元素往右遍历
        # 只不过在往前找有序部分的时候, 不是-1, 而是-gap
        # 这种思路会比强行分拆子数组更简单直接
        def rf(arr: List[int], gap: int, index: int):
            if index > len(arr)-1:
                return

            target, pos = arr[index], index

            while pos-gap >= 0 and arr[pos-gap] > target:
                arr[pos], pos = arr[pos-gap], pos-gap
            arr[pos] = target

            rf(arr, gap, index+1)

        ans = arr.copy()
        gap = int(len(arr)/2)
        while gap >= 1:
            rf(ans, gap, gap)
            gap = int(gap/2)

        return ans


s = Solution()
print(s.shell_sort([10, 7, 8, 9, 1, 5]))
