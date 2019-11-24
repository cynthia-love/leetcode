# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 自己实现优先队列
    python3自带的优先队列不允许直接插入同优先级元素, 用着蛋疼
    注意堆排序有几个优化点, 可以提升速度:
    1. 因为频繁插入, 删除节点, 建议用dequeue, 比普通list快, 提升200ms左右
    2. 插入元素和初始构建虽然思路一样, 但插入有中断条件, 步长也不一样; 提升100ms左右
    3. heapify的时候, 处理到最后一个非叶节点就结束, 没感觉出来提升
    4. 堆的大小存一下, 用到的地方较多, 提升20-30ms
    5. 最后一个非叶节点索引存一下
    如果不是为了追求极限优化, 考虑到代码易编写性, 只考虑1, 2, 3即可
"""
from typing import List
from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class PriorityQueue:

    def __init__(self, queue=None):
        self.queue = deque(queue) if queue else deque()
        # 堆的大小存一下, 能稍微提升一下性能
        self.size = len(self.queue)
        self.last = int(self.size/2)-1
        # 构建初始堆
        self.sort()

    def heapify(self, i):
        if i > self.last:
            return
        l, r, im = 2*i+1, 2*i+2, i
        if r <= self.size-1 and self.queue[r][0] < self.queue[im][0]:
            im = r
        if l <= self.size-1 and self.queue[l][0] < self.queue[im][0]:
            im = l
        if im != i:
            self.queue[i], self.queue[im] = self.queue[im], self.queue[i]
            self.heapify(im)
            return True
        return False

    def sort(self):
        i = self.last
        while i >= 0:
            self.heapify(i)
            i -= 1

    def resort(self):
        i = self.last
        while i >= 0:
            is_swap = self.heapify(i)
            if not is_swap:
                break
            i = int((i-1)/2)

    def push(self, val, item):
        self.queue.append((val, item))
        self.size += 1
        self.last = int(self.size/2)-1
        self.resort()

    def get(self):
        return self.queue[0]

    def pop(self):
        ans = self.queue[0]
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        self.queue.pop()
        self.size -= 1
        self.last = int(self.size / 2) - 1
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