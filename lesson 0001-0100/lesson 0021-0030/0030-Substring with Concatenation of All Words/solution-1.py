# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: s = "barfoothefoobarman", words = ["foo","bar"]
    找到s中所有子串的起始索引, 子串的概念为words中的所有单词拼起来(不限先后次序)
    比如这里可以找foobar也可以找barfoo, 限定每个单词长度一致
"""
from typing import List


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []

        ans, lens, size, index = [], len(words), len(words[0]), 0

        def isMatch(subs, subwords):
            lens, size = len(subwords), len(subwords[0])
            pos, l_pos = 0, [0] * lens

            while pos <= index + lens * size - 1:

                for i in range(lens):
                    if l_pos[i] > size - 1: continue
                    if words[i][l_pos[i]] == s[pos]:
                        l_pos[i] = l_pos[i] + 1
                        if l_pos[i] > size - 1:
                            l_pos = [x if x > size - 1 else 0 for x in l_pos]
                            break
                pos += 1

            if sum(l_pos) == lens * size:

        while index <= len(s)-lens*size:

            for item in ans:
                if index-item < lens*size and (index-item) % size == 0:
                    print(item)
                    # 这里优化
                    break


                ans.append(index)
                match = True

            index += 1

        return ans


s = Solution()
print(s.findSubstring("aaaaaaaa", ["aa","aa", "aa"]))
