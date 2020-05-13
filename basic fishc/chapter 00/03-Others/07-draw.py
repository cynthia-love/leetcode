# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    接收含两个变量的.npz格式文件, 需要指定文件名, x变量名称(默认"x"), y变量名称(默认"y")
    -t 标题, -xl 横坐标, -yl 纵坐标, -pt 尖点阙值, -pc 尖点需要大于前后几个值

    os.system("python draw.py {} -x {} -y {} -t {} -xl {} -yl {} -pt {} -pc {}".
          format("文件名.npz", "自变量名", "因变量名", "图像标题", "横坐标", "纵坐标", "均值几倍作为极点", "前后几个都小于作为极点"))
"""
import sys
import numpy as np
import matplotlib.pyplot as pt


def cmp(l: list, i: int, n: int):
    for k in range(i - 1, max(i - n - 1, -1), -1):
        if l[k] >= l[i]:
            return False
    for k in range(i + 1, min(i + n + 1, len(l)), 1):
        if l[k] >= l[i]:
            return False

    return True


if len(sys.argv) <= 1:
    print("请指定有效的.npz格式文件名!")
    sys.exit(1)

x, y = "x", "y"  # 默认横坐标, 纵坐标变量名为x, y
title, xlabel, ylabel = "", "", ""  # 默认不指定标题, 横坐标, 纵坐标
peak_t, peak_c = 1.5, 1

if "-x" in sys.argv:
    index = sys.argv.index("-x")
    if index + 1 <= len(sys.argv) - 1:
        x = sys.argv[index + 1]
    else:
        print("请指定有效的自变量名!")
        sys.exit(1)

if "-y" in sys.argv:
    index = sys.argv.index("-y")
    if index + 1 <= len(sys.argv) - 1:
        y = sys.argv[index + 1]
    else:
        print("请指定有效的因变量名!")
        sys.exit(1)

if "-t" in sys.argv:
    index = sys.argv.index("-t")
    if index + 1 <= len(sys.argv) - 1:
        title = sys.argv[index + 1]
    else:
        print("请指定有效图像名!")
        sys.exit(1)

if "-xl" in sys.argv:
    index = sys.argv.index("-xl")
    if index + 1 <= len(sys.argv) - 1:
        xlabel = sys.argv[index + 1]
    else:
        print("请指定有效横坐标标签!")
        sys.exit(1)

if "-yl" in sys.argv:
    index = sys.argv.index("-yl")
    if index + 1 <= len(sys.argv) - 1:
        ylabel = sys.argv[index + 1]
    else:
        print("请指定有效纵坐标标签!")
        sys.exit(1)

if "-pt" in sys.argv:
    index = sys.argv.index("-pt")
    if index + 1 <= len(sys.argv) - 1:
        peak_t = float(sys.argv[index + 1])
    else:
        print("请指定有效尖点阈值!")
        sys.exit(1)

if "-pc" in sys.argv:
    index = sys.argv.index("-pc")
    if index + 1 <= len(sys.argv) - 1:
        peak_c = int(sys.argv[index + 1])
    else:
        print("请指定尖点前后数量!")
        sys.exit(1)

data = np.load(sys.argv[1])

x, y = data[x], data[y]

pt.figure(figsize=(12, 12 * 0.618))

pt.title(title)
pt.xlabel(xlabel)
pt.ylabel(ylabel)

pt.plot(y)  # 这里不要plot(x, y), x为字符串类型, 是为了做tick显示用的

step = len(x) // 10 + 1  # len(x) == len(y)
range_x = range(0, len(x), step)
mark_x = [str(x[i]) for i in range(0, len(x), step)]  # 为了保险对x又进行了一次str转化
pt.xticks(range_x, mark_x)  # 哪些x点上显示什么值

# 对于折线图的上顶点加标注，超过一定阙值, 且是尖点才加
t_y = np.mean(y) * peak_t
for i in range(len(y)):
    if y[i] >= t_y and cmp(y, i, peak_c):
        pt.annotate(str(x[i]), xy=(i, y[i]), xytext=(-20, 10),
                    textcoords="offset pixels", color="red")

pt.show()
