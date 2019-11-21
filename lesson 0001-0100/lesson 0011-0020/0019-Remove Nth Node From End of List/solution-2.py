# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 双指针, 比如pre->1->2->3->4->5, 删除倒数第二个意味着当右指针到5的时候, 左指针到3
    考虑特殊情况, 删除5, 按之前思路, 左指针到4, 没问题; 删除1, 没法隔5, 最好加个头部
"""


class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        pre = ListNode(-1)
        pre.next = head

        l, r, d = pre, head, 1
        while r.next:
            if d < n:
                r, d = r.next, d+1
            else:
                l, r = l.next, r.next
        l.next = l.next.next

        return pre.next