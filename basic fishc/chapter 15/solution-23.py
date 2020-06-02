# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Canvas, 用于显示和编辑图形(直线, 矩形, 文本等)
"""

from tkinter import *
root = Tk()

c = Canvas(root, width=200, height=100)
c.pack()

# 也可以用*(x1, x2)这种形式, 便于理解, 表示一个点
l1 = c.create_line(*(0, 50), 200, 50, fill='green')
l2 = c.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))

# 矩形指定对角线就行
r1 = c.create_rectangle(50, 25, 150, 75, fill='blue')

root.mainloop()

