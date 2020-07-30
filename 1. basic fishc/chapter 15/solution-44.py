# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现一个功能比较完备的秒表
    秒表更新思路: tkinter窗口，比如root窗口，以及Toplevel窗口，都有一个after方法。此方法执行后，
    将会在规定的时间间隔之后，执行一个特定的您指定的函数。如果在您指定的这个定时执行的函数中，再次
    调用after方法，就可以起到一个定时器的效果。
    为了用该方法, 这里自定义类需要继承Frame

    梳理功能点:
    1. 初始进去, 秒表显示00:00.00, 分别代表分钟, 秒, 百分秒
    下方两个按钮, 计次和启动, 初始计次不能点, 再下方展示所有计次的时间, 初始为空
    2. 点了启动, 计次按钮可点, 启动按钮变成停止, 此时点计次, 下方插入时间点
    3. 点暂停, 此时计次按钮变复位, 暂停按钮变启动, 点复位回到初始状态, 点启动, 继续计时
    那么用stage的思路, 可以有这么几种枚举值:
    INIT, RUN, PAUSE
"""
from tkinter import *
from tkinter import ttk, StringVar  # 为什么上面的*引入不进来
from datetime import datetime
from typing import Dict, Union

INIT, RUN, PAUSE = 1, 2, 3

class StopWatch(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)
        self.delay = 50  # after函数多久以后执行, 单位ms

        self.stage = INIT  # stage的思路真的好啊, 写tkinter和pygame都可以用
        # 各种变量, 可以都放到state里便于管理, 不过这里不多, 其实没必要
        self.state = {
            # INIT阶段要用到的
            "text": StringVar(),
            # RUN阶段新用到的, 这俩只有阶段转换的时候才能设置值, 所以没法在init里设置
            "time": None,
            "base": None,
            "timer": None
        }

        # 画页面
        # 注意, tkinter只能设置窗体整体的透明度, 不支持设置组件bg属性透明, 但会继承窗体的透明度
        # 变化比较频繁的采取设置textvariable, 不然直接config设置text就够了, fg字体颜色, bg背景颜色
        self.label = Label(parent, textvariable=self.state['text'], fg="white", bg="black", font=("黑体", 60))
        self.label.place(relx=0.5, rely=0.25, anchor=CENTER)
        # place布局除了可以指定relx, rely, 还可以指定relheight, relwidth以及对应的x, y, height, width

        # 苹果电脑下button的bg属性好像没有效果....relief属性也没有效果...
        # activebackground点击时按钮的背景颜色
        self.button1 = Button(parent, fg='white', bg='black', activebackground='black', bd=0, font=("黑体", 28), relief=FLAT, command=self.f1, width=5)
        self.button1.place(relx=0.078, rely=0.5, anchor=SW)

        # button2的fg老变, 就不在这里设置了
        self.button2 = Button(parent,  bg='black', activebackground='black', bd=0, font=("黑体", 28), relief=FLAT, command=self.f2, width=5)
        self.button2.place(relx=0.912, rely=0.5, anchor=SE)

        # Listbox和Scrollbar要包起来, 不然滚动条会超出Listbox范围
        frame = Frame(parent)
        frame.place(relx=0, rely=0.55, anchor=NW, relwidth=1.0, relheight=0.45)

        # bd是边框宽度, highlightthickness是高亮边框的宽度, selectbackground是选中某一项的背景色
        self.list = Listbox(frame, bd=0, fg='white', bg='black', selectbackground='black', highlightthickness=0, font=("黑体", 16))  # 后面有expand和fill, 就别设置宽高了
        # expand是否自动扩展, fill扩展方向, 俩参数关系没明白, 比如sb就不能同时指定expand
        self.list.pack(side=LEFT, expand=YES, fill=BOTH)

        """ 滚动条设置样式好像无效, 为了显示效果, 暂时不用了
        sb = Scrollbar(frame, bg='black', bd=0, relief=FLAT)
        sb.pack(side=RIGHT, fill=Y)

        self.list.config(yscrollcommand=sb.set)
        sb.config(command=self.list.yview)
        """

        # 初始化INIT阶段变量值
        self.state["text"].set("00:00.00")
        # 左右按钮就四个量变, 干脆每次阶段转换都全量赋这几个值, 逻辑更清晰, 对折UI就很好写
        self.button1.config(text="计次", state=DISABLED)
        self.button2.config(text="启动", fg='lime')

    def f1(self):
        if self.stage == INIT:
            # INIT阶段左键不可点
            pass
        elif self.stage == RUN:
            # RUN阶段左键是计次, 点了计次; 这里又用到了嵌套format, 外层控制宽度, 内层控制展示值
            self.list.insert(0, "{:<4}计次 {:<15}{}".format("", "{:0>2}".format(self.list.size()+1), self.state['text'].get()))
        elif self.stage == PAUSE:
            # PAUSE阶段左键是复位, 点了回到INIT状态
            self.stage = INIT
            self.state["text"].set("00:00.00")
            self.button1.config(text="计次", state=DISABLED)
            self.button2.config(text="启动", fg='lime')

            # PAUSE复位比最开始INIT多了个清空列表
            self.list.delete(0, END)

    def f2(self):
        if self.stage == INIT:
            # INIT阶段右键是绿色的启动, 点了进到RUN阶段
            self.stage = RUN
            # INIT状态点击右键, 启动, 先修改INIT阶段的老变量
            self.button1.config(text="计次", state=NORMAL)
            self.button2.config(text="暂停", fg='red')
            # 再初始化RUN阶段的变量, INIT-RUN, 要重置time为0以及赋base初值
            self.state['time'] = 0
            self.state['base'] = datetime.now()
            self.update()

        elif self.stage == RUN:
            # RUN阶段右键是红色暂停, 点了进到PAUSE阶段, 此时取消执行update
            self.stage = PAUSE
            # RUN阶段点击右键, 暂停, 先改按钮
            self.button1.config(text="复位", state=NORMAL)
            self.button2.config(text="继续", fg='lime')
            # 再取消after, base暂时不改, 继续的时候才更新base
            self.after_cancel(self.state['timer'])

        elif self.stage == PAUSE:
            # PAUSE阶段右键是绿色继续, 点了进到RUN阶段, 已计time不动, 重置base, 重新调update
            self.stage = RUN
            self.button1.config(text="计次", state=NORMAL)
            self.button2.config(text="暂停", fg='red')
            self.state['base'] = datetime.now()
            self.update()

    def update(self):
        now = datetime.now()
        self.state['time'] += (now-self.state['base']).total_seconds()
        self.state['text'].set(self.t2s(self.state['time']))
        self.state['base'] = now

        self.state['timer'] = self.after(self.delay, self.update)

    def t2s(self, t):
        # t存的是带小数的秒
        # 灵活利用多级嵌套format
        return "{}:{}.{}".format(
            "{:0>2d}".format(int(t // 60)),
            "{:0>2d}".format(int(t % 60)),
            "{:0>2d}".format(int(t % 1 * 100 // 1))  # t%1是取小数, 再 * 100 // 1是取前两位小数
        )

def main():
    root = Tk()
    root.title("Stop Watch")
    root.geometry("494x800+600+150")  # 后面的padx和pady是相对于屏幕的位置
    root.iconbitmap("img/watch.ico") # mac下设置没用
    root['background'] = 'black'
    root.attributes("-alpha", 0.66)  # 设置整个窗体的透明度
    # root.attributes("-fullscreen", True)  # 全屏
    # root.attributes("-topmost", True)  # 所有窗口中处于最顶层, 失焦也还是在最顶层
    root.overrideredirect(True) # 取消标题栏, 但mac下设置了好像也不正常
    # root.resizable(width=False, height=False)  # 不让调整大小

    # quit终止所有tkinter应用程序, 范围不可控, 用destroy只终止本程序
    # 这里退出好像不能直接写root.destroy, 只能写成这种形式
    root.bind("<Escape>", lambda x:root.destroy())

    StopWatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()



