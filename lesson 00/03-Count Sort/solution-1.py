# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    计数排序, 待排序内容必须能通过统一公式转化为确定范围的整数
    比如待排序内容范围97-122,  可以通过减97进一步转化到0-25
    时间复杂度O(n), 拿空间换时间
    举例: 3 4 4 5, 生成数组为: 1 2 1, 2表示4映射到的索引1数量为2
"""
from typing import List


class Solution:
    def count_sort(self, arr: List[int])->List[int]:

        max_v , min_v = max(arr), min(arr)
        cs = [0]*(max_v-min_v+1)

        # 比如5映射到0, 每遇到一次5, cs[0]+=1
        for i in arr:
            cs[i-min_v] += 1

        ans = []
        for i in range(len(cs)):
            for j in range(cs[i]):
                # 索引i出现j次, 拼结果的时候还要将i转回原值
                ans.append(i+min_v)

        return ans


s = Solution()
print(s.count_sort([12, 11, 13, 5, 6, 7, 7]))
