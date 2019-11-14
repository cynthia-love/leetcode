# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 暴力遍历优化
    思路: 比如abcabcbb, 对于第一个a, 最大不重复子串到了c, 那么对于b, b-c之间的没必要遍历了
"""
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        # 用right存上一个最大不重复子串最右索引
        max_len, right = 1, -1

        for i in range(len(s)):
            right = i if right <= i else right
            for j in range(right+1, len(s)):
                # 注意这里是满足条件才加, 所以right的终值刚好是最右索引值
                if s[j] not in s[i:j]:
                    right += 1
                else:
                    break
            max_len = max(max_len, right-i+1)
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))