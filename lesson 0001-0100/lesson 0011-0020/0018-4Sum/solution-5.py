# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 应该是k越大这种表现越好, 3数和230/313, 4数和217/282, 好像并没有
    {
        4: {8: [[1, 2, 3, 4], [2,3, 8, 0]]}
    }
    了解这种思路即可, 但这题不适合, 有太多荣誉计算
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        mem = {}

        def rf(n):
            if n in mem:
                return mem[n]

            ans = {}
            if n == 1:
                for i, v in enumerate(nums):
                    if v not in ans:
                        ans[v] = [tuple([i])]
                    else:
                        ans[v].append(tuple([i]))
                mem[n] = ans

                return ans

            if n == 2:
                for i in range(len(nums)):
                    for j in range(i+1, len(nums)):
                        k12 = nums[i]+nums[j]
                        if k12 not in ans:
                            ans[k12] = [tuple([i, j])]
                        else:
                            ans[k12].append(tuple([i, j]))
                mem[n] = ans
                return ans

            ans1, ans2 = rf(int(n/2)), rf(int((n+1)/2))
            key1, key2 = ans1.keys(), ans2.keys()

            for k1 in key1:
                for k2 in key2:
                    v1, v2, k12 = ans1[k1], ans2[k2], k1+k2
                    for vv1 in v1:
                        for vv2 in v2:
                            ll1, ll2, m = 0, 0, []
                            while ll1 <= len(vv1)-1 and ll2 <= len(vv2)-1:
                                if vv1[ll1] == vv2[ll2]: break
                                if vv1[ll1] < vv2[ll2]:
                                    m.append(vv1[ll1])
                                    ll1 += 1
                                else:
                                    m.append(vv2[ll2])
                                    ll2 += 1
                            if ll1 > len(vv1)-1:
                                m += vv2[ll2:]
                            else:
                                m += vv1[ll1:]

                            if len(m) == len(vv1)+len(vv2):

                                if k12 not in ans:
                                    ans[k12] = {tuple(m)}
                                else:
                                    ans[k12].add(tuple(m))

            ans = dict([(k, list(v)) for k, v in ans.items()])
            mem[n] = ans
            return ans

        ans_all = rf(15)
        if target not in ans_all:
            return []

        ans_i = ans_all[target]
        ans_v = set([tuple([nums[x] for x in y]) for y in ans_i])
        return [[x for x in y] for y in ans_v]

import datetime
t1 = datetime.datetime.now()
s = Solution()
import random
random.seed(1)
x = [random.randint(-10, 10) for i in range(30)]
print(x)
r = s.fourSum(x, 0)
print(r)

print(datetime.datetime.now()-t1)