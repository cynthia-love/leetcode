# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    延续solution-5, 继续演示另一种父子组件传参方式
    command函数还是父组件传, 只不过触发时调子组件的方法获取状态
    相对来讲, 这种方法比solution-5更好, 毕竟选中状态数组只有在子组件内部才用
    父组件不关心选中状态数组, 只关心传入选项列表, 获得的也是选项列表
"""


from tkinter import *
from typing import List

class Choice:
    """
    传入父组件, 选项列表, onchange函数; 这么传可以让父组件获取子组件状态
    选项列表可以是[], 也可以是[(id, text)], 如果是前者, 自动以索引作为id
    """
    def __init__(self, parent, data: list, onchange):

        if type(data[0]) != tuple:
            self.value = list(enumerate(data))
        else:
            self.value = data

        self.checked = [IntVar() for x in range(len(self.value))]  # IntVar默认为0好像

        for i in range(len(self.value)):
            # 这里除了用默认的01表示未选/已选, 还可以自定义onvalue, offvalue; 如果是用数组索引, 考虑到0, 建议onvalue用index+1
            cb = Checkbutton(parent, text=self.value[i][1], variable=self.checked[i], command=onchange)
            # side控制摆放在四个方向的大致位置，然后anchor可以控制控件放置在side确定的区域内的某个位置。
            # side有四个取值, top, bottom, left, right, 有先来后到之分, 默认为top
            # 四个top相当于没指定, 体会一下, side会在剩余未占部分找top, bottom, left, right
            cb.pack(side='top', anchor='w')

    def getChoice(self):
        # 返回[(id, value)]
        return [self.value[i] for i in range(len(self.value)) if self.checked[i].get() == 1]

class MyFrame:
    def __init__(self, parent):
        # self.girl = ["西施", "王昭君","貂蝉", "杨玉环"]
        self.girl = [(101, "西施"), (102, "王昭君"), (103, "貂蝉"), (104, "杨玉环")]

        framel = Frame(parent)
        framel.pack(side='left')

        # 要调子组件方法获取状态这里需要加上self
        self.choice = Choice(framel, self.girl, self.onchange)

        framer = Frame(parent)
        framer.pack(side='right')

        self.text = StringVar()
        self.text.set("请挑选妃子~")
        label = Label(framer, textvariable=self.text, justify='left', fg='red')
        label.pack()

    def onchange(self):

        girl = self.choice.getChoice()
        print(girl)
        if girl:
            self.text.set("已选: "+'、'.join([x[1] for x in girl]))
        else:
            self.text.set("请挑选妃子~")

root = Tk()
root.geometry('500x500+400-100')  # 宽x高+/-padx+-/pady
root.resizable(False, False)
frame = MyFrame(root)
root.mainloop()