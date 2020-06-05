# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Canvas实现手写
"""
from tkinter import *

root = Tk()
# *********************************************************
c = Canvas(width=500, height=300, background='white')
c.pack()
r = 1.0
def draw(e):
    c.create_oval(e.x-r, e.y-r, e.x+r, e.y+r, fill='red', outline='red')

c.bind("<B1-Motion>", draw)

Label(root, text="按住鼠标左键滑动绘画").pack(side=BOTTOM)

# *********************************************************
root.mainloop()