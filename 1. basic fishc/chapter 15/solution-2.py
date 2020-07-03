# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    进阶版本, 独立成一个App组件, 随时可以加到其他容器组件中去
"""
import random
import tkinter as tk

"""
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

"""

# 再封装个相对复杂的, frame套button, 点击打印文字
# 如果想变更组件上文字呢?这里好像不能像react, vue那样通过声明个self.xxx变量, 实现动态更新渲染
class App:
    def __init__(self, parent):

        # frame一般用在复杂布局中将组件分组
        frame = tk.Frame(parent)
        frame.pack(side='left', padx=10, pady=10)  # side指定大概偏移位置后, 可用padx, pady微调

        self.button = tk.Button(frame, text="hahaha", fg='blue', bg='yellow', command=self.swap)
        self.button.pack()

    def swap(self):
        print("按钮被点击!~~~")

window = tk.Tk()
app = App(window)
window.mainloop()