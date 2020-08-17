# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    反复从标准输入读取一行直到抛出EOFError异常, 然后以相反的顺序输出(Ctrl+D结束)
"""

res = []
try:
    while True:
        res.append(input())
except EOFError:

    # for each in res[::-1]:
    #     print(each)

    i = len(res)-1
    while i >= 0:
        print(res[i])
        i -= 1
