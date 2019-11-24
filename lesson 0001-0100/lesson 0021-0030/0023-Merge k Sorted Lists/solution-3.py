# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 22归并, 非递归
    利用双端队列, 先全放进去, 再取俩, 合并完放到最后, 以此类推
"""
from typing import List
from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None

        d = deque()
        for l in lists:
            d.append(l)

        while len(d) > 1:
            l1 = d.popleft()
            l2 = d.popleft()
            pos = ans = ListNode(-1)
            p, q = l1, l2
            while p and q:
                if p.val < q.val:
                    pos.next, pos, p = p, p, p.next
                else:
                    pos.next, pos, q = q, q, q.next
            p = p if p else q
            pos.next = p
            d.append(ans.next)
        ans = d.popleft()
        return ans


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