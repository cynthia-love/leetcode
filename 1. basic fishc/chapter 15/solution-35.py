# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Toplevel组件, 可以理解成子Tk(), 是一种顶层窗口
"""

from tkinter import *

root = Tk()
root.title("基本窗口")
root.geometry("300x300")

tl = None  # 指向最后一个顶层窗口

def f():
    global tl
    t = Toplevel()
    t.title("新的顶层窗口")
    Label(t, text="提醒!").pack()
    tl = t


Button(root, text="点我", command=f).pack()

# tl.attributes单个参数表示打印, 两个参数表示设置
Button(root, text="透明", command=lambda : print(tl.attributes('-alpha')) and tl.attributes('-alpha', 0.5)).pack()

root.mainloop()