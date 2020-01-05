# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 1, 2, 3->1, 3, 2; 即重排序各个数字, 排完之后是其所有排列的下一个大的数字
    如果已经是最大3, 2, 1; 则变成1, 2, 3
    要求, 替换必须是in-place且空间复杂度为常数
    观察: 1 2 3 4 | 5->1 2 3 | 5 4-> 1 2 4 3 | 5->1 2 4 | 5 3->1 2 5 3 | 4->1 2 | 5 4 3
    ->1 3 2 4 5->1 3 2 5 4->1 3 5 2 4->1 3 | 5 4 2-> 1 4 2 3 5
    规律是? 找到第一个左小于右的分界线, 比如3-5 4, 右边找到最小的大于3的值和3互换, 4-5 3
    然后右侧重新按从小到大排序; 极端情况是 | 5 4 3 2 1, 没的换, 直接从小到大排序
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], start: int, end: int):
            # 1 2 3 4 变 4 3 2 1
            p, q = start, end
            while p < q:
                nums[p], nums[q] = nums[q], nums[p]
                p, q = p + 1, q - 1

        p = len(nums)-1
        # 找到第一个左小于右的分界线
        while p >= 1 and nums[p-1] >= nums[p]: p -= 1
        if p == 0: reverse(nums, 0, len(nums)-1)
        else:
            # 找到分界线右边最小的大于分界线左值的位置; 由于右侧是递减, 从最小的开始找
            for i in range(len(nums) - 1, p - 1, -1):
                if nums[i] > nums[p - 1]:
                    nums[i], nums[p - 1] = nums[p - 1], nums[i]
                    break

            reverse(nums, p, len(nums) - 1)


s = Solution()
print(s.nextPermutation([3, 2, 1]))
