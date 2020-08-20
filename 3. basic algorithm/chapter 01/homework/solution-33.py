# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    支持复位和清除的计算器
    输入r复位输入c清除
"""

exp = ""
while True:
    s = input("Enter...")
    if s == "r":
        exp = ""
    elif s == 'c':
        exp = exp[:-1]
    elif s == "=":
        print(eval(exp))
    else:
        exp += s
