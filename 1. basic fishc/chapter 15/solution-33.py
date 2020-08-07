# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Spinbox, 支持选择预制值的输入框, 可手输
"""
from tkinter import *

root = Tk()

options = ["选择1", "选择2", '选择3']

sb = Spinbox(root, values = options)
sb.pack()

Button(text='点我', command=lambda :print(sb.get())).pack()

var = StringVar()
var.set(0)
sb2 = Spinbox(root, from_=0, to=10, textvariable=var)
sb2.pack()

Button(text='点我', command=lambda : print(var.get())).pack()

root.mainloop()