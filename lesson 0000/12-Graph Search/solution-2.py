# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    深度优先-非递归形式
    不同于拓扑排序, 这里没法在入栈的时候控制重复, 比如a节点指向b, c, d, 那么b, c, d都得压入栈,
    然后d又指向b, 那么在处理d的时候b已经被访问过了, 再等到b出栈的时候就不能处理b了
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

    def DFS(self):

        visited, ans = [0]*self.n, []

        dq = deque()
        for vertex in range(self.n):
            dq.append(vertex)

            while dq:
                v = dq.pop()
                # 深度优先只能出的时候控制重复
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

print(g.DFS())