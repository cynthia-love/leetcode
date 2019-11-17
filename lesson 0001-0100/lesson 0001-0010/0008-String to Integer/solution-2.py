# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 挑战一下完全不借助正则, 灵活借助try except
"""
class Solution:

    def myAtoi(self, str: str) -> int:

        s = str.strip()
        if not s:
            return 0
        flag = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in {'+', '-'} else s

        # 仔细思考这里为什么要这么做
        # 比如最大127, 那么不能算完再和127比, 因为即使大于127截断后还是在127内
        # 所以只能计算前比, 比如32 5, 32大于12, 再乘以10肯定超限
        INT_MIN, INT_MAX = -2**31, 2**31-1
        p_min, q_min = int(INT_MIN/10), INT_MIN-int(INT_MIN/10)*10
        p_max, q_max = int(INT_MAX/10), INT_MAX-int(INT_MAX/10)*10

        ans = 0
        for i in s:
            try:
                # 123aab, 枚举到a的时候会退出
                q = int(i)
                if ans < p_min or (ans == p_min and flag*q < q_min):
                    return INT_MIN
                if ans > p_max or (ans == p_max and flag*q > q_max):
                    return INT_MAX
                ans = ans*10+flag*q
            except:
                break
        return ans


s = Solution()
print(s.myAtoi("-22"))