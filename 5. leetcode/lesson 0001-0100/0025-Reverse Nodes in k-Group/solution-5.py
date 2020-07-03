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

        pos = ans = ListNode(-1)

        while True:
            h, c = head, 1
            if not h: return ans.next

            while h and c <= k: h.next, pos.next, h, c = pos.next, h, h.next, c+1

            # c>k说明翻转到底了, 以->-1->3->2->1 4->5为例, 此时head指向1, h指向4,
            if c > k: head.next, pos, head = h, head, h
            # 不足k个, 说明多翻了, 最后一次要再翻一次翻回去
            # -1->3->2->1 5->4, 此时head指向4, h指向none, pos指向1
            else: head.next, head, k = None, pos.next, c-1


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


