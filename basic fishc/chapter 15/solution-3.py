# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Label组件详解
    可文字, gif图片, 或两者结合
"""

from tkinter import *

class App:

    def __init__(self, parent):

        # txt = "您所下载的影片含有未成年人限制内容, 请满18岁后再点击观看!"
        # label1 = Label(parent, text=txt)
        # label1.pack(side=LEFT)

        """
        首先, Label组件只支持.gif格式的图片
        其次, 这里的img不能是临时变量, 比如把self.img改成img图片就渲染不出来了, 很奇怪
        而且把PhotoImage写到label2里也不行...奇了怪了, 好像只能像下面这么写
        而上面的text可以看到, txt前并没加self也能正常显示...
        """
        # self.img = PhotoImage(file='img/demo.gif')
        # label2 = Label(parent, image=self.img)
        # label2.pack(side=RIGHT)

        """
        text和image可以混合到一起
        """
        self.img3 = PhotoImage(file='img/cute.gif')
        # justify换行后左对齐, padx文字右移一点, fg文本颜色, compound混合模式, 不指定文字出不来
        label3 = Label(parent, text="带换行的图片文字混合演示\n这里是第二行", font=("楷体", 12),
                       justify=LEFT, padx=10, image=self.img3, compound=CENTER)  # CENTER表示混到图片中间
        label3.pack(side=RIGHT)

root = Tk()

app = App(root)

root.mainloop()