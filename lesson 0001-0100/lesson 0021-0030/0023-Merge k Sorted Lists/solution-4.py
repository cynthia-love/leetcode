# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 优先队列
    思路1, 把所有元素全部放进去, 堆排序, 但是这样就无法利用每个链表有序的特点了
    思路2, 每次只压每个链表的第一个元素
"""
from typing import List
from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        pos = ans = ListNode(-1)

        pq = PriorityQueue()

        # python3的优先队列, 如果元素不支持比较, 那么不允许插入同优先级的元素
        # 这里无法给ListNode添加__lt__, __gt__, __eq__, 只能添加个index
        # 一般情况下, put的时候(val, item)即可
        index = 0

        for i in range(len(lists)):
            # ()里的第一个参数是优先级, 越小越高
            # 这里如果想想优先取大的很容易, 加个负号
            if lists[i]:
                pq.put((lists[i].val, index, lists[i]))
                index += 1
        while not pq.empty():
            val, i, l = pq.get()
            pos.next, pos = l, l
            if l.next:
                pq.put((l.next.val, index, l.next))
                index += 1

        return ans.next


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



