# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    延续solution-5, 继续演示另一种父子组件传参方式
    command函数还是父组件传, 只不过触发时调子组件的方法获取状态
    相对来讲, 这种方法比solution-5更好, 毕竟选中状态数组只有在子组件内部才用
    父组件不关心选中状态数组, 只关心传入选项列表, 获得的也是选项列表
"""


from tkinter import *

class Choice:
    """
    传入父组件, 选项列表, onchange函数; 这么传可以让父组件获取子组件状态
    """
    def __init__(self, parent, values: list, onchange):

        self.values = values
        self.checked = [IntVar() for x in range(len(self.values))]

        for i in range(len(self.values)):
            cb = Checkbutton(parent, text=self.values[i], variable=self.checked[i], command=onchange)
            # side控制摆放在四个方向的大致位置，然后anchor可以控制控件放置在side确定的区域内的某个位置。
            # side有四个取值, top, bottom, left, right, 有先来后到之分, 默认为top
            # 四个top相当于没指定, 体会一下, side会在剩余未占部分找top, bottom, left, right
            cb.pack(side='top', anchor='w')

    def getChoice(self):
        return [self.values[i] for i in range(len(self.values)) if self.checked[i].get() == 1]

class MyFrame:
    def __init__(self, parent):
        self.girl = ["西施", "王昭君","貂蝉", "杨玉环"]

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
        if girl:
            self.text.set("已选: "+'、'.join(girl))
        else:
            self.text.set("请挑选妃子~")

root = Tk()
root.geometry('500x500+400-100')  # 宽x高+/-padx+-/pady
root.resizable(False, False)
frame = MyFrame(root)
root.mainloop()