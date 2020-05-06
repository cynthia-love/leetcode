# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    选择排序, 非递归形式
"""
from typing import List


class Solution:

    def selection_sort(self, arr: List[int]) -> List[int]:

        ans = arr.copy()
        # 长度为n的数组, 0~n-1, 把0~n-2的都选出来就结束了
        for i in range(len(ans)-1):

            # 找到当前处理的部分的最小索引位置
            min_i = i
            for j in range(i+1, len(ans)):
                if ans[j] < ans[min_i]:
                    min_i = j

            ans[i], ans[min_i] = ans[min_i], ans[i]

        return ans


s = Solution()
print(s.selection_sort([10, 7, 8, 9, 1, 5]))
