# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 22归并, 递归
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def rf(left=0, right=len(lists)-1):

            if left == right:
                return lists[left]

            mid = int((left+right)/2)
            l1, l2 = rf(left, mid), rf(mid+1, right)

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
        return rf() if lists else None


s = Solution()
x1 = ListNode(1)
x1.next = ListNode(2)
x1.next.next = ListNode(4)
x2 = ListNode(2)
x2.next = ListNode(2)
x2.next.next = ListNode(4)

x3 = ListNode(2)
x3.next = ListNode(2)
x3.next.next = ListNode(4)

ans = s.mergeKLists([x1, x2, x3])

while ans:
    print(ans.val, end="")
    ans = ans.next