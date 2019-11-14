# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 滑动窗口
    思路: 比如abcabcbb, 方法2的思路是减少重复比较, 比如对于a已经比较到abc了, 那么b就不和c比较了
    而滑动窗口则是真正的减少比较次数, 比如abc, 右边再遇到b, 左索引直接划到b
    00->01-02->13->24->35->56->77, 可以发现窗口右边界是以1递增的
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 同样, 这种特殊情况没必要费脑子放到后面去处理
        if len(s) <= 1:
            return len(s)

        l, r, max_len = 0, 0, 1

        while r <= len(s)-1:
            # 从l到r-1寻找与r相同的字符
            # 找到后, 窗口左边界移到其下一位
            for i in range(l, r):
                if s[i] == s[r]:
                    l = i+1
                    break  # 少了这个break, 性能差距会非常大

            max_len = max(max_len, r-l+1)
            r += 1

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("a"))