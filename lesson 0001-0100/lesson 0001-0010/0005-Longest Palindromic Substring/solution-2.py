# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 动态规划
    思路: ababa是回文的条件是s[i+1, j-1]是且s[i] == s[j]
    所以, 从1到n遍历长度即可
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:

        # dp = [[False]*len(s)]*len(s)
        # 这里不能这么写, [x]*n的写法,如果x不是基本数据类型, 复制的是引用; 这里每行会是同一个数组
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        ans = ""
        for k in range(1, len(s)+1):
            for i in range(len(s)-k+1):
                j = i+k-1  # 这里得先算出来, 不然会超时
                dp[i][j] = s[i] == s[j] and (k <= 2 or dp[i+1][j-1])
                # 这里用max_len比用len(ans)会稍微快一点, 虽然还是很慢
                if k > len(ans) and dp[i][j]:
                    ans = s[i:j+1]
        return ans


s = Solution()
print(s.longestPalindrome("babad"))