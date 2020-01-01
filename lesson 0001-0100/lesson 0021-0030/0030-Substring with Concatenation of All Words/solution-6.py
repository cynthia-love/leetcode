# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    方法6, 结合方法5对方法3的优化(3种情况)和方法4对方法3的优化(先算一波, 省去后面count判断)
    bar-foo-foo-bar-the
     arf-oof-oob-art-hef

    1. 当前hash匹配上了, 那么下一个hash只需要比较要出去的和要进来的
    2. 当前判断过程中发现不在words里的单词, 那么窗口进行大跳
    3. 之前有次数超限的单词, 那么一直要等到能够移除这个单词才能进行正常判断

    好像如果先算, 那么优化点2就没法做了...从效果来看, 没了优化点2, 还不如方法5快
"""
from typing import List
from collections import defaultdict


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []

        lens, lenw, size, hw = len(s), len(words), len(words[0]), defaultdict(int)
        # 处理words
        for item in words: hw[item] += 1

        h, ans = [defaultdict(int) for i in range(size)], set()

        # 初始化d
        for i in range(size):
            for j in range(i, min(lens-size+1, i+lenw*size), size):
                h[i][s[j: j+size]] += 1

        for i in range(size):
            if h[i] == hw: ans.add(i)

        # 处理剩余部分
        for i in range(size):
            for j in range(min(lens-size+1, i+lenw*size), lens-size+1, size):
                l, r = j-lenw*size, j
                lw, rw = s[l: l+size], s[r: r+size]
                # 下面两句一定不能用连续赋值, 因为存在lw和rw相等的情况
                h[i][rw] += 1; h[i][lw] -= 1

                # 优化点3, 注意if lw in hw的判断, 避免hw自动被添加元素
                # 方法5之所以不需要这句判断, 因为其大跳代码在最前面
                # 不在hw里的单词根本就不会处理, 也不会忘h[i]里添加
                if lw in hw and h[i][lw] > hw[lw]: continue
                # 注意底下这句话要放在优化点的后面; defaultdict的特点, 访问了就赋值
                if h[i][lw] == 0: h[i].pop(lw)
                # 优化点1, 之前的匹配上了
                if l in ans:
                    if lw == rw: ans.add(l+size)
                elif h[i] == hw: ans.add(l+size)

        return list(ans)


s = Solution()
print(s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                      ["fooo","barr","wing","ding","wing"]))
