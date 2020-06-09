# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    place
    需要更精细化控制布局的时候, 比如一个组件在另一个组件上方
"""
from tkinter import *
root = Tk()

photo = PhotoImage(file='img/tulips.gif')
Label(image=photo).pack()

# 先找到相对位置(50%, 50%), 再把子组件的中心定位在该点上, 即先找点, 再确定子组件的哪个位置对应这个点
Button(root, text='点我', command=lambda :print(photo)).place(relx=0.5, rely=0.5, anchor='center')

# 除了relx, rely, 还有relwidth, relheight
top = Toplevel()
top.geometry('300x300')

# 这里拉伸top, 里面的组件长宽会跟着变
Label(top, bg='red').place(relx=0.5, rely=0.5, anchor='center', relwidth=0.75, relheight=0.75)
Label(top, bg='green').place(relx=0.5, rely=0.5, anchor='center', relwidth=0.6, relheight=0.6)

Label(top, bg='yellow').place(relx=0.5, rely=0.5, anchor='center', relwidth=0.45, relheight=0.45)
Label(top, bg='blue').place(relx=0.5, rely=0.5, anchor='center', relwidth=0.3, relheight=0.3)


root.mainloop()