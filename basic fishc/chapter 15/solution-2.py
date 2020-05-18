# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    进阶版本, 独立成一个App组件, 随时可以加到其他容器组件中去
"""
import random
import tkinter as tk

class App:

    def __init__(self, parent):
        label = tk.Label(parent, text="这里是文本", bg=random.choice(["green", "yellow", "red", "blue"]))
        label.pack()

window = tk.Tk()

frame = tk.Frame(window)
frame.pack()

f_l = tk.Frame(frame)
f_r = tk.Frame(frame)
f_l.pack(side='left')
f_r.pack(side='right')

a_l = App(f_l)
a_r = App(f_r)  # 封装之后再重复添加就非常简单了

window.mainloop()