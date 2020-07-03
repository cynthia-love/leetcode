# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 递归
"""


class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 如果不满足都不为空, 返回不空的那个
        if not (l1 and l2): return l1 or l2

        ans, l1, l2 = (l1, l1.next, l2) if l1.val < l2.val else (l2, l1, l2.next)

        ans.next = self.mergeTwoLists(l1, l2)

        return ans


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

print(None or None)