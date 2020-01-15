# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析, 有序链表合并
"""
"""
    方法1, 非递归, 开辟新的链表空间
"""


class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1: return l2
        if not l2: return l1

        ans = ListNode(-1)

        p, q, pos = l1, l2, ans

        while p and q:

            if p.val < q.val:
                node = ListNode(p.val)
                pos.next = node
                p, pos = p.next, pos.next

            else:
                node = ListNode(q.val)
                pos.next = node
                q, pos = q.next, pos.next

        p = q if not p else p

        while p:
            node = ListNode(p.val)
            pos.next = node
            p, pos = p.next, pos.next

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


