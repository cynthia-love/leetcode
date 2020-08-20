# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    模拟简单计算器
    每一次输入做一个单独的行
    可以输入数字或者操作符比如+, =
    每一次输入完毕后, 显示处理结果
"""

exp = ""
while True:
    s = input("Enter...")
    if s == "=":
        print(eval(exp))
    elif s in ['+', '-']:
        print(eval(exp))
        exp += s
    else:
        exp += s