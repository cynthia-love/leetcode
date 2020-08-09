# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    颜色选择框
"""
from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry('300x300')

label = Label(text="这里是label")
label.pack()

def f():
    # 第一个参数为默认选中颜色
    # parent为对话框显示在哪个窗口上, 默认显示在根窗口上
    color = askcolor("#5df351", title='颜色', parent=root)
    print(color)  # ((139.54296875, 255.99609375, 136.53125), '#8bff88')
    # 不选会是(None, None), bg=None好像不会改变原颜色, 要保险的话加个if判断
    label.config(bg=color[1])  # 这里好像不能用color[0], 只能用color[1], 实际上是一种颜色的两种写法

Button(root, text='选择颜色', command=f).pack()


root.mainloop()