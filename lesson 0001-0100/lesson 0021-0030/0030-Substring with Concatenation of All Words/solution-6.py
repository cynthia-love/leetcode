# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    方法6, 结合方法5对方法3的优化(3种情况)和方法4对方法3的优化(先算一波, 省去后面count判断)
"""
from typing import List
from collections import defaultdict


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass


s = Solution()
print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
