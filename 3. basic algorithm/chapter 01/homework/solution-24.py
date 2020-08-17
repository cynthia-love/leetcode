# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    计算字符串中元音字母的个数
"""

def f(s: str) -> int:
    r = {'a', 'e', 'i', 'o', 'u'}
    res = 0
    for each in s:
        if each in r:
            res += 1
    return res

print(f("helloworld"))

def f2(s: str) -> int:
    r = {'a', 'e', 'i', 'o', 'u'}
    f = [x for x in s if x in r]
    return len(f)
print(f2("helloworld"))