# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Menubutton组件
    适用于希望菜单按钮出现在其他地方的时候, 当然, 也可以用Menu的post方法实现
"""
from tkinter import *
root = Tk()
# 注意Menu顶层菜单的text是添加cascade的时候指定额, 而Menubutton是自己的
mb = Menubutton(root, text='点我', relief=RAISED)
mb.pack()

# Menubutton的时候这里的mb不能省
menu = Menu(mb, tearoff=False)  # Menubutton的下一级是顶层菜单
mb.config(menu=menu)

menu.add_checkbutton(label='打开', command=lambda :print("打开"), selectcolor='yellow')
menu.add_separator()
menu.add_command(label='保存', command=lambda : print('保存'))
menu.add_command(label='退出', command=root.quit)

root.mainloop()