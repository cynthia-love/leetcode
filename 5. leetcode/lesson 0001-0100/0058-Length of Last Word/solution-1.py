# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 仅包含字母和空格的字符串, 返回最后一个单词的长度; 不存在返回0
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.rstrip()
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ': return len(s)-1-i

        return len(s)


s = Solution()
print(s.lengthOfLastWord("a "))
