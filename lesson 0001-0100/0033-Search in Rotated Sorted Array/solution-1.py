# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: [7,8,9,10,0,1 | 2,3,4,5,6], 升序不重复数组, 但可能是循环的, 给定一个值找到返回索引, 找不到返回-1
    要求时间复杂度O(log n)

    log n, 典型的分治的复杂度, 无非是考虑的情况多了点

    比如这里找到中间点1(左归属), 通过与left位置比较, 可以知道左半部分是升序还是循环(只考虑左边就行, 不用管右边是什么)
    0. 中间位置恰好是target, 直接返回
    1. 递归左边的条件1, 升序, left <= target < middle, 其中left < middle用于确定是升序
    2. 递归左边的条件2, 循环, middle < left <= target(位于7-10部分), 或者 target < middle <left(位于0-1部分)
    3. 其他情况, 递归右边
"""
"""
    方法1, 递归形式
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binSearch(left, right):
            if left > right: return -1
            middle = int((left+right)/2)
            if nums[middle] == target: return middle
            if nums[left] == target: return left

            # 左半部分递增, target位于中间
            if nums[left] < target < nums[middle]: return binSearch(left, middle-1)
            # 左半部分循环, 789012, target位于789部分
            if nums[middle] < nums[left] < target: return binSearch(left, middle-1)
            # 左半部分循环, 789012, target位于012部分
            if target < nums[middle] < nums[left]: return binSearch(left, middle-1)

            return binSearch(middle+1, right)

        return binSearch(0, len(nums)-1)


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
