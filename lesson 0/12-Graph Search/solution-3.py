# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    广度优先, 只有非递归形式
"""
from collections import defaultdict, deque


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.n = len(vertices)
        self.name2int = dict([(v,k) for k,v in enumerate(vertices)])
        self.edges = defaultdict(list)

    def add_edge(self, start, end):

        self.edges[self.name2int[start]].append(self.name2int[end])

    def BFS(self):
        visited, ans = [0]*self.n, []

        dq = deque()

        # 右侧进, 左侧出, 即为广度优先
        for vertex in range(self.n):
            dq.append(vertex)
            while dq:
                v = dq.popleft()
                if visited[v] == 1:
                    continue
                ans.append(v)
                visited[v] = 1
                for end in self.edges[v]:
                    dq.append(end)

        return ans


g = Graph(["a", "b", "c", "d", "e", "f"])
g.add_edge("f", "c")
g.add_edge("f", "a")
g.add_edge("e", "a")
g.add_edge("e", "b")
g.add_edge("c", "d")
g.add_edge("d", "b")
g.add_edge("a", "c")
g.add_edge("a", "d")
g.add_edge("a", "f")

print(g.BFS())