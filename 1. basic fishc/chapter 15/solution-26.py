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
# 再根据开始角度, 和持续角度, 从这个椭圆里取一部分, 注意持续角度是在start的基础上再去加
arc = c.create_arc(10, 10, 10+180, 10+180, start=45, extent=330, fill='red')

# BitmapImage或者PhotoImage
p = PhotoImage(file="img/cute.gif")
# 这里的anchor表示把图片的哪个位置订到(200, 0)这个点上, 有点像place布局
# 这里tag可以指定一个, 直接引号括起来, 也可以指定多个, 用tuple格式
pic = c.create_image(200, 0, anchor=NW, image=p, tag=("pic", "pic2"))

# 加入其它组件, 这里print输出1, 2, 3, 说明canvas的create_xxx返回的是组件的数字id
button = Button(text="点我", command=lambda: print(arc, pic, but))
but = c.create_window(500, 100, anchor=NW, window=button)

# 这里的arc, pic, but实际是1, 2, 3, 即画布对象的ID
# 画布可以通过这个进行coords(), itemconfig(), move()等
# 除了通过数字去确定, 还可以通过tag, 比如预定义的ALL和CURRENT
# 这里把鼠标移到弧形上面点击左键, 弧形颜色会变黑
# 不建议直接把事件绑定到canvas上, 比如这里, 给canvas绑定左键点击事件
# 点击时将光标指向的元素置fill属性, 但是有时候指向的元素并没有fill属性
c.bind('<Button-1>', lambda e: c.itemconfig(CURRENT, fill=random.choices(['black', 'yellow', 'red', 'green'])))

# 除了整个画布绑定事件, 还可以给单个元素绑定事件, 好像没发现能直接通过元素id绑定事件的函数
# 得先在创建元素的时候指定tag属性, 再用tag_bind方法给该元素绑定事件
c.tag_bind("pic", '<Enter>', lambda x: print(x))
root.mainloop()