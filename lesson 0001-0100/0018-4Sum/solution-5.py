# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3的另一种实现方式, 比如算7个数的和, 可以设置一个递归把3和4个数的所有枚举都算出来, 并利用
    动态规划的思想把中间结果存起来, 中间值存储形式:
    {
        4: { -8: [[1, 2], [3, 4]], 4: [[0, 5]]},
        2: ...
    }
    nums先排个序, 便于归并

    想法是好的, 但是从结果来看, 虽然能算出来, 但冗余计算太多, 导致时间性能远差于solution-4, 超时
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

        ans_all = rf(4)
        if target not in ans_all:
            return []

        ans_i = ans_all[target]
        ans_v = set([tuple([nums[x] for x in y]) for y in ans_i])
        return [[x for x in y] for y in ans_v]


s = Solution()
print(s.fourSum([1, 2, 3, 4, 5], 10))
