# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法5, 外层不用递归, 内层用尾插

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:




x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)
x.next.next.next.next = ListNode(5)
s = Solution()
a = s.reverseKGroup(x, 3)
while a:
    print(a.val, end=" ")
    a = a.next
print()


