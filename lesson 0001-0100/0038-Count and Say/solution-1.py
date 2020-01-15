# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    题目分析: 外观数列(全是整数), 即从数字1开始, 每一项都是对前一项的描述
    1,                               [[1, "1"]]
    1个1, 即11                       [[2, "1"]]
    2个1, 即21                       [[1, "2"], [1, "1"]]
    一个2一个1, 即1211               [[1, "1"], [1, "2"], [2, "1"]]
    一个1一个2, 2个1, 即111221
    3个1, 2个2, 1个1, 312211
    找到第n项
    基本思路: 对n-1项的字符串扫描计数, 如果字符和前一字符相同, 计数+1, 否则压入新的计数项
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for i in range(2, n+1):
            count = []
            for j in range(len(ans)):
                if j == 0 or ans[j] != ans[j-1]:
                    count.append([1, ans[j]])
                else: count[-1][0] += 1
            ans = ""
            for item in count:
                ans += str(item[0])+item[1]

        return ans


s = Solution()
print(s.countAndSay(5))

