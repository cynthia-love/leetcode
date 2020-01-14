# -*- coding: utf-8 -*-
# Author: Cynthia


"""
    方法5， 栈, 只不过不是暴力法中的每次取出一定子串再去判断而是一次遍历直接得出解
    有点类似方法3, 两遍滑动窗口，只不过利用栈的特点，一遍就能处理((())()的情况，不用来第二遍了
    关键点: 存储索引, 且多存一个前置索引, 以处理|()(())的情况
    思路：初始压入-1， 遇到(将其索引压入栈，比如这里会变成-1,0,1,2
    第一次遇到),此时栈长>2, 说明有(, 出栈, 栈顶为1, 子串长3-1=2
    继续, 还是), 此时栈长>2, 说明有(, 出栈, 栈顶为0, 子串长4-0=4
    继续, (, 入栈, 变成-1, 0, 5
    继续, ), 此时栈长>2, 说明有(, 出栈, 栈顶为0, 子串长6-0=6

    再考虑特殊情况))()))
    初始压入-1
    继续, ), 此时栈长1, 说明没有(, 大跳, 出栈, 入0
    继续, ), 此时栈长1, 说明没有(, 大跳, 出栈, 入1
    继续, (, 入栈, 变成1, 2
    继续, ), 此时栈长2, 说明有(, 出栈, 栈顶为1, 子串长3-1=2
    继续, ), 此时栈长1, 说明没有(, 大跳, 出栈, 入4
    ...
"""
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack, ans = deque([-1]), 0
        for i in range(len(s)):
            # 遇到(无脑压入
            if s[i] == '(':
                stack.append(i)
            # 遇到)才需要特殊处理; 要么长度等于1, 要么大于1
            else:
                # 等于1, 更新边界, 保证边界始终是1个
                if len(stack) == 1:
                    stack.pop()
                    stack.append(i)
                # 大于等于2, 说明是边界+至少一个(
                else:
                    stack.pop()
                    ans = max(ans, i-stack[-1])
        return ans


s = Solution()
print(s.longestValidParentheses("((())((())))"))