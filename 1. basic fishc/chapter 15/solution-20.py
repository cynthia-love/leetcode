# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    搜索
"""

from tkinter import *
root = Tk()
# ********************************************************************************************************************
text = Text(root, width=50, height=20)
text.pack()
text.insert('insert', 'Hello fishffishffccc')

start = 1.0
def find():
    global start
    # stopindex不指定则默认为END; regexp表示开启正则匹配模式
    pos = text.search(r'fishf{2}', start, stopindex='end', regexp=True)
    # 设置backwards为True表示从后往前搜索,相应的start为END, start更新为pos-1c
    if not pos:
        print("没了")
    else:
        print(pos)  # pos为l.c格式的索引，字符串格式
        start = '{}+{}c'.format(pos, 1)  # 这里如果跳过6，那就找不到1.11了, 1.6+1c
        # 不确定会不会换行, 只能用这种相对位置表达方式
        # 除了+1c, 还可以+多个c, 直接跳过这个字符串, 看需要把

button = Button(root, text="搜索fishc", command=find)
button.pack()

# ********************************************************************************************************************
root.mainloop()