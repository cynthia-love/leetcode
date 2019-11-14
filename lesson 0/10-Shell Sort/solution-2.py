# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    希尔排序, 非递归形式
"""
from typing import List


class Solution:

    def shell_sort(self, arr: List[int]) -> List[int]:

        ans = arr.copy()
        gap = int(len(arr)/2)

        while gap >= 1:

            # 比如gap=1, 第一个待插入元素的索引为1
            for i in range(gap, len(ans)):

                target, pos = ans[i], i

                # 找到带插入元素应该在的位置
                while pos-gap >= 0 and ans[pos-gap] > target:
                    ans[pos], pos = ans[pos-gap], pos-gap
                ans[pos] = target

            # gap的递减可以-1, 也可以除以2, 不重要, 最后总会变成1
            gap = int(gap/2)

        return ans


s = Solution()
print(s.shell_sort([10, 7, 8, 9, 1, 5]))
