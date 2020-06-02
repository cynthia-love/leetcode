# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Marks用法, 即自定义位置标记(类似INSERT)
    左边插入值会导致Mark后移(删除左移), 右边则不会改变mark位置
    相当于Mark会在初始set时记住它'后边的那家伙'
"""

from tkinter import *
root = Tk()
# ********************************************************************************************************************

text = Text(root, width=50, height=20)
text.pack()

text.insert('end', "这里是初始文字\n这里是第二行")

text.mark_set("middle", "1.2")
text.mark_set("lineouter", "1.10")
text.mark_set("allouter", "3.10")

button = Button(root, text="中间", command=lambda :text.insert('middle', '中间'))
button.pack()

button = Button(root, text="行内超", command=lambda :text.insert('lineouter', '行内超'))
button.pack()

button = Button(root, text="全部超", command=lambda :text.insert('allouter', '全部超'))
button.pack()

# ********************************************************************************************************************
root.mainloop()