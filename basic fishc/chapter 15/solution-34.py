# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    PanedWindow, 类似于Frame
    但Frame只能跟着窗体整体扩大缩小, 而PanedWindow可以调整相对的空间划分
"""

from tkinter import *

root = Tk()
root.geometry("300x300")

# 注意这里的orient的意义, 这里水平, 只的是后续add组件, 水平排, 可以添加多个
pw = PanedWindow(orient=HORIZONTAL, showhandle=True, sashrelief=SUNKEN)
pw.pack(fill=BOTH, expand=1)
label = Label(pw, text="left")
pw.add(label)

# 这里竖直排
pw2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
pw.add(pw2)

pw2.add(Label(text="上方"))
pw2.add(Label(text="下方"))
pw2.add(Label(text="下方"))
# 排了三个会出现2条分割线; 即分割几块是根据add了多少个元素

root.mainloop()