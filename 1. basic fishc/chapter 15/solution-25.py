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

# 双击左键Double-Button-1, 这里Double是modifier, Button是type, 1是detail
# 但是左键移动B1-Motion, B1成了modifier, 主体type是Motion
# Motion事件有x和y参数
c.bind("<B1-Motion>", draw)  # 一般组件绑定事件是bind, text里是tag_bind

Label(root, text="按住鼠标左键滑动绘画").pack(side=BOTTOM)

# *********************************************************
root.mainloop()