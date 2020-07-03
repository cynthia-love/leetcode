# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Canvas, 用于显示图形(直线, 矩形, 文本等)
    显示完还可以移动，调整样式，删除
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

Button(root, text='调整位置', command=lambda: c.coords(l1, 0, 25, 200, 25)).pack(side='left')
Button(root, text='改变颜色', command=lambda: c.itemconfig(r1, fill='black')).pack(side='left')
Button(root, text='删除', command=lambda: c.delete(l2)).pack(side='left')
# 特别地， delete函数有内置关键字ALL, 表示清空画布； CURRENT表示鼠标指针指向的对象

root.mainloop()

