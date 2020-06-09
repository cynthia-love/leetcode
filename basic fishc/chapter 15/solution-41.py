# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    标准对话框(属于顶层窗口), 类似于h5里的alert
    种类倒是不少, 感觉就两类, 一类选是否, 一类只提醒
"""
from tkinter import *
from tkinter.messagebox import *
root = Tk()

# 阻塞, default设置按下回车响应的那个按钮, 视对话框的不同可以指定不同的值
# icon设置图标, 有ERROR, INFO, QUESTION, WARNING, 不能自定义
x = askokcancel("标题", "内容", default=CANCEL, icon=ERROR)
print(x)  # 返回True和False

x = askquestion("标题", "内容", default=NO, icon=INFO)
print(x)  # 返回yes和no

x = askretrycancel("标题", "内容")
print(x)  # 返回False和True

x = askyesno("标题", "内容")
print(x)  # False和True

x = showerror("标题", "内容")
print(x)  # 就返一个ok表示用户点了ok

x = showinfo("标题", "内容")
print(x)  # 就返了一个ok表示用户点了ok

x = showwarning("标题", "提醒")
print(x)  # 就返了一个ok表示用户点了ok

root.mainloop()
