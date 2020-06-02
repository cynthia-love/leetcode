# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Marks用法, 给某些位置做个标记
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
button.pack(side='left')

button = Button(root, text="行内超", command=lambda :text.insert('lineouter', '行内超'))
button.pack(side='left')

button = Button(root, text="全部超", command=lambda :text.insert('allouter', '全部超'))
button.pack(side='left')

# 这里会把选中的整个往后推
button = Button(root, text="SEL_LEFT", command=lambda :text.insert(SEL_FIRST, '左选中'))
button.pack(side='left')

# 在选中的下一个位置插入； 说明[SEL_FIRST, SEL_LAST)
button = Button(root, text='SEL_LAST', command=lambda :text.insert(SEL_LAST, '右选中'))
button.pack(side='left')
# ********************************************************************************************************************
root.mainloop()