# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 栈
"""
from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def pl(self, head: ListNode):
        while head:
            print(head.val, end=" ")
            head = head.next
        print("")

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        ans, dq = ListNode(-1), deque()
        pos = ans

        dq.append(head)
        dq.append(head.next)
        head = head.next.next

        while dq:
            if len(dq) == 1:
                pos.next = dq.pop()
            else:

                pos.next = dq.pop()
                pos = pos.next
                pos.next = dq.pop()
                pos = pos.next

                # 这个地方是个大坑啊, 不加这个None输出ans的时候会一直循环
                pos.next = None

                if head:
                    dq.append(head)
                    head = head.next
                if head:
                    dq.append(head)
                    head = head.next

        return ans.next


x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)
s = Solution()
a = s.swapPairs(x)
while a:
    print(a.val, end=" ")
    a = a.next
