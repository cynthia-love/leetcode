# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 还是递归, 但是思路有点不一样
    ()), ((), 假设左括号个数为p, 那么下一个位置可以放置:
    1. 如果p没到n, 还可以放左括号
    2. 如果右括号个数没到p, 可以放右括号
"""


from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def rf(s="", p=0, q=0):
            if len(s) == 2*n:
                ans.append(s)
                return
            # 有点绕, 代码倒是更简洁了, 但是不好理解
            if p < n:
                rf(s+"(", p+1, q)
            if q < p:
                rf(s+")", p, q+1)

        rf()
        return ans


s = Solution()
print(s.generateParenthesis(3))