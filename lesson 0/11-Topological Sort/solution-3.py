# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    拓扑排序, 广度优先, 只有非递归形式, 一边进另一边出即为广度优先
    另外, 注意这里的广度优先和图的广度优先概念不一样, 这里广的是入度为0的点而非子节点
"""
from collections import defaultdict, deque


class Graph:

    def __init__(self, vertices: list):
        self.vertices = vertices
        self.n = len(vertices)
        self.name2int = dict([(v,k) for k,v in enumerate(vertices)])
        self.edges = defaultdict(list)

    def add_edge(self, start, end):
        self.edges[self.name2int[start]].append(self.name2int[end])

    def topo_sort(self):
        indegrees, ans = [0]*self.n, []

        for ends in self.edges.values():
            for end in ends:
                indegrees[end] += 1

        dq = deque()
        for vertex in range(self.n):
            if indegrees[vertex] == 0:
                dq.append(vertex)

        while dq:
            vertex = dq.popleft()
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

