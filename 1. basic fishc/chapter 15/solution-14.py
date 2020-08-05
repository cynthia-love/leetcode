# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Text组件, 可用于显示多行文本, 可作为简单文本编辑器, 网页浏览器
    Text不光支持插入文本, 还支持插入图片, 插入其他组件(即和canvas类似 也具有容器功能)
    插入文本insert, 插入图片image_create, 插入组件window_create
"""

from tkinter import *
root = Tk()
# ******************************************************************************************************************

text = Text(root, width=50, height=20)
text.pack()

# 没找到能直接指定text值的属性, 只能用insert插入
# 注意, text的插入不是一行行插的, 需要手动加\n或者等超长自动换行
text.insert(INSERT, 'I love \n')  # INSERT表示光标位置, 不过这种自动插的光标肯定在最后, 所以和END没啥区别
text.insert(END, "FishC.comddddddddddddddddddddddddddddddddddddddd\n")  # 不指定\n, 到组件宽度上限后也会自动换行

pic = PhotoImage(file='img/demo.gif')

def showImg():

    # 这里如果光标选某个位置, 再点按钮, 就能把图片插到相应位置；插入图片用的不是insert而是image_create
    text.image_create(INSERT, image=pic)

# Text里还支持插入其它Tkinter组件, 可以把它想象成frame，注意这里不能让组件自己pack，像插入图片一样，Text有自己的方法
button = Button(text, text= '点我点我', command = showImg)
# button.pack(), 这里不能这么调, 外部组件并不清楚Text组件相对位置
text.window_create(END, window=button)

# ******************************************************************************************************************
root.mainloop()



