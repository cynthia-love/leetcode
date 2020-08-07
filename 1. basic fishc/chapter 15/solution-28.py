# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    任意位置弹出菜单而不是嵌到最上面
"""

from tkinter import *
root = Tk()

menu = Menu()
menu.add_command(label="复制", command=lambda : print("复制"))
menu.add_command(label="粘贴", command=lambda : print("粘贴"))
m2 = Menu()
menu.add_cascade(label="更多", menu=m2)
m2.add_command(label="哈哈", command=lambda : print("哈哈"))

# 菜单嵌入最上方用root.config, 而弹出是menu自己pop(位置)

# e.x, e.y是相对于窗口, 而e.x_root, e.y_root是相对于整个屏幕
# 这里要用x_root, y_root, 想一下为什么
root.bind("<Button-2>", lambda e: menu.post(e.x_root, e.y_root))


root.mainloop()