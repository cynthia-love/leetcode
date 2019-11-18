# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 双指针, 实质就是在移动的过程中不断消去不可能成为最大值的状态

    受方法1启发, 左边界右移必须找大于原高度的才有可能容量增加, 其实右边界也一样
    leetcode上给的解法是每次移动1, 之后算面积, 再比较左右, 短的那侧再移动1

    感觉这里是可以继续优化的, 没必要每次移动1造成很多不必要的计算ans
    比如左侧之前最高8, 那么右移得找到比这个8大的才有意义, 不然肯定不如选8这个边界
    稍微快了一点, 效果有限, 毕竟都是O(n)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans, lmax, rmax = 0, len(height)-1, 0, 0, 0

        while l < r:
            ans = max(ans, min(height[l], height[r])*(r-l))
            lmax, rmax = max(lmax, height[l]), max(rmax, height[r])

            if height[l] < height[r]:
                while l < r and height[l] <= lmax:
                    l += 1
            else:
                while r > l and height[r] <= rmax:
                    r -= 1

        return ans


s = Solution()
print(s.maxArea([1, 8, 6]))
