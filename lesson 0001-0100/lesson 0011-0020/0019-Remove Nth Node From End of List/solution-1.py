# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 给定链表1->2->3->4->5, 删除倒数第n个, 比如倒数第二个, 变成1->2->3->5. n始终合法
"""


class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        nodes, h = [], head
        while h:
            nodes.append(h)
            h = h.next

        if n == len(nodes):
            head = head.next
        elif n == 1:
            nodes[-2].next = None
        else:
            nodes[-n-1].next = nodes[-n].next
        return head

