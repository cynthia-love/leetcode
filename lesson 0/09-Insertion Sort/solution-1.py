# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    插入排序, 和选择排序有点类似, 只不过选择排序是每次从未排序部分选一个最小的放到头部(或者说前面有序
    部分的尾部), 而插入排序是随便选一个, 因为是随便选的, 不能直接加到有序部分的尾部, 而是要一点点往
    前找应插入的位置
"""
"""
    插入排序, 递归形式
"""
from typing import List


class Solution:

    def insertion_sort(self, arr: List[int]) -> List[int]:

        def rf(arr: List[int], left: int):  # 第二个参数为待插入的索引值

            # 已经没有待排序部分, 退出递归
            # 注意, 选择排序的退出条件是剩一个, 因为剩的肯定是最大的, 但插入排序不能剩
            # [10, 7, 8, 9, 1, 5]
            if left > len(arr)-1:
                return

            # 这里也可以两两交换, 但前半部分是有序的, 两两交换效率低
            target, pos = arr[left], left
            while pos-1 >= 0 and arr[pos-1] > target:
                arr[pos], pos = arr[pos-1], pos-1
            arr[pos] = target

            rf(arr, left+1)

        ans = arr.copy()
        rf(ans, 1)
        return ans


s = Solution()
print(s.insertion_sort([10, 7, 8, 9, 1, 5]))




