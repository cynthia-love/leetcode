# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Button组件
    除了多了个点击事件command, 其他和Label差不多
"""

import random
import tkinter as tk

class App:

    def __init__(self, parent):

        frame1, frame2 = tk.Frame(parent), tk.Frame(parent)

        frame1.pack(padx=10, pady=10, fill='x')
        # 前面提到组件独占空间会自动扩展, 比如side=top时, 会横向占据整行
        # 对于一般组件是这样的, 但对于frame不是, frame依赖内部组件填充
        # 想要frame占据整行, 需要显式提供fill='x', 这种情况下fill不依赖于expand=YES
        frame2.pack(padx=10, pady=10, fill='x')

        # text="xxx", 文本不可变; textvariable=StringVar(), 文字可变
        # text其实也可以实现文本可变, 用config强改就行了
        self.txt = tk.StringVar()
        self.txt.set("您所下载的影片含有未成年人限制内容, \n请满18岁后再点击观看!")
        label = tk.Label(frame1, textvariable=self.txt, justify=tk.LEFT, fg='red')
        label.pack(side=tk.LEFT)

        self.img = tk.PhotoImage(file="img/cute.gif")
        label2 = tk.Label(frame1, image=self.img, bg='green')
        label2.pack(side=tk.RIGHT)

        button = tk.Button(frame2, text="图文结合的按钮", command=self.click, image=self.img, compound=tk.CENTER)
        button.pack()



    def click(self):
        self.txt.set(random.choice(["你骗人!", "鬼扯呢你!", "哈哈继续啊!", "总算得逞了你!"]))

root = tk.Tk()
root.geometry('800x800+400-100')  # 宽x高+/-padx+-/pady
root.resizable(False, False)
app = App(root)
root.mainloop()