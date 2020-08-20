# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    罚抄作业
    "I will never spam my friends again."
    写100次
    允许有8次不同的随机输入错误(错误不计入100)
"""

target = "I will never spam my friends again."
count = 0
error = set()

while count < 10:
    s = input("请输入作业: ")
    if s == target:
        count += 1
    else:
        error.add(s)
        if len(error) > 8:
            print("You lose!")
            break
