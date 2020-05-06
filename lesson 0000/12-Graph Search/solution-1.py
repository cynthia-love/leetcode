# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    图的遍历, 深度优先-递归形式
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices: list):
        self.vertices = vertices
        self.n = len(vertices)
        self.name2int = dict([(v,k) for k,v in enumerate(vertices)])
        self.edges = defaultdict(list)

    def add_edge(self, start, end):
        self.edges[self.name2int[start]].append(self.name2int[end])

    def DFS(self):

        visited, ans = [0]*self.n, []

        def rf(vertex, visited, ans):
            if visited[vertex] == 1:
                return
            ans.append(vertex)
            visited[vertex] = 1

            for end in self.edges[vertex]:
                rf(end, visited, ans)

        # 分别以每个顶点开始去深度递归
        for vertex in range(self.n):
            rf(vertex, visited, ans)

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

print(g.DFS())