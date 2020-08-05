# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Canvas还可以绘制文本， 圆， 多边形
"""
from math import *
from tkinter import *
root = Tk()
# *******************************************************************************************************
c = Canvas(root, width=800, height=800, background='pink')
c.pack()
c.create_line(0, 400, 800, 400, fill="red", width=3)
c.create_line(400, 0, 400, 800, fill='red', width=3)

# 画文字, 给的坐标应该是中心点
c.create_text(200, 200, text="FishCadfkdjfkdjfk")

# 画圆， 参数同矩形， 对角点， 在矩形内画圆， 正方形则是圆否则是椭圆
# 矩形也可以指定dash设置边框为虚线, outline控制边框颜色, fill控制内部填充颜色
c.create_rectangle(500, 150, 700, 250, dash=(4, 4), outline='red')
c.create_oval(500, 150, 700, 250, fill='green')

# 圆, pygame里的rect习惯于指定左上角的点, 然后给width, height
# (x, y), (x+width, y+height), 这么写可能更好用肉眼看些
c.create_rectangle(100, 500, 100+200, 500+200, dash=(4, 4), outline='blue')
c.create_oval(100, 500, 300, 700, fill='yellow')

# 多边形, 画个五边形, 通过中心点, 算出来上, 左上, 右上, 左下, 右下五个点
center_x, center_y, r = 500, 500, 50
points = [
    center_x - int(r * sin(0.4 * pi)), center_y - int(r * cos(0.4 * pi)),
    center_x, center_y - r,
    center_x + int(r * sin(0.4 * pi)), center_y - int(r * cos(0.4 * pi)),
    center_x + int(r * sin(0.2 * pi)), center_y + int(r * cos(0.2 * pi)),
    center_x - int(r * sin(0.2 * pi)), center_y + int(r * cos(0.2 * pi))
]
c.create_polygon(points, outline='green', fill='yellow')
# create_polygon函数要注意点的顺序, 想象自己在用笔画
# 只是点顺序不同, 上面的是五边形,下面的是五角星
center_x, center_y, r = 700, 700, 50
points = [
    center_x - int(r * sin(0.4 * pi)), center_y - int(r * cos(0.4 * pi)),
    center_x + int(r * sin(0.4 * pi)), center_y - int(r * cos(0.4 * pi)),
    center_x - int(r * sin(0.2 * pi)), center_y + int(r * cos(0.2 * pi)),
    center_x, center_y - r,
    center_x + int(r * sin(0.2 * pi)), center_y + int(r * cos(0.2 * pi))

]
# 这里把点一个个传进去和以一整个list的形式传进去都是可以的
# 这里的fill注意, 最中间的位置不会填充
c.create_polygon(*points, outline='green', fill='yellow')


# *******************************************************************************************************
root.mainloop()