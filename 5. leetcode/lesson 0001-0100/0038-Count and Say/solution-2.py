# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    方法2, 不求中间ans, 用一维数组
    i项和i-1项值相同, count[-2]+1
    i项和i-1项值不同, 压入计数1, 压入i项
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        count = [1]
        for i in range(n-1):
            current = []
            for j in range(len(count)):
                if j == 0 or count[j] != count[j-1]:
                    current.extend([1, count[j]])
                else:
                    current[-2] += 1
            count = current
        return "".join([str(x) for x in count])


s = Solution()
print(s.countAndSay(2))

