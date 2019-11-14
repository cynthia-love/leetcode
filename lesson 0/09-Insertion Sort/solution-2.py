# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    插入排序, 非递归形式
"""
from typing import List


class Solution:
    
    def insertion_sort(self, arr: List[int]) -> List[int]:
        
        ans = arr.copy()
        # 最外层控制待插入的元素的索引, 从1开始
        for i in range(1, len(ans)):
            
            target, pos = ans[i], i
            while pos-1 >= 0 and ans[pos-1] > target:
                ans[pos], pos = ans[pos-1], pos-1
            ans[pos] = target
        
        return ans


s = Solution()
print(s.insertion_sort([10, 7, 8, 9, 1, 5]))
