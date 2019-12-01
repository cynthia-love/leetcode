# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 不用乘号, 除号, 模运算符计算两个数的商, 32位整数范围
    比如 10/3=3...1, 7/-3=-2...1, -7/-3=2...-1
    思路: 比如1284/4
    =1200/4+80/4+4/4=321
    =1200/400*10**2+80/40*10**1+4/4*10**0, 二进制同理
    1111/10 (15/2=7)
    =1000/10<<2>>2+100/10<<1>>1+10/10<<0>>0
    =111
    1111/12
    =1110/120*10**1+31/12*10**0
    =90+2=92

    二进制与十进制不同的地方在于, 10010/11, 被除数符合最大左移时, 商一定是1
    10001/1100, 100...11, 注意直接跳过了110
"""
"""
    先不考虑溢出试试
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 异或, 符号不同时为True
        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor, count = abs(dividend), abs(divisor), 0

        while dividend >= divisor:
            divisor, count = divisor << 1, count+1
        # 100/10的, 左移了2位; 100/11的左移了1位
        divisor, count, result = divisor >> 1, count-1, 0
        # 1010/11, 1010/110, 100/11
        while count >= 0:
            if dividend >= divisor:
                result = result+(1 << count)
                dividend -= divisor
                divisor >>= 1
                count -= 1
            else:
                divisor >>= 1
                count -= 1

        return -result if sign else result if result <= 2**31-1 else 2**31-1


s = Solution()
print(s.divide(10, 3))