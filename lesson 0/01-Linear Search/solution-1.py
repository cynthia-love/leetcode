# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    最基础的查找算法, 按一定顺序检查数组中的每一个元素,直到找到特定值为止
"""


class Solution:

    def linear_search(self, arr: list, target)->int:
        for i in range(len(arr)):
            # 搜索过程中找到目标值就返回其索引
            if arr[i] == target:
                return i
        # 所有值都不满足要求, 返回-1
        return -1


s = Solution()
print(s.linear_search(['A', 'B', 'C', 'D', 'E'], '1'))
