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
        # expand影响的是领土, fill影响的是当前占用
        # 不开启expand时, 领土是上面一行, 此时fill y是没意义的, fill x则占据整行
        # 开启expand, 领土全占, 此时fill both会全占了
        # frame属于容器, 一般都是要扩展到最大范围, 要有fill, 只expand没意义, 子组件获取不到其未占用的领土
        frame.pack(side=side, expand='yes', fill='both')

        # 大概知道setgrid是干嘛的了, 这里如果设置了True, 那root里的300x300会变成300行x300列
        # 如果设置False, 300x300则是300像素x300像素; 尽量不要开启吧, 太乱
        self.lb = Listbox(frame, setgrid=False, height=height, selectmode=EXTENDED)
        for item in self.values:
            self.lb.insert(END, item[1])
        self.lb.pack(side=LEFT, expand='yes', fill='x')
        # 在frame占据全部window的前提下, 这里listbox的side设置的left, 为了与scrollbar接壤
        # 其要向右扩展, 需要先拓展领土, 再用fill占用, expand只有一个取值, 只能设置yes
        # 但fill可以控制其实际占用的领土, fill设置x, 则只横向扩展
        # fill设置both, 则占满全部frame所占据的领土, 此时listbox的height设置就没意义了

        sb = Scrollbar(frame, command=self.lb.yview)
        sb.pack(side=RIGHT, anchor='w')
        # scrollbar放在右边, 其独占空间会压缩一部分listbox的扩展空间
        # 注意这里anchor设置w和center和e, 效果是等价的, 因为水平范围上, scrollbar并没有移动空间

        self.lb.config(yscrollcommand=sb.set)


    def getChoices(self):
        # 将选中的索引转化成[(id:value)]的形式返回
        return [self.values[i] for i in self.lb.curselection()]


root = Tk()
root.geometry("300x300+100+100")
mlb = MListbox(root, ['鸡蛋', '鸭蛋', '鹅蛋', '李狗蛋', '蛋蛋1', '蛋蛋2'], TOP, 5)

bt = Button(root, text="点我看选中了啥", command=lambda x=mlb: print(x.getChoices()))
bt.pack(side=BOTTOM)
root.mainloop()