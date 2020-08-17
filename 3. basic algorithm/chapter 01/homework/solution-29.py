# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    输出'c', 'a', 't', 'd', 'o', 'g' 所有可能组成的字符串, 不可重复
"""
from itertools import permutations
def f1():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    g = permutations(l, len(l))
    l_p = list(g)
    return l_p

print(len(f1()))

# 其他方法, 自己实现
# 方法1, 递归最一般思路, 在当前数组里面选一个, 剩下的继续递归, 直到数组长度为1, 全拼起来append到结果集里去
def f2():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    def rf(res, l):
        if len(l) == 1:
            r.append(res+l[0])
        else:
            for i in range(len(l)):
                rf(res+l[i], [l[j] for j in range(len(l)) if j!=i ])
                # 注意这里用的解析语法, 会生成一个新的[], 避免直接在原[]上改影响了下一次递归

    rf("", l)
    return r
print(len(f2()))

# 方法2,



