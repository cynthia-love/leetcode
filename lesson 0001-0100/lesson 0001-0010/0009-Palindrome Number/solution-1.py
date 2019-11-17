# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 判断一个数字是否是回文, 比如1, 比如121, 负数肯定不是
"""
"""
    方法1, 借助str, 这种不用考虑负数
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        # 奇数012, 到1; 偶数0123到1
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True


s = Solution()
print(s.isPalindrome(123))