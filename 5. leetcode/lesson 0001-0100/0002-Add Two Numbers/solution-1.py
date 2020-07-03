# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 链表存储的数字相加, 双指针即可, 同时记录上一次相加的进位
    例如: 2->4->3     5->6->4->7
    注意不同长以及最后的进位等特殊情况
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode)->ListNode:
        # 加个头节点, 便于后续处理
        ans = ListNode(0)

        p, q, pos, flag = l1, l2, ans, 0

        # 先把同样长度的部分加完
        while p and q:

            sums = p.val+q.val+flag
            val, flag = int(sums % 10), int(sums // 10)

            # 注意有先后赋值顺序的语句不能写到一行
            pos.next = ListNode(val)
            pos, p, q = pos.next, p.next, q.next

        # 再加长的那个剩余部分
        left = p if p else q
        while left:
            sums = left.val+flag
            val, flag = int(sums % 10), int(sums // 10)

            pos.next = ListNode(val)
            pos, left = pos.next, left.next

        # 注意, 还可能有最后一个进位
        if flag == 1:
            pos.next = ListNode(1)

        # 返回的时候把头结点去掉
        return ans.next


l1 = ListNode(5)
l2 = ListNode(5)

s = Solution()
print(s.addTwoNumbers(l1, l2))
