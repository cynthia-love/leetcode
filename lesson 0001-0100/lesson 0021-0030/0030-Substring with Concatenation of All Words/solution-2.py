# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, hash
    其实方法1之所以超时, 感觉问题主要出在匹配判断函数上
    在保留方法1优化思路的基础上, 改进匹配函数, 改为hash判断
    s = "barfoofoothefoobarman", words = ["foo","bar"]
    子串barfoofoo, words = ["foo", "foo","bar"]
    定义哈希:
    {
        "foo": 2,
        "bar": 1
    }
    遍历barfoofoo的时候, 再造一个hash, 最后比较两个dict是否相等
    两个优化点, 一个和方法1一样
     bababababa
      babababacd, 这里只需要看cd和ba能不能匹配上了
    另外一个是构建hash的时候, 提前终止
    虽然过了 但是耗时在1100ms左右, 还是不理想
"""
from typing import List
from collections import defaultdict

class Solution:

    def isMatch(self, subs, subwords) -> bool:
        size, h, h_s = len(subwords[0]), defaultdict(int), defaultdict(int)
        for word in subwords: h[word] += 1
        for i in range(0, len(subs)-size+1, size):
            h_s[subs[i: i+size]] += 1
            # 优化点, 提前终止
            if h_s[subs[i: i+size]] > h[subs[i: i+size]]:
                return False
        return True


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        ans, lens, size = set(), len(words), len(words[0])
        for i in range(len(s)-lens*size+1):

            flag = False
            for j in range(1, lens):
                # 如果有部分和之前比上的重叠, 仅比较剩余部分
                if i-j*size in ans:
                    subs = s[i+(lens-j)*size:i+lens*size]
                    subwords = [s[x: x+size] for x in range(i-j*size, i, size)]
                    if self.isMatch(subs, subwords):
                        ans.add(i)
                        flag = True
                        break
            if not flag and self.isMatch(s[i: i+lens*size], words):
                ans.add(i)

        return list(ans)


s = Solution()
print(s.findSubstring("abababba", ['ab', 'ba']))