# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 自己实现优先队列, 非递归形式
    去掉各种冗余计算, 看看到底能优化到多少, solution-5大概在250左右
    solution-6最高能优化到200ms
"""
from typing import List
from collections import deque
from math import floor


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class PriorityQueue:
    def __init__(self, queue=None):
        self.queue = deque(queue) if queue else deque()
        self.size = len(self.queue)
        self.last = floor(self.size/2-1)
        self.sort()

    def sort(self):
        i = self.last
        while i >= 0:
            self.heapify(i)
            i -= 1

    def heapify(self, i):
        start = i
        while i <= self.last:
            r, im = 2*i+2, i
            l = r-1
            if r < self.size and self.queue[r][0] < self.queue[im][0]:
                im = r
            if self.queue[l][0] < self.queue[im][0]:
                im = l

            if im != i:
                self.queue[im], self.queue[i] = self.queue[i], self.queue[im]
                i = im
            else:
                if i == start:
                    return False
                else:
                    break

        return True

    def resort(self):
        i = self.last
        while i >= 0:
            is_swap = self.heapify(i)
            if not is_swap:
                break
            else:
                i = int((i-1)/2)

    def push(self, val, item):
        self.queue.append((val, item))
        self.size = len(self.queue)
        self.last = floor(self.size/2-1)
        self.resort()

    def pop(self):
        ans = self.queue[0]
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        self.queue.pop()
        self.size = self.size-1
        self.last = floor(self.size/2-1)
        self.heapify(0)
        return ans

    def empty(self):
        return True if not self.queue else False


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pos = ans = ListNode(-1)

        vals = [(l.val, l) for l in lists if l]
        pq = PriorityQueue(vals)
        while not pq.empty():
            v, l = pq.pop()
            pos.next, pos = l, l
            if l.next:
                pq.push(l.next.val, l.next)
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