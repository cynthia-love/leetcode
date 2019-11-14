# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    堆排序， 非递归形式
"""
from typing import List


class Solution:

    def heap_sort(self, arr: List[int]) -> List[int]:

        ans = arr.copy()

        # 从n-1位置开始进行堆调整，每次出来一个根最大和末位交换, 一直到1结束
        for i in range(len(ans)-1, 0, -1):
            # 计算最后一个非叶节点的索引
            last_parent = int((i-1)/2)
            # 单次调整需要遍历到第一个非叶节点, 即根节点
            # solution-1这里用了while循环, 都行, 不过建议固定步长的用for吧
            for j in range(last_parent, -1, -1):
                left, right = j*2+1, j*2+2
                if right <= i and ans[j] < ans[right]:
                    ans[j], ans[right] = ans[right], ans[j]
                if ans[j] < ans[left]:
                    ans[j], ans[left] = ans[left], ans[j]
            # 单次调整完毕, 交换0号位和i号位, 然后i-1
            ans[0], ans[i] = ans[i], ans[0]

        return ans


s = Solution()
print(s.heap_sort([12, 11, 13, 5, 6, 7]))