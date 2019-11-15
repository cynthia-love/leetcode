# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法2, 数字型直接倒转
    比如123, 第一次ans=3, 第二次ans*10+2=32, 第三次ans*10+1=321
"""


class Solution:
    def reverse(self, x: int) -> int:
        # 注意, python里, -1//10 = -1 ~ 9, 而不是0~-1, 负数不能用//和%
        # 要正数下取, 负数上取, 所以这里用int最合适, 直接舍弃小数位
        MIN_INT, MAX_INT, ans = -2**31, 2**31-1, 0

        # 注意and要先判断超限, 能加再去加, 而不能计算完后再和MIN_INT, MAX_INT比
        # 以8位为例, -128: 127, -12~-8, 12~7, 所以这里才会算p/q_max/min
        p_min, q_min = int(MIN_INT / 10), MIN_INT - int(MIN_INT / 10) * 10
        p_max, q_max = int(MAX_INT / 10), MAX_INT - int(MAX_INT / 10) * 10

        while x:
            # 由于有负数, 取个位值只能这么取; 这里建议先算p再算q, 避免重复计算
            p, q = int(x/10), x-int(x/10)*10

            # 第一种, p部分就超限了, 那乘以10以后肯定超限
            if ans < p_min or ans > p_max:
                return 0
            # 第二种, p部分相等, q部分超限
            if (ans == p_min and q < q_min) or (ans == p_max and q > q_max):
                return 0

            ans, x = ans*10 + q, p

        return ans


s = Solution()
print(s.reverse(-1463847412))