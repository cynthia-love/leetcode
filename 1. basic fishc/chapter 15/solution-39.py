# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    grid
    比frame+pack方便的多
"""

from tkinter import *

root = Tk()

# grid里对应anchor的是sticky, 表示放在所占空间的什么位置, 有点类似anchor
# 注意这里的column是从0开始的, 而text里的column是从1开始的
Label(root, text='用户名').grid(row=0, sticky='w', column=0)
Label(root, text='密码').grid(row=1, sticky='w', column=0)

Entry(root).grid(row=0, column=1)
Entry(root, show='*').grid(row=1, column=1)

# 跨多个网格
img = PhotoImage(file='img/demo.gif')
Label(root, image=img, width=30, height=30).grid(row=0, rowspan=2, column=2)

Button(text="提交", width=30).grid(row=2, column=0, columnspan=3)

root.mainloop()