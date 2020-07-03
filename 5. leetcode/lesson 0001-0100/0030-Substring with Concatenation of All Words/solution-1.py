# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: s = "barfoothefoobarman", words = ["foo","bar"]
    找到s中所有子串的起始索引, 子串的概念为words中的所有单词拼起来(不限先后次序)
    比如这里可以找foobar也可以找barfoo, 限定每个单词长度一致
"""
"""
    方法1, 暴力法, 给每个word设置一个指针, 从头开始遍历s, 每次取和所有word加起来长度相同的子串
    针对每个子串, 遍历words指针, 匹配上的后移一位; 如果某个匹配到头了, 把所有未匹配到头的重置
    子串遍历完以后, 看指针数组的总长度, 以确定是否都到头了, 到了, 说明匹配上
    
    不出意外, 上述方法超时
    
    第一个优化思路, 如果前面匹配上的子串和当前子串有重合的部分, 且这部分长度是size的倍数, 那么
    这部分就不需要再重复判断了
    
    bababababa
      babababacd, 这里只需要看cd和ba能不能匹配上了, 出意外, 还是超时
"""
from typing import List


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []

        lens, size, ans = len(words), len(words[0]), []

        def isMatch(subs, subwords):
            sublens, subsize = len(subwords), len(subwords[0])
            l_pos = [0]*sublens

            for item in subs:

                for i in range(sublens):
                    if l_pos[i] > subsize - 1: continue
                    if subwords[i][l_pos[i]] == item:
                        l_pos[i] = l_pos[i] + 1
                        if l_pos[i] > subsize - 1:
                            l_pos = [x if x > subsize - 1 else 0 for x in l_pos]
                            break

            return True if sum(l_pos) == sublens * subsize else False

        for index in range(len(s)-lens*size+1):

            flag = False
            for item in ans[-1:-1:-1]:
                dis = index -item
                if dis >= lens*size: break
                if dis % size == 0:
                    subs = s[index+lens*size-dis: index+lens*size]
                    subwords = [s[i: i+size] for i in range(item, index, size)]
                    if isMatch(subs, subwords):
                        flag = True
                        ans.append(index)
                        break

            if not flag and isMatch(s[index: index+lens*size], words): ans.append(index)

        return ans


s = Solution()
print(s.findSubstring("bababaab", ['ba', 'ab']))
