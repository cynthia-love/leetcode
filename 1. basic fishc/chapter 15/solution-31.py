# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    OptionMenu组件
    除了往Menu里一个个添加radiobutton实现单选菜单, 还可以直接用OptionMenu
    区别于radiobutton的是, radiobutton里选中的是id, 这里直接是字符串值
"""
from tkinter import *
root = Tk()

options = ['one', 'two', 'three']

var = StringVar()
var.set(options[0])

om = OptionMenu(root, var, *options)
om.pack()

Button(root, text='点我', command=lambda :print(var.get())).pack()

root.mainloop()