# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    方法6, 与方法5类似, 还是栈, 一次遍历, 区别在于
    方法5边界位置存的是索引值, 而此方法存的是算出来的长度
    以)()())()()(为例:
    先压入0, 表示此时以字符串的最左边界, 符合条件得子串长度0
    遇到), 此时栈长度1, 说明只有一个最左边界, 没有(, 大跳重置stack
    遇到(, 压入一个新的0, 变成00, 这个0可能作为新的边界, 也可能作为(和)配对, 看下一个是什么
    遇到), 此事栈长度为2, 说明除了最左边界, 上一个遇到的是(, 那么以)为边界的右符合条件子串至少长度为2, 出栈, 加2
    遇到(, 压入栈, 变成20
    遇到), 栈长2, 配对成功, 出栈, 变4
    这里要注意一下, ()(()), 变化顺序: 0->00->2->20->200->22->6
    即上一个边界不是简单加2, 而是加上其右边一个边界算出来的长度后再加2

"""
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack, ans = deque([0]), 0
        for c in s:
            # 遇到左括号, 无脑压入
            if c == "(":
                stack.append(0)
            else:
                # 遇到), stack长1, 说明没有对应的(, 大跳
                if len(stack) == 1:
                    stack.clear()
                    stack.append(0)
                # stack长大于1, 说明有对应的(,加到上一个边界里, 再出栈
                else:
                    # val = stack.pop()
                    # stack[-1] += val+2
                    stack[-2] += stack[-1]+2
                    stack.pop()
                    ans = max(ans, stack[-1])

        return ans


s = Solution()
print(s.longestValidParentheses(")()())()()("))
