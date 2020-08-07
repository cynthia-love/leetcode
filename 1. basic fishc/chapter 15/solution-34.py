# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    PanedWindow, 类似于Frame
    但Frame只能跟着窗体整体扩大缩小, 而PanedWindow可以调整相对的空间划分
    像是PyCharm的界面就类似于PanedWindow
    比如左侧的Project就是Horizontal划分, 然后可以动态拖动
"""

from tkinter import *

root = Tk()
root.geometry("300x300")

# 注意这里的orient的意义, 这里水平, 只的是后续add组件, 水平排, 可以添加多个
pw = PanedWindow(orient=HORIZONTAL, showhandle=True, sashrelief=SUNKEN)
pw.pack(fill=BOTH, expand=True)
label = Label(pw, text="left")
pw.add(label)  # PanedWindow下的组件时通过其add方法添加的
# 这种情况下在初始化组件的时候, 就可以把首参数parent window省了
# 比如这里的Label写法和下面的Label写法都是可以的

# 这里竖直排
pw2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
pw.add(pw2)

pw2.add(Label(text="上方"))
pw2.add(Label(text="下方"))
pw2.add(Label(text="下方"))
# 排了三个会出现2条分割线; 即分割几块是根据add了多少个元素

root.mainloop()