# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 双指针
    受方法1启发, 左边界右移必须找大于原高度的, 其实右边界也一样, 一次遍历O(n)
    每次移动短的那个(移动长的容量只会减不会增)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans, ml, mr = 0, len(height)-1, 0, height[0], height[len(height)-1]

        while l < r:
            print(l, r)
            ans = max(ans, min(height[l], height[r])*(r-l))
            if height[l] <= height[r]:
                while l+1 < r and height[l+1] <= ml:
                    l += 1
                ml = height[l]
            else:
                while r-1 > l and height[r-1] <= mr:
                    r -= 1
                mr = height[r]


        return ans


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
