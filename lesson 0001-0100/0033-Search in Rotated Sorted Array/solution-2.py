# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    思路不变, [7,8,9,10,0,1 | 2,3,4,5,6]
    0. 中间位置恰好是target, 直接返回
    1. 递归左边的条件1, 升序, left <= target < middle, 其中left < middle用于确定是升序
    2. 递归左边的条件2, 循环, middle < left <= target(位于7-10部分), 或者 target < middle <left(位于0-1部分)
    3. 其他情况, 递归右边
"""
"""
    方法2, 非递归形式
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            m = int((l+r)/2)
            # 中间匹配上, 提前终止
            if nums[m] == target: return m
            # 左边匹配上, 提前终止
            if nums[l] == target: return l
            """
            看到一个神仙写法, 三个异或, 尝试理解下
            首先, 异或的概念, 两项异或, A xor B, 都为真或都为假时结果为假; 一真一假或一假一真时结果为真
            三项, 真真真, 假假真, 结果为真(奇数个真); 其他情况, 假假假, 假真真, 结果为假; 一共就四种情况
            假定三个条件分别为nums[l] > target, target > nums[m], nums[m] > nums[l], 显然, 不可能同时为真
            下面这句if相当于: 假 假 真 or 假 真 假 or 真 假 假, 即异或的三种情况; 也就是说:
            A xor B xor C 等价于 (A and B and C) or (not A and not B and C) or (not A and B and not C) or (A and not B and not C) 
            if nums[l] < target < nums[m] or nums[m] < nums[l] < target or target < nums[m] < nums[l]: r = m-1
            其实没必要, 有点过于强行增加理解难度了
            """
            if (nums[l] > target) ^ (target > nums[m]) ^ (nums[m] >= nums[l]): r = m-1
            else: l = m+1
        return -1


s = Solution()
print(s.search([1, 3], 3))