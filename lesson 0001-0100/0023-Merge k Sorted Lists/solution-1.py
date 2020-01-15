# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: k个链表合并, 两种思路
    1. 先ans和第一个合并,出来结果再和第二个, 再第三个
    2. 2个2个合并, 再四个四个合并
"""
"""
    方法1, 一个一个合并
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists: return None
        for i in range(len(lists)-1):
            pos = ans = ListNode(-1)
            p, q = lists[i], lists[i+1]
            while p and q:
                if p.val < q.val:
                    pos.next, pos, p = p, p, p.next
                else:
                    pos.next, pos, q = q, q, q.next
            p = q if not p else p
            pos.next = p
            lists[i+1] = ans.next
        return lists[-1]


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