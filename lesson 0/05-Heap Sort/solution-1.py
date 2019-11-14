# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    堆排序, 一种利用堆的概念进行的排序, 父节点总是>=或<=左右子节点
    根据完全二叉树的性质, 对于0 1 2 3 4 5 6 ... n:
    1. 最后一个非叶节点索引值为: int((n-1)/2)
    2. 索引n节点的左子节点索引为2n+1, 右子2n+2
    那么从最后一个非叶节点往前遍历一遍, 将最大/最小值浮到根节点
    注意, 冒泡排序一般是往最大索引浮, 而堆排序是往索引0浮
    之后交换索引0和最后一个元素, 一次浮动结束, 调整交换后的数组
    得到符合堆性质的根节点后,再和倒数第二个元素交换
"""
"""
    堆排序, 递归形式
"""
from typing import List


class Solution:
    def heap_sort(self, arr: List[int])->List[int]:
        ans = arr.copy()

        def rf(arr: List[int], last_index: int):
            # 递归退出条件
            if last_index <= 0: return
            # 找到最后一个非叶节点
            parent = int((last_index-1)/2)
            while parent >= 0:
                right = 2*parent+2
                left = 2*parent+1
                if right <= last_index and arr[parent] < arr[right]:
                    arr[parent], arr[right] = arr[right], arr[parent]
                if arr[parent] < arr[left]:
                    arr[parent], arr[left] = arr[left], arr[parent]
                parent -= 1
            # 交换根节点和数组最后一个元素
            arr[0], arr[last_index] = arr[last_index], arr[0]
            # 继续排序除掉最后一个元素的数组
            rf(arr, last_index-1)

        rf(ans, len(ans)-1)

        return ans


s = Solution()
print(s.heap_sort([12, 11, 13, 5, 6, 7]))

