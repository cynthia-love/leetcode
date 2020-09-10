# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    求标准多项式的一阶导数
    f(x) = an·x^n+an-1·x^(n-1)+…+a2·x^2+a1·x+a0
    比如 2*x^5 + 3*x + 8
    则输入2 5 3 1 8 0
    输出: 2 4 3 0
"""

def f(params):
    for i in range(1, len(params), 2):
        params[i] -= 1
    res = []
    for i in range(0, len(params), 2):
        if params[i+1] < 0: continue
        res.extend([params[i], params[i+1]])
    return res


print(f([2, 5, 3, 1, 8, 0]))  # [2, 4, 3, 0]


