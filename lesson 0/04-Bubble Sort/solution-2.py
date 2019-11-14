# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    冒泡排序, 非递归形式
"""
from typing import List


class Solution:

    def bubble_sort(self, arr: List[int]):
        ans = arr.copy()

        # 外层控制冒泡次数, n个元素排n-1次就够
        for i in range(1, len(ans)):
            # 第1次排遍历到第n-1个元素, 第二次n-2
            for j in range(len(ans)-i):
                if ans[j] > ans[j+1]:
                    ans[j], ans[j+1] = ans[j+1], ans[j]

        return ans


s = Solution()
print(s.bubble_sort([64, 34, 25, 12, 22, 11, 90]))