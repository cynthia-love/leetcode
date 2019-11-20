# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 注意偶数个sum的特殊性, 4sum意味着, 2次遍历能拿到所有的2sum组合
    用数据结构存储所有2sum可能性, 注意value里是索引而非值, 值没法区分有没有重复元素:
    {
        -1:[(0, 2), (1, 3)]
        1:[(1, 4), (2, 5)]
    }
"""

from typing import List
from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        h = defaultdict(list)

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                h[target-nums[i]-nums[j]].append((i, j))

        ans, h2 = set(), set()
        for k, v in h.items():
            # 处理1+1这种情况
            if k*2 == target and len(v) >= 2:
                for i in range(len(v)-1):
                    for j in range(i+1, len(v)):
                        s = set(v[i]+v[j])
                        # 保证是四个不同位置的元素
                        if len(s) == 4:
                            l = [nums[x] for x in s]
                            l.sort()
                            ans.add(tuple(l))

            if target-k in h2:
                # 处理1+2的情况
                l = [x+y for x in v for y in h[target-k] if len(set(x+y)) == 4]
                l = [sorted([nums[x] for x in y]) for y in l]
                for t in l: ans.add(tuple(t))

            h2.add(k)

        return [list(t) for t in ans]


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))