# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法4, 滑动窗口优化, 可以用作滑动窗口类问题的模板, 一定要记牢了
    abcabcbb, lb分别存{a:0, b:1, c:2}->{a:3, b:1, c:2}
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        # lb存储窗口元素, left存窗口左边界索引
        # 由于s不会为空, 建议窗口初始化长度1, 便于理解
        lb, left, max_len = {s[0]}, 0, 1

        # 窗口初始0-0, 右边界从1开始扩展
        for right in range(1, len(s)):
            # 把窗口里和s[right]相等的元素及其左边都出窗口
            # 这里直接用while就行, 没必要再加个if判断
            while s[right] in lb:
                lb.remove(s[left])
                left += 1
            # 注意和s[right]相等的也remove了, 所以这里要再add一下
            lb.add(s[right])
            # 此时len(lb)为滑到right位置的符合不重复条件的窗口的大小
            max_len = max(max_len, len(lb))

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("pa"))