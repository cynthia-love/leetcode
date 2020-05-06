# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    拓扑排序, 深度优先-非递归形式
    思路: 利用双向队列, 一边进一边出, 即为深度优先; 一边进另一边出, 即为广度优先
    另外, 较之普通深度优先遍历, 拓扑排序有用到入度概念, 可以在插入时控制不重复, 所以不用visited数组

"""
from collections import defaultdict, deque


class Graph:

    def __init__(self, vertices: list):
        self.vertices = vertices
        self.n = len(vertices)
        self.name2int = dict([(v, k) for k, v in enumerate(vertices)])
        self.edges = defaultdict(list)

    def add_edge(self, start, end):
        self.edges[self.name2int[start]].append(self.name2int[end])

    def topo_sort(self):
        indegrees, ans = [0]*self.n, []

        # 初始化入度数组
        for ends in self.edges.values():
            for end in ends:
                indegrees[end] += 1

        dq = deque()
        # 把初始入度为0的压入dq
        for vertex in range(self.n):
            if indegrees[vertex] == 0:
                dq.append(vertex)

        while dq:

            vertex = dq.pop()
            ans.append(vertex)

            for end in self.edges[vertex]:
                indegrees[end] -= 1
                if indegrees[end] == 0:
                    dq.append(end)

        return ans if len(ans) == self.n else -1


g = Graph(["a", "b", "c", "d", "e", "f"])
g.add_edge("f", "c")
g.add_edge("f", "a")
g.add_edge("e", "a")
g.add_edge("e", "b")
g.add_edge("c", "d")
g.add_edge("d", "b")
print(g.topo_sort())
