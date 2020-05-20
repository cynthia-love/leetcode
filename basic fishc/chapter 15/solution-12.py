# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    自己封装一个更好用的Listbox组件
    传入list, 支持[xx, xx]和[(id, value)]两种传入方式, 返回[(index, value)]
"""

from tkinter import *

class MListbox:

    def __init__(self, parent, values, side=TOP, height=10):
        if values and isinstance(values[0], tuple):
            self.values = values
        else:
            self.values = list(enumerate(values))

        # 由于Listbox里面有俩组件, 为了保证整体性, 内部套一个frame
        frame = Frame(parent)
        frame.pack(side=side)

        self.lb = Listbox(frame, setgrid=True, height=height, selectmode=EXTENDED)
        for item in self.values:
            self.lb.insert(END, item[1])
        self.lb.pack(side=LEFT, fill=BOTH)

        sb = Scrollbar(frame, command=self.lb.yview)
        sb.pack(side=RIGHT, fill=Y)

        self.lb.config(yscrollcommand=sb.set)


    def getChoices(self):
        return [self.values[i] for i in self.lb.curselection()]


root = Tk()
mlb = MListbox(root, ['鸡蛋', '鸭蛋', '鹅蛋', '李狗蛋', '蛋蛋1', '蛋蛋2'], TOP, 5)

bt = Button(root, text="点我看选中了啥", command=lambda x=mlb: print(x.getChoices()))
bt.pack(side=BOTTOM)

root.mainloop()