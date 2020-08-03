# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    详解结果对象
"""

import re

# 先说search, 返回一个匹配结果

res = re.search(r"(abc)(def)", "abcdef")
print(res)  # <_sre.SRE_Match object; span=(0, 6), match='abcdef'>
print(res.group())  # abcdef, 直接调, 不给索引, 则输出整个正则匹配结果, 相当于group(0)
print(res.span())  # (0, 6)
print(res.start())  # 0
print(res.end())  # 6

print(res.groups())  # ('abc', 'def'), 注意只有groups, 没有spans; 返回各子匹配

print(res.group(1))  # abc, 第一个子组
print(res.span(1))  # (0, 3)
print(res.start(1))  # 0
print(res.end(1))  # 3


# 再说findall; 慎用, 尤其带括号的时候; 还是finditer好
# 也不尽然, 括号用好了, findall更简洁
res = re.findall(r"abc", "abcefgabcdabc")
print(res)  # ['abc', 'abc', 'abc'], 怎么不是对象了; 有时候只需要结果不需要span, 且不需要总的串, 只需要个别子组, 用findall也不是不行
print(type(res))  # <class 'list'>...直接就是个list???
# 没括号的时候, findall默认返回全部匹配串

res = re.findall(r"x(a)(b)(c)", "xabcefgxabcdxabc")
print(res)  # [('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c')]
# 带子组的情况findall会给把子组全拆了???子组外面的东西就没了???x呢???
# 想要获得完整匹配串其实也简单, (x(a)(b)(c)), 强制把整个作为一个子组就行了
# 有时候要提取位置的匹配结果
for each in res:
    print(each[2])

# 最后说说finditer
res = re.finditer(r"aba", "ababacaba")
print(res)  # <callable_iterator object at 0x000000000217C2B0>
print(list(res))   # [<_sre.SRE_Match object; span=(0, 3), match='aba'>, <_sre.SRE_Match object; span=(6, 9), match='aba'>]
# finditer相当于多个search, 单号注意这里ababa, 只会匹配前面的aba, 之后指针就后移了, 不会匹配2-4的aba!!!
# print(res)
# print(list(res))  # 奇了怪了, 这里怎么没了....注意迭代器next之后, 好像没办法把指针再退回一步或者退到开头
# 不管了, 先分析迭代元素
res = re.finditer(r"ab(a)", "ababacaba")
for o in res:
    print(o.group(), o.span())  # 对于迭代器中的每一项, 就和search, match的搜索结果对象没什么区别了
    print(o.span(1))