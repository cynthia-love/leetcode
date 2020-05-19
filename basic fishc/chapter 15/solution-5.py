# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Checkbutton组件, 多选
    注意, 虽然是多选, 也是要一个一个添加的
    其是否选中用variable值决定, 0未选中, 1选中
    太难使了, 还是封装一层吧
"""
"""
    此例顺便演示一种父组件获取子组件状态的方法,
    即利用python的引用传参, 父组件直接把状态数组, command函数传给子组件
    子组件触发command的时候, 相当于直接改了父组件的状态数组
"""
from tkinter import *

class Choice:
    """
    传入父组件, 选项列表, 选中状态列表, onchange函数; 这么传可以让父组件获取子组件状态
    """
    def __init__(self, parent, values: list, checked: list, onchange):


        for i in range(len(values)):
            cb = Checkbutton(parent, text=values[i], variable=checked[i], command=onchange)
            # side控制摆放在四个方向的大致位置，然后anchor可以控制控件放置在side确定的区域内的某个位置。
            # side有四个取值, top, bottom, left, right, 有先来后到之分, 默认为top
            # 四个top相当于没指定, 体会一下, side会在剩余未占部分找top, bottom, left, right
            cb.pack(side='top', anchor='w')

class MyFrame:
    def __init__(self, parent):
        self.girl = ["西施", "王昭君","貂蝉", "杨玉环"]
        self.state = [IntVar() for x in self.girl]  # 注意这里传入的一定是这个, 子组件才能触发父组件的值变化

        framel = Frame(parent)
        framel.pack(side='left')

        choice = Choice(framel, self.girl, self.state, self.onchange)

        framer = Frame(parent)
        framer.pack(side='right')

        self.text = StringVar()
        self.text.set("请挑选妃子~")
        label = Label(framer, textvariable=self.text, justify='left', fg='red')
        label.pack()

    def onchange(self):
        state = [x.get() for x in self.state]
        girl = [self.girl[i] for i in range(len(self.girl)) if state[i] == 1]
        if girl:
            self.text.set("已选: "+'、'.join(girl))
        else:
            self.text.set("请挑选妃子~")

root = Tk()
root.geometry('500x500+400-100')  # 宽x高+/-padx+-/pady
root.resizable(False, False)
frame = MyFrame(root)
root.mainloop()