# -*- coding; utf-8 -*-
# Author: Cynthia

"""
    撤销undo和恢复redo
"""

from tkinter import *

root = Tk()

# 这里设置undo为True才能开启撤销
text = Text(root, width=30, height=10, undo=True)
text.pack()

text.insert('insert', 'I love FishC')

button = Button(root, text='undo', command=lambda: text.edit_undo())
button.pack()

button2 = Button(root, text='redo', command=lambda: text.edit_redo())
button2.pack()

root.mainloop()

