# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 1, 2, 3->1, 3, 2; 即重排序各个数字, 排完之后是其所有排列的下一个大的数字
    如果已经是最大3, 2, 1; 则变成1, 2, 3
    要求, 替换必须是in-place且空间复杂度为常数
    观察: 1 2 3 4 5-> 1 2 3 5 4-> 1 2 4 3 5-> 1 2 4 5 3
    4 5变5 4, 此时想找下一个必须扩展到3位考虑3 5 4, 此时除去3的位置已经是倒序最大, 想找
    下一个得从5 4里找一个刚好大于3的数和3互换, 4 5 3, 由于百位变大了一个值, 剩余部分得变成
    从小到大; 本身5 4就是降序, 4刚好大于3, 说明左边大于3右边小于3, 所以排序不用全排, 倒序就行
    同样道理, 4 3 5->4 5 3->5 3 4, 注意扩展到3位后还会再回去考虑两位的
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 由于频繁用到倒序, 需要先写一个翻转函数
        def reverse(nums: List[int], start: int, end: int):
            # 1 2 3 4 5 变 5 4 3 2 1, 直接改原数组, 左右俩指针互换即可
            p, q = start, end
            while p < q:
                nums[p], nums[q] = nums[q], nums[p]
                p, q = p+1, q-1

        # 找到右边降序部分的左分界线
        p = len(nums)-1
        while p >= 1 and nums[p] <= nums[p-1]: p -= 1
        if p == 0: reverse(nums, 0, len(nums)-1); return

        # 找到p位置后, 右边倒序部分为从p到len(nums)-1, 此时需要从倒序部分找到一个刚好大于p-1位置
        q = len(nums)-1
        while nums[q] <= nums[p-1]: q -= 1
        nums[p-1], nums[q] = nums[q], nums[p-1]

        # 互换后, 把右侧倒序部分翻转
        reverse(nums, p, len(nums)-1)


s = Solution()
print(s.nextPermutation([1, 2, 3]))
