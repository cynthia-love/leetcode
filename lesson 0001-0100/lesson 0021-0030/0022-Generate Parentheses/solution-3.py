# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法3, 闭合数(概念有点难理解)
    一对括号: ()
    两对括号: 一对(), (一对), ()一对
    三对括号: 两对(), 一对(一对), (两对), (一对)一对, (), 两对
    n对括号: n-1对(), n-2对(1对), n-3对(2对)...
    看出规律了吗, 其实就是n-1对括号在1(2)3, 3个位置枚举
    在这个思路的基础上, 动态规划, 把每一个组合都记住, 并利用{}去重

    这里其实还要优化空间, 不用在3个位置枚举, 在两个位置枚举即可
    1(2)3, x(y)z->(x-1)(y)(z-1)->(x+y)z
"""
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        mem = {}

        def rf(n):
            if n in mem:
                return mem[n]
            if n == 0:
                return {""}
            if n == 1:
                return {"()"}

            ans = set()
            for i in range(n):
                # 这里别忘了-1, 因为已经有一个()了
                j = n-1-i
                ans |= {"({}){}".format(x, y) for x in rf(i) for y in rf(j)}

            mem[n] = ans
            return mem[n]

        return rf(n)


s = Solution()
print(s.generateParenthesis(3))
