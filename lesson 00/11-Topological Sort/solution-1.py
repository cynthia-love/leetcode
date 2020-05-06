# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    拓扑排序
    概念: 由一个有向无环图的顶点组成的序列, 满足若存在边A->B, 则A一定在B前面
    数据结构:
    顶点: ['a', 'b', 'e']
    顶点个数/索引: 3, (索引从0开始, 不再单独存一个数组)
    边:{
        1: [2, 3],
        2: [3]
    }(用defaultdict(list)存储以初始化value为[])

    基本思路: 从入度为0的点开始, 将其指向节点入度减1, 如果减1后等于0, 继续

"""
"""
    拓扑排序, 深度优先-递归形式
    注意这里的深度优先和图的深度优先不太一样, 这里深度的回头条件是入度不为0而非不存在边
"""
from collections import defaultdict


class Graph:

    def __init__(self, vertices: list):
        self.vertices = vertices
        self.n = len(vertices)
        self.name2int = dict([(v, k) for k, v in enumerate(vertices)])
        self.edges = defaultdict(list)

    def add_edge(self, start, end):

        self.edges[self.name2int[start]].append(self.name2int[end])

    def topo_sort(self):

        def rf(index, indegrees, ans):
            if indegrees[index] != 0:
                return
            ans.append(index)

            for end in self.edges[index]:
                indegrees[end] -= 1
                rf(end, indegrees, ans)

        indegrees, ans = [0]*self.n, []

        # 初始化入度列表
        for ends in self.edges.values():
            for end in ends:
                indegrees[end] += 1

        for i in range(self.n):
            rf(i, indegrees, ans)

        return ans if len(ans) == self.n else -1


g = Graph(["a", "b", "c", "d", "e", "f"])
g.add_edge("f", "c")
g.add_edge("f", "a")
g.add_edge("e", "a")
g.add_edge("e", "b")
g.add_edge("c", "d")
g.add_edge("d", "b")
print(g.topo_sort())