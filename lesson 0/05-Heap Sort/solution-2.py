# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    堆排序, 非递归形式
    无非heapify函数不递归, 而是判断当下是否探到底
    (单分支递归很容易改非递归, while就行; 双分支的比如归并, 可以用双端队列)
    ([8][7][6][5][4][2][1][2], 先取87, 怕排好序, 插入[87], 取65, 插入[65], 22完成后队列变成
    [78], [56], [24], [12], 再取前两个, 变成[5678], 再插入队尾...)

"""
from typing import List, Tuple
from collections import deque


class PriorityQueue:
    def __init__(self, queue: List[Tuple[int, object]] = None):
        self.queue = deque(queue) if queue else deque()
        self.sort()

    def sort(self):
        i = int(len(self.queue)/2)-1
        while i >= 0:
            self.heapify(i)
            i -= 1

    def heapify(self, i):
        flag = False
        while i <= int(len(self.queue)/2)-1:
            l, r, im = i*2+1, i*2+2, i
            im = r if r <= len(self.queue)-1 and self.queue[r][0] < self.queue[im][0] else im
            im = l if l <= len(self.queue)-1 and self.queue[l][0] < self.queue[im][0] else im

            if im != i:
                self.queue[i], self.queue[im] = self.queue[im], self.queue[i]
                i = im
                flag = True
            else:
                break

        return flag

    def push(self, val: int, obj: object):
        self.queue.append((val, obj))
        self.resort()

    def resort(self):
        i = int(len(self.queue)/2)-1
        while i >= 0:
            flag = self.heapify(i)
            if not flag: break
            i = int((i+1)/2)-1

    def pop(self) -> Tuple[int, object]:
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        ans = self.queue.pop()
        self.heapify(0)
        return ans

    def empty(self):
        return True if not self.queue else False


class Solution:
    def heap_sort(self, arr: List[int]) -> List[int]:
        pq = PriorityQueue([(x, x) for x in arr])
        ans = []
        while not pq.empty():
            ans.append(pq.pop()[0])
        return ans


s = Solution()
print(s.heap_sort([12, 11, 13, 5, 6, 7]))

