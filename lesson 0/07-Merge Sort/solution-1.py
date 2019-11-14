# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    归并排序, 先排前半部分和后半部分, 然后合并俩有序数组
    同快速排序, 递归排序好像也只有递归写法
"""
from typing import List


class Solution:

    def merge_sort(self, arr: List[int]) -> List[int]:

        def rf(arr: List[int], left: int, right: int):
            # 单个元素为递归退出条件
            if left >= right:
                return

            mid = int((left+right)/2)
            rf(arr, left, mid)
            rf(arr, mid+1, right)

            # 前后半部分排好序后这里要借助中间数组
            ll = arr[left:mid+1].copy()
            lr = arr[mid+1: right+1].copy()
            p, q = 0, 0
            # 归并的时候, 可以以arr为参考点, 下面
            # 这种写法主要基于len(arr) = len(ll)+len(lr)
            """
            for i in range(left, right+1):
                if q > len(lr)-1 or ll[p] <= lr[q]:
                    arr[i], p = ll[p], p+1
                else:
                    arr[i], q = lr[q], q+1
            """
            # 第二种归并方式, 以ll, lr为参考点
            p, q, index = 0, 0, left
            while p <= len(ll)-1 and q <= len(lr)-1:
                if ll[p] <= lr[q]:
                    arr[index], p, index = ll[p], p+1, index+1
                else:
                    arr[index], q, index = lr[q], q+1, index+1
            # 循环退出后, 拼接ll或lr的剩余部分
            if p > len(ll)-1:
                while q <= len(lr)-1:
                    arr[index], q, index = lr[q], q+1, index+1
            else:
                while p <= len(ll)-1:
                    arr[index], p, index = ll[p], p+1, index+1

        ans = arr.copy()
        rf(ans, 0, len(ans)-1)
        return ans


s = Solution()
print(s.merge_sort([10, 7, 8, 9, 1, 5]))