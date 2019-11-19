# -*- coding: utf-8 -*-

# Author: Cynthia


"""
    方法2, 之前的思路是同时比较所有str的第1个字符, 第2个字符...
    还有一种思路是两两比较出来一个prefix, 再和第三个比
"""
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: return ""

        ans = strs[0]

        for i in range(1, len(strs)):

            p, q, tmp = 0, 0, ""
            while p <= len(ans)-1 and p <= len(strs[i])-1:
                if ans[p] != strs[i][q]:
                    break
                tmp, p, q = tmp+ans[p], p+1, q+1

            ans = tmp

        return ans


s = Solution()
print(s.longestCommonPrefix(["aaa", "abc", "abd"]))