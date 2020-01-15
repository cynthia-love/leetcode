# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 递归
    能用dequeue的好像也能用递归, 比如归并排序
"""


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
        def rf(h=head):
            if not h or not h.next: return h
            # 1->2->剩余
            x, y, z = h, h.next, h.next.next
            y.next, x.next = x, rf(z)
            return y

        return rf()



x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)
s = Solution()
a = s.swapPairs(x)
while a:
    print(a.val, end=" ")
    a = a.next
