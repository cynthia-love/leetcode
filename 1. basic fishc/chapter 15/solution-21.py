# -*- coding; utf-8 -*-
# Author: Cynthia

"""
    撤销undo和恢复redo
    原理，用户每一步操作都会记到栈1里，一般默认记最近的10个
    undo则出栈1入栈2，redo出栈2入栈1
    如果undo之后有新的操作，会清空栈2，无法再redo
    强行redo会抛TclError
"""
"""
    先简单演示
"""

from tkinter import *
root = Tk()
# ********************************************************************************************************************

# 这里设置undo为True才能开启撤销
text = Text(root, width=30, height=10, undo=True)
text.pack()
text.insert('insert', 'I love FishC')

button = Button(root, text='undo', command=lambda: text.edit_undo())
button.pack()

button2 = Button(root, text='redo', command=lambda: text.edit_redo())
button2.pack()

# ********************************************************************************************************************
root.mainloop()

