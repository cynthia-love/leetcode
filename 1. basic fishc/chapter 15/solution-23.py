# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Canvas, 用于显示图形(直线, 矩形, 文本等)
    (Text里也可以展示文本, 图片, 其他组件, 但不是自己画的, 是外部引入的)
    显示完还可以移动，调整样式，删除
"""

from tkinter import *
root = Tk()

c = Canvas(root, width=600, height=600)
c.pack()

# 也可以用*(x1, x2)甚至(x1, x2)这种形式, 便于理解, 表示一个点
# create_line实际上就是指定一个起点一个终点
# 注意canvas里的fill区别于tkinter其他组件里的fill
l1 = c.create_line((0, 50), (200, 50), fill='green')
l2 = c.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))  # dash可以实现画虚线

# 矩形指定对角两个点就行
r1 = c.create_rectangle((50, 25), (150, 75), fill='blue')

# coords后面2个/4个参数实际上还是指定的线段l1的起始截止位置, 甚至长度也可以变, 那还叫移动吗, 跟重画差不多了
Button(root, text='调整位置', command=lambda: c.coords(l1, (0, 25), (300, 25))).pack(side='left')
Button(root, text='改变颜色', command=lambda: c.itemconfig(r1, fill='black')).pack(side='left')
Button(root, text='删除', command=lambda: c.delete(l2)).pack(side='left')
# 特别地， delete函数有内置关键字ALL, 表示清空画布； CURRENT表示鼠标指针指向的对象
# 另外, 当delete的对象已经删除时, 重复点击并不会报错

root.mainloop()

