# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Entry组件, 输入框
"""
from tkinter import *

class MInput:

    def __init__(self, parent):

        self.state = {
            'username': StringVar(),
            'password': StringVar()
        }

        # tkinter支持三种布局方式, pack(), grid(), place(); grid()是以表格的形式管理
        Label(parent, text="账号: ").grid(row=0, column=0)
        Entry(parent, textvariable=self.state['username']).grid(row=0, column=1, padx=10, pady=5)

        Label(parent, text="密码: ").grid(row=1, column=0)
        # show='*'可以隐藏密码
        Entry(parent, textvariable=self.state['password'], show='*').grid(row=1, column=1, padx=10, pady=5)


    def getState(self):
        return self.state['username'].get(), self.state['password'].get()

    def clear(self):
        self.state['username'].set("")
        self.state['password'].set("")


root = Tk()
f1 = Frame(root)
f1.pack()
minput = MInput(f1)

f2 = Frame(root)
f2.pack()

# sticky相当于pack()布局中的anchor, 设置组件在网格中的对齐方式（前提是有额外的空间）
Button(f2, text="获取信息", width=10, command=lambda :print(minput.getState())).grid(row=0, column=0, padx=10, pady=5, sticky='e')
Button(f2, text="清除信息", width=10, command=minput.clear).grid(row=0, column=1, padx=10, pady=5)
Button(f2, text="退出", width=10, command=root.quit).grid(row=0, column=2, padx=10, pady=5, sticky='w')

root.mainloop()


