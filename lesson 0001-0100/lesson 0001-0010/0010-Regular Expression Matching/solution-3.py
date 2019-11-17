# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 非确定性有穷状态机, NFA
    a*b*c*拼个$方便处理, a*b*c*$节点数是去掉*之后的字符数量+1
    数据结构:
    self.n, 节点个数, 0表示首节点
    self.e, 边, 格式 (这题其实用不到):
        {
            0: {1: ['a', 'b']},
            2: {2: ['c']}
        }
    self.m, 动作, 格式:
        {
            0: {'a': [2, 3]},
            1: {'c': [1, 2]}
        }
"""
from collections import defaultdict

class Graph:
    def __init__(self, p):
        # a*b*c*->a*b*c*$
        self.p = p+'$'
        # a*b*c*$->abc$
        self.p_ns = self.p.replace("*", "")
        self.n = len(self.p_ns)+1

        self.m = defaultdict(dict)
        self.createNFA()

    def createNFA(self):
        # 初始化move
        for v in range(self.n):
            self.m[v] = defaultdict(list)
        # 初始状态位于首节点
        p, i, v = self.p, 0, 0
        while p[i:]:
            if p[i+1:] and p[i+1] == '*':
                self.m[v][p[i]].append(v+1)
                self.m[v+1][p[i]].append(v+1)
                i2, v2 = i, v
                while p[i2+1:] and p[i2+1] == '*' and p[i2+2:]:
                    self.m[v][p[i2+2]].append(v2+2)
                    i2, v2 = i2+2, v2+1
                i, v = i+2, v+1
            else:
                self.m[v][p[i]].append(v+1)
                i, v = i+1, v+1

    def DFS(self, s):
        s = s+'$'

        def rf(s, v):
            if not s: return v == self.n-1

            for c in self.m[v][s[0]]+self.m[v]['.']:
                if rf(s[1:], c):
                    return True

            return False

        return rf(s, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        g = Graph(p)
        return g.DFS(s)


s = Solution()
print(s.isMatch("aaa", "a*b*c*"))
