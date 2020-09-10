# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    读入一个文件, 统计文档中每个字母的频次, 画出柱状图
"""
import matplotlib.pyplot as plt

filename = "solution-33.py"

with open(filename, "r") as f:
    data = f.read().lower()
    keys = [chr(ord('a')+i) for i in range(26)]  # 字母枚举, 记住这种写法
    d = dict.fromkeys(keys, 0)

    for each in data:
        if each in d:
            d[each] += 1

    plt.figure(figsize=(8, 5))
    plt.title("Hello world")
    plt.bar(d.keys(), d.values())

    for x, y in d.items():
        plt.text(x, y+0.3, y, ha='center')

    plt.show()