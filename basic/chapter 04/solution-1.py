# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第4章 了不起的分支和循环
"""

"""
    分数分段
"""

score = int(input("请输入您的分数: "))

if 100 >= score >= 90:
    print("A")
elif 90 > score >= 80:
    print("B")
elif 80 > score >= 70:
    print("C")
elif 70 > score >= 60:
    print("D")
elif 60 > score >= 0:
    print("E")
else:
    print("输入错误!")


# 也可以这么写, 想想为什么, else天然带not条件
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 0:
    print("E")
else:
    print("输入错误!")
