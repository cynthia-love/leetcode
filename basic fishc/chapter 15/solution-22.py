# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    自定义undo和redo的粒度
"""

from tkinter import *

root = Tk()

# autoseparators=False关闭默认粒度, maxundo设置最大撤销次数
text = Text(root, width=50, height=30, undo=True, autoseparators=False, maxundo=10)
text.pack()
text.insert('insert', 'I love fishC')
# 绑定事件, 每按一下键盘, 就加一个记忆点,这样撤销的时候撤回到上一个记忆点
text.bind('<Key>', lambda e: text.edit_separator())

button = Button(root, text='undo', command=lambda: text.edit_undo())
button.pack()

button = Button(root, text='redo', command=lambda: text.edit_redo())
button.pack()

root.mainloop()