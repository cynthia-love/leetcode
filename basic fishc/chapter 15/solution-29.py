# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    级联菜单里的每一项不用command而是用Checkbutton和Radiobutton
"""
from tkinter import *

root = Tk()

menu = Menu()  # 貌似这里不指定root好像也没啥影响
root.config(menu=menu)  # 顶层菜单啥都没, 用config加到组件里去

m1 = Menu()
menu.add_cascade(label='文件', menu=m1)

m2 = Menu()
menu.add_cascade(label='编辑', menu=m2)

# 先处理m1的多选
v1, v2, v3 = IntVar(), IntVar(), IntVar()
v1.set(1), v2.set(0), v3.set(1)
m1.add_checkbutton(label="打开", command=lambda :print(v1.get(), v2.get(), v3.get()), variable=v1)
m1.add_checkbutton(label="保存", command=lambda :print(v1.get(), v2.get(), v3.get()), variable=v2)
m1.add_checkbutton(label="退出", command=lambda :print(v1.get(), v2.get(), v3.get()), variable=v3)
# 点完后, 菜单关闭, 但多选状态保留, 下次再点开还是上次的多选结果

# 再处理m2的单选
v4 = IntVar()
m2.add_radiobutton(label="复制", command=lambda :print(v4.get()), variable=v4, value=100)
m2.add_radiobutton(label="剪切", command=lambda :print(v4.get()), variable=v4, value=1000)
m2.add_separator()
m2.add_radiobutton(label="粘贴", command=lambda :print(v4.get()), variable=v4, value=10000)

root.mainloop()