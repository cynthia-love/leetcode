# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    事件绑定
"""
from tkinter import *
root = Tk()
root.geometry('300x300')

frame = Frame(root, height=100, width=300, bg='red')
frame.pack()
# 绑定鼠标左键点击事件
frame.bind('<Button-1>', lambda e: print(e.x, e.y))

frame = Frame(root, height=100, width=300, bg='green')
frame.pack()
# 绑定键盘事件
frame.bind('<Key>', lambda e: print(e))
frame.focus_set()  # 得先获得焦点才能接收键盘事件; 或者设置takefocus为True, 然后用Tab移动焦点
# <KeyPress event keysym=d keycode=100 char='d' x=-5 y=-150>

frame = Frame(root, height=100, width=300, bg='yellow')
frame.pack()

frame = Frame(root, height=100, width=300, bg='blue')
frame.pack()

root.mainloop()