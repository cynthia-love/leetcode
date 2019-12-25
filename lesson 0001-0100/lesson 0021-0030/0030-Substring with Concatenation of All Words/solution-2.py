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
"""
from typing import List


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass



s = Solution()
print(s.findSubstring("abababba", ['ab', 'ba']))