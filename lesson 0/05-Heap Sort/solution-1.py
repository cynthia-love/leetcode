# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    堆排序, 一种利用堆的概念进行的排序, 父节点总是>=或<=左右子节点
    根据完全二叉树的性质, 对于0 1 2 3 4 5 6 ... 共n个节点:
    1. 最后一个非叶节点索引值为: int(n/2)-1
    2. 索引n节点的左子节点索引为2n+1, 右子2n+2
    那么从最后一个非叶节点往上遍历一遍, 如果某个节点和子节点有交换
    那么还得往下处理直到不再交换为止

    优先队列和堆排序的区别无非是由存[1, 2, 8, 4]这样的变成存[(1, item1), (2, item2)...]
    比较排序的时候区元素的[0]去比较即可, 其他和堆排序完全一样
"""
"""
    堆排序, 递归形式
"""
from typing import List, Tuple
from collections import deque


class PriorityQueue:
    # 这里额外讲一下typing, List[int or float], 还可以用and or
    # 而Tuple[int, object], 不是表示或, 而是(int, object)这种
    def __init__(self, queue: List[Tuple[int, object]] = None):
        self.queue = deque(queue) if queue else deque()
        self.sort()

    def sort(self):
        i = int(len(self.queue)/2)-1
        while i >= 0:
            self.heapify(i)
            i -= 1

    def heapify(self, i):
        if i > int(len(self.queue)/2)-1: return
        l, r, im = i*2+1, i*2+2, i
        im = r if r <= len(self.queue)-1 and self.queue[r][0] < self.queue[im][0] else im
        im = l if l <= len(self.queue)-1 and self.queue[l][0] < self.queue[im][0] else im
        # 如果根节点不是最小
        if im != i:
            self.queue[i], self.queue[im] = self.queue[im], self.queue[i]
            self.heapify(im)
            # True表示此次由i开始下溯了(有节点交换)
            # push的时候利用此标志终止上溯
            return True

    def push(self, val: int, obj: object):
        self.queue.append((val, obj))
        # 注意添加元素和首次整理不一样, 不用经过所有的非叶节点
        self.resort()
        # 另外, 往下heapify自带提前终止特性, 而往上走没有
        # 对于push来说, 处理到某一个节点, 发现没交换, 就没必要往上走了, 此优化能优化时间440->280

    def resort(self):
        i = int(len(self.queue)/2)-1
        while i >= 0:
            flag = self.heapify(i)
            if not flag: break
            # 这种写法当i=0的时候会死循环, 要么改成floor, 要么换种写法
            # i = int((i-1)/2)
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

