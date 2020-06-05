# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Canvas其它补充
"""
import random
from tkinter import *
root = Tk()

c = Canvas(width=600, height=600, background='yellow')
c.pack()

# 弧形本质上是画椭圆, 也是指定矩形对角俩点, 然后以矩形中心为中心, 画一个内切椭圆
# 再根据开始角度, 和持续角度, 从这个椭圆里取一部分
arc = c.create_arc(10, 10, 190, 190, start=45, extent=330, fill='red')

# BitmapImage或者PhotoImage
p = PhotoImage(file="img/cute.gif")
pic = c.create_image(200, 0, anchor=NW, image=p)

# 加入其它组件
button = Button(text="点我", command=lambda: print(arc, pic, but))
but = c.create_window(500, 100, anchor=NW, window=button)

# 这里的arc, pic, but实际是1, 2, 3, 即画布对象的ID
# 画布可以通过这个进行coords(), itemconfig(), move()等
# 除了通过数字去确定, 还可以通过tag, 比如预定义的ALL和CURRENT
# 这里把鼠标移到弧形上面点击左键, 弧形颜色会变黑
c.bind('<Button-1>', lambda e: c.itemconfig(CURRENT, fill=random.choices(['black', 'yellow', 'red', 'green'])))

root.mainloop()