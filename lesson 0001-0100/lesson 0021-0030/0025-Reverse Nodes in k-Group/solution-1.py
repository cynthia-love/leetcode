# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 链表翻转, 不是每2个, 而是每k个, 不足k的部分不翻转
"""
from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def rf(head: ListNode = head):
            dq, c, h = deque(), 0, head

            while h and c < k:
                dq.append(h)
                h, c = h.next, c+1

            if c < k: return head

            pos = ans = dq.pop()
            # 1->2->3-4, 比如k=2, 这里先pop出来2之后
            # 由于后面会改变其next指向, 所以这里记得把指向3的指针存一下
            remains = pos.next

            while dq:
                pos.next = dq.pop()
                pos = pos.next
            pos.next = rf(remains)

            return ans

        return rf()


x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)
s = Solution()
a = s.reverseKGroup(x, 2)
while a:
    print(a.val, end=" ")
    a = a.next