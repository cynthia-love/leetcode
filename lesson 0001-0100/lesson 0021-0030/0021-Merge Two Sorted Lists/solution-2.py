# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 非递归, 且不开辟新的链表空间
"""


class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        pos = ans = ListNode(-1)

        p, q = l1, l2

        while p and q:

            if p.val < q.val:
                pos.next, pos, p = p, p, p.next
            else:
                pos.next, pos, q = q, q, q.next

        p = q if not p else p
        pos.next = p
        return ans.next


s = Solution()
x1 = ListNode(1)
x1.next = ListNode(2)
x1.next.next = ListNode(4)
x2 = ListNode(2)
x2.next = ListNode(2)
x2.next.next = ListNode(4)

ans = s.mergeTwoLists(x1, x2)

while ans:
    print(ans.val, end="")
    ans = ans.next