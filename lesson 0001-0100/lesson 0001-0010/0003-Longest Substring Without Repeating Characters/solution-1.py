# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 最长不含重复字符的子串, 比如abcabcbb最长子串abc, 输出3

"""
"""
    方法1, 暴力遍历, 从每一个字符出发, 寻找最长不重复子串
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        # 对于""和"x"的情况, 建议单拎出来处理, 这样主体代码部分逻辑更清晰
        if len(s) <= 1:
            return len(s)

        max_len = 1
        for i in range(len(s)):
            k = 1
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    k += 1
                else:
                    break
            max_len = max(max_len, k)
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("abcad"))
