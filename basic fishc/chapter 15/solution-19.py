# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    关闭时判断文件内容是否发生改变
"""

from tkinter import *
import hashlib

def getSig(contents):
    return hashlib.md5(contents.encode('utf-8')).digest()

root = Tk()
text = Text(root, width=50, height=30)
text.pack()
text.insert(INSERT, 'I love fishc.com')

contents = text.get(1.0, END)  # 注意这里索引1.0表示第一行第0列
sig1 = getSig(contents)

def click():
    contents2 = text.get(1.0, END)
    sig2 = getSig(contents2)
    if sig1 == sig2:
        print("风平浪静")
    else:
        print("变了")

Button(root, text='检查', command=click).pack()
root.mainloop()
