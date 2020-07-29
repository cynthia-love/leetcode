# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现一个功能比较完备的秒表
    秒表更新思路: tkinter窗口，比如root窗口，以及Toplevel窗口，都有一个after方法。此方法执行后，
    将会在规定的时间间隔之后，执行一个特定的您指定的函数。如果在您指定的这个定时执行的函数中，再次
    调用after方法，就可以起到一个定时器的效果。
    为了用该方法, 这里自定义类需要继承Frame

    梳理功能点:
    1. 初始进去, 秒表显示00:00:00, 分别代表分钟, 秒, 百分秒
    下方两个按钮, 计次和启动, 初始计次不能点, 再下方展示所有计次的时间, 初始为空
    2. 点了启动, 计次按钮可点, 启动按钮变成停止, 此时点计次, 下方打印所有计次时间点
    3. 点暂停, 此时计次按钮变复位, 暂停按钮变启动, 点复位回到初始状态, 点启动, 继续计时
    那么用stage的思路, 可以有这么几种枚举值:
    INIT, RUN, PAUSE
"""
from tkinter import *
from tkinter import ttk  # 为什么上面的*引入不进来
from datetime import datetime

INIT, RUN, PAUSE = 1, 2, 3

class StopWatch(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)
        self.delay = 50  # after函数多久以后执行, 单位ms
        self.stage = INIT

        self.base = None  # 基准时间
        self.time = None  # 已持续时间, 单位秒, 带小数

        # 设置三个变量, 文本, 左右按钮名
        self.text = StringVar()
        self.text_button1 = StringVar()
        self.text_button2 = StringVar()

        self.timer = None  # after定时器

        self.init()  # 初始化变量值
        # 注意有一点, pygame重新开始可以直接main(), tkinter不行, 还是得手动去重置变量值

        # 画页面
        # 注意, tkinter只能设置窗体整体的透明度, 不支持设置组件bg属性透明, 但好像会继承窗体的透明度
        self.label = Label(parent, textvariable=self.text, fg="black", font=("黑体", 66))
        self.label.place(relx=0.5, rely=0.25, anchor=CENTER)

        # 苹果电脑下button的bg属性好像没有效果....这是逼我用canvas吗, 先不管样式, 先做实现功能
        self.button1 = Button(parent, textvariable=self.text_button1, fg='grey', bg='black',
               font=("黑体", 30), relief=RAISED, command=self.f1)
        self.button1.place(relx=0.14, rely=0.5, anchor=SW)

        self.button2 = Button(parent, textvariable=self.text_button2, fg='green', bg='black',
               font=("黑体", 30), relief=RAISED, command=self.f2)
        self.button2.place(relx=0.86, rely=0.5, anchor=SE)

        # Listbox和Scrollbar要包起来, 不然滚动条会超出Listbox范围
        frame = Frame(parent)
        frame.place(relx=0, rely=0.55, anchor=NW, relwidth=1.0, relheight=0.45)
        self.list = Listbox(frame, bd=0, font=("黑体", 18))  # 后面有expand和fill, 就别设置宽高了
        # expand是否自动扩展, fill扩展方向, 俩参数关系没明白, 比如sb就不能指定expand
        self.list.pack(side=LEFT, expand=YES, fill=BOTH)  # fill好像是拖动的时候才有用吧
        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=Y)

        self.list.config(yscrollcommand=sb.set)
        sb.config(command=self.list.yview)

    def init(self):
        self.time = 0

        self.text.set("00:00:00")
        self.text_button1.set("计次")
        self.text_button2.set("启动")

    def f1(self):
        self.list.insert(0, "{:<6}计次{:<17}{}".format("", self.list.size()+1, self.text.get()))

    def f2(self):
        self.list.delete(0, END)


    def t2s(self, t):
        # t存的是带小数的秒
        # 灵活利用多级嵌套format
        return "{}:{}:{}".format(
            "{:0>2d}".format(int(t // 60)),
            "{:0>2d}".format(int(t % 60)),
            "{:0>2d}".format(int(t % 1 * 100 // 1))
        )


    def start(self):
        self.base = datetime.now()
        self.update()
        self.stage = RUN

    def update(self):
        now = datetime.now()
        self.time += (now-self.base).total_seconds()
        self.base = now

        self.text.set(self.t2s(self.time))
        self.timer = self.after(self.delay, self.update)


def main():
    root = Tk()
    root.title("Stop Watch")
    root.geometry("370x600+600+150")  # 后面的padx和pady是相对于屏幕的位置
    # root.iconbitmap("img/watch.ico") # mac下设置没用
    # root['background'] = 'black'
    root.attributes("-alpha", 0.95)  # 设置整个窗体的透明度
    # root.attributes("-fullscreen", True)  # 全屏
    # root.attributes("-topmost", True)  # 所有窗口中处于最顶层, 失焦也还是在最顶层
    # root.overrideredirect(True) # 取消标题栏, 但mac下设置了好像也不正常
    root.resizable(width=False, height=False)  # 不让调整大小

    # quit终止所有tkinter应用程序, 范围不可控, 用destroy只终止本程序
    # 这里退出好像不能直接写root.destroy, 只能写成这种形式
    root.bind("<Escape>", lambda x:root.destroy())

    sw = StopWatch(root)
    sw.start()
    root.mainloop()

if __name__ == "__main__":
    main()



