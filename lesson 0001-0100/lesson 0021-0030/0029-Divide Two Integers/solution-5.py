# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法5, 大神的5行神仙解法, 学习一下
"""


class Solution:
    def divide2(self, dividend: int, divisor: int) -> int:
        a, b, r, t = abs(dividend), abs(divisor), 0, 1
        while a >= b or t > 1:
            if a >= b: r += t; a -= b; t += t; b += b
            else: t >>= 1; b >>= 1

        print([dividend ^ divisor >= 0])
        print((-r, r)[dividend ^ divisor >= 0])
        return min((-r, r)[dividend ^ divisor >= 0], (1 << 31) - 1)


    def divide(self, dividend: int, divisor: int) -> int:
        dd, dr, r, c = abs(dividend), abs(divisor), 0, 0


        while dd >= dr or c > 0:
            print(bin(dd), bin(dr), r, c)
            if dd >= dr:
                dd, dr, r, c = dd-dr, dr << 1, r+(1 << c), c+1
            else:
                c -= 1
                dr >>= 1

        """
            有点绕, 以1000/3十进制为例
            和之前的方法先提前算出来最大位移位数相比, 此法不先算出来
            而是先计算当前, 然后一有机会就往大了窜
            
            1000, 3, 位移0->1000-3, 30, 1, 位移1
            
            997, 30, 位移1->997-30, 300, 1+10, 位移2
            
            697, 300, 位移2, 697-300, 3000, 11+100, 位移3
            
            397 < 3000, 397, 300, 位移2
            
            397, 300, 397-300, 3000, 111+100, 位移3
            
            97 < 3000, 97, 300, 位移2
            
            97 < 300, 97, 30, 位移1
            
            97, 30, 位移1, 97-30, 300, 211+10, 位移2
            
            37 < 300, 位移2, 30, 位移1
            37, 30, 位移1, 37-30, 300, 位移2
        """




s = Solution()
print(s.divide(100, 3))

x = [1, 2]
y = [3]
print([88, 8][False])

from requests.cookies import RequestsCookieJar

cookie = RequestsCookieJar()

from requests.cookies import cookiejar_from_dict



