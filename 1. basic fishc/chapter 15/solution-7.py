# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Radiobutton单选组件, 和多选的区别在于, 选中状态是单个值而不是一个list, 每一项的onvalue不能相同(这里的变量名是value)
    多选的选中状态为[0, 1, 0, 1, 0], 单选的选中状态为 3, 即单个int
"""

from tkinter import *

class MRatio:
    def __init__(self, parent, choices, command):
        if choices and isinstance(choices[0], tuple):
            self.choices = choices
        else:
            self.choices = list(enumerate(choices))

        self.command = command

        self.chosen = IntVar()

        for id, value in self.choices:
            # 这里的value等价于Checkbutton里的onvalue; indicatoron可以隐藏前面的圆圈
            choice = Radiobutton(parent, text=value, value=id+1, variable=self.chosen, command=self.command, indicatoron=False)
            choice.pack(anchor='w')

    def getState(self):
        for item in self.choices:
            if item[0]+1 == self.chosen.get():
                return item
        return None

class MFrame:
    def __init__(self, parent):
        # LabelFrame可以在框上面加文字, 且默认边框可见, 其他和frame一样
        f_l = LabelFrame(parent, text="这里是LabelFrame", padx=5, pady=5)
        f_l.pack(side='top')

        f_r = Frame(parent)
        f_r.pack(side='top')

        self.choices = [(101, '貂蝉'), (102, '西施'), (103, '闭月'), (104, '羞花')]
        self.ratio = MRatio(f_l, self.choices, self.command)

        self.text = StringVar()
        self.text.set("请挑选~")
        label = Label(f_r, textvariable=self.text, fg='red', justify='left')
        label.pack(anchor='center')

    def command(self):
        print(self.ratio.getState())
        self.text.set(self.ratio.getState()[1])

root = Tk()
root.geometry('500x500+400-100')  # 宽x高+/-padx+-/pady
root.resizable(False, False)
frame = MFrame(root)

root.mainloop()