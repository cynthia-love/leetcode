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
    return ["".join(x) for x in l_p]

print(len(set(f1())))

# 其他方法, 自己实现
# 方法1, 递归最一般思路, 枚举, 在当前数组里面选一个, 剩下的继续递归, 直到数组长度为1, 全拼起来append到结果集里去

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
print(len(set(f2())))

# 方法2, 回溯法
# 和f2的区别在于, f2是准入控制, 已经用到的字符就不传给下一级递归了
# 而回溯法则是可以到下一级递归, 发现不符合条件再回去
def f3():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []

    def rf(res, s):
        if s in res: return
        # 注意这里判断的一定是5, 而不是6
        if len(res) == 5:
            r.append(res+s)
            return
        for each in l:
            rf(res+s, each)

    for each in l:
        rf("", each)

    return r
print(len(set(f3())))

# 方法4, n进制元素自然进位法(不停地加1, 然后过滤掉不符合要求的项), 效率低
# 012->020->021->022->100->101->...
# 最后一次循环为1-000
def f4():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    n = len(l)
    k = list(range(n))  # 初始012345

    while sum(k) != 0:  # 555555->1-000000
        if len(set(k)) == n:
            r.append("".join([l[i] for i in k]))
        flag = 0
        for i in range(n-1, -1, -1):
            k[i] = k[i] + 1 if i == n-1 else k[i] + flag
            flag = 0
            if k[i] >= n:
                k[i] %= n
                flag = 1
            else:
                break
    return r

print(len(set(f4())))

# 方法5和6, 递归的另一种思路, 插入以及衍生的号称最蛋疼的全排列邻位对换法
def f5():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    # 插入思路, c->ac, ca->tac, atc, act, tca, cta, cat->...

    def rf(s, i):
        if len(s) == len(l):
            r.append(s)
            return
        # 枚举位置比s长度多一个
        for j in range(len(s)+1):
            rf(s[:j]+l[i]+s[j:], i+1)
    rf("", 0)
    return r
print(len(set(f5())))

"""
    邻位对换法思路, 不断地找最大可移动数
    (1)可移动概念, 一个数沿着它的方向的邻位比它小(需要引入方向概念)
    (2)如果一个可移动的数发生了移动, 那么所有比他大的数的方向都反过来
    有点绕, 基本思路其实很简单: 1234, 找到最大可移动的数4, 1243
    继续找最大可移动数4, 1423, 继续, 4123, 再找最大可移动数3
    4132, 因为3移动了, 把大于3的方向反向, 此时继续找最大可移动, 又变成了4
    
    1234->1243->1423->4123
    123->132
    4132->1432->1342->1324
    132->312
    3124->3142->3412->4312
    12->21
    4321->3421->3241->3214
    321->231
    2314->2341->2431->4231
    231->213
    4213->2413->2143->2134
    
"""
def f6():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    n = len(l)
    # k存储索引序列, 即我们要排序的对象
    # d存储各个索引的初始方向, 初始都向左, 即-1
    k = list(range(n))  # [0, 1, 2, 3, 4, 5]
    d = [-1 for _ in range(n)]  # [-1, -1, -1, -1, -1, -1]

    def findTop():
        top_i, top_v = -1, -1
        # 这里直接遍历k就好, 没必要非要从大到小找
        # 从大到小找倒是可以提前终止, 不过还得去反向定位其在k中的位置
        for i in range(n):
            # 符合条件的要求: 移动方向上的下一个位置的值小于当前值
            if k[i] > top_v and 0 <= i+d[k[i]] < n and k[i+d[k[i]]] < k[i]:
                top_i, top_v = i, k[i]
        return top_i, top_v

    r.append("".join([l[i] for i in k]))

    while True:
        t_i, t_v = findTop()
        if t_i == -1: break

        # 注意这里的改变方向要放在位置移动前面
        for i in range(t_v+1, n):
            d[i] = -d[i]

        # 待移动位置t, 邻位t+d[k[i]]
        k[t_i], k[t_i+d[t_v]] = k[t_i+d[t_v]], k[t_i]

        r.append("".join([l[i] for i in k]))

    return r
print(len(set(f6())))


