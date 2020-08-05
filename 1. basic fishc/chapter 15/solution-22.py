# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    自定义undo和redo的粒度
"""

from tkinter import *
root = Tk()
# *******************************************************************************************************************

# autoseparators=False关闭默认粒度, maxundo设置最大撤销次数
text = Text(root, width=50, height=30, undo=True, autoseparators=False, maxundo=10)
text.pack()

text.insert('insert', 'I love fishC')

# 绑定事件, 每按一下键盘, 就把操作入栈
# 而默认情况下可能是连续按下多个键才作为一个整体一次操作入栈
# 注意初始insert的I love fishC还是作为一次操作入栈的
text.bind('<Key>', lambda e: text.edit_separator())

button = Button(root, text='undo', command=lambda: text.edit_undo())
button.pack()

button = Button(root, text='redo', command=lambda: text.edit_redo())
button.pack()

# ********************************************************************************************************************
root.mainloop()