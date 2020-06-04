# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Canvas还可以绘制文本， 圆， 多边形
"""

from tkinter import *
root = Tk()
# *******************************************************************************************************
c = Canvas(root, width=800, height=800)
c.pack()
c.create_line(0, 400, 800, 400, fill="red", width=3)
c.create_line(400, 0, 400, 800, fill='red', width=3)

# 画圆， 参数同矩形， 对角点， 在矩形内画圆， 正方形则是圆否则是椭圆
c.create_oval(400, 0, 800, 400, fill='green')

c.create_text(200, 200, text="FishC")






# *******************************************************************************************************
root.mainloop()