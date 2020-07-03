# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    题目分析: 不用乘号, 除号, 模运算符计算两个数的商, 32位整数范围
    比如 100/3=33...1, 7/-3=-2...1, -7/-3=2...-1
    思路: 回忆一下十进制除法是怎么算的
       33
    3|100   从左边开始, 找到第一个大于等于3的位置, 开始除, 然后100-3*3*10=10
       9    当然, 也可以理解是100/(3*10**1), 得到的3*10**1(另一种思路, 除数左移)

    二进制思路同理, 而且更简单, 因为但凡能除得起, 这一位的商的值肯定是1(没有2,3,4等其他取值)
          10
    101|101011   注意看这里的规律, 商的1是左移3位, 算1011的时候相当于:
        101      101011-1*(101 << 3)
          0011   还要注意, 处理左移2的时候, 被除数已经是11了, 商计0, 没必要再来
                 一次 11-0*(101 << 2)
"""
"""
    先不考虑计算过程中的溢出, 都转化成正数去算
    方法1, 右移被除数
"""


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        # 如果被除数和除数符号不一致, 则flag为True
        flag = (dividend >= 0) ^ (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)

        d, count = dividend, 0
        while d >= divisor:
            d, count = d >> 1, count+1

        # count多移了一位, 这里要-1
        # count的意义为: 100右移1位可以去除以3
        count -= 1

        result = 0
        while count >= 0:

            d = dividend >> count
            if d >= divisor:
                result += 1 << count
                dividend -= divisor << count
            count -= 1

        return -result if flag else 2**31-1 if result >= 2**31 else result


s = Solution()
print(s.divide(10, 3))
