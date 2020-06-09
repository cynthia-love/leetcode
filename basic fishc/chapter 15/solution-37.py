# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Event对象
"""
import random
from tkinter import *
root = Tk()

frame = Frame(root, height=100, width=300, bg='blue')
frame.pack()
frame.focus_set()

"""
e.widget, 产生该事件的组件
e.type, 事件类型, 比如KeyPress
e.char, 按键对应的字符, 比如空格键对应' '
e.keysym, 按键的系统名, 比如空格键为space, 上键为Up
注意, 没按Caps, H键的字符和名字都是h
而按了, 不光字符变成了H, 按键名也变成了H
"""
frame.bind('<Key>', lambda e: print(e.widget, e.type, e.x, e.y, e.char, e.keysym)
                              or e.widget.config(bg=random.choices(['yellow', 'red', 'green', 'blue'])))



root.mainloop()