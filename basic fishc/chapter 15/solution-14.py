# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Text组件, 可用于显示多行文本, 可作为简单文本编辑器, 网页浏览器
    Text不光支持插入文本, 还支持插入图片, 其他组件(类似于frame)
"""

from tkinter import *

root = Tk()

text = Text(root, width=50, height=20)
text.pack()

# 没找到能直接指定text值的属性, 只能用insert插入
# 注意, text的插入不是一行行插的, 更像是文件指针的感觉
text.insert(INSERT, 'I love \n')  # INSERT表示光标位置, 不过这种自动插的光标肯定在最后, 所以和END没啥区别
text.insert(END, "FishC.comddddddddddddddddddddddddddddddddddddddd\n")  # 不指定\n, 到组件宽度上限后也会自动换行

pic = PhotoImage(file='img/demo.gif')

def showImg():

    # 这里如果光标选某个位置, 再点按钮, 就能把图片插到相应位置
    text.image_create(INSERT, image=pic)

# Text里还支持插入image对象和Tkinter组件, 可以把它想象成frame
button = Button(text, text= '点我点我', command = showImg)
# button.pack(), 这里不能这么调, 外部组件并不清楚Text组件相对位置
text.window_create(END, window=button)

root.mainloop()



