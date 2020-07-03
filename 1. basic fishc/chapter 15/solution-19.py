# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    判断文件内容是否发生改变，算md5摘要
"""

from tkinter import *
from base64 import b64encode
import hashlib

root = Tk()
# ******************************************************************************************************************

def getSig(contents):
    # 传入参数必须为byte类型； digest输出也是byte类型
    return hashlib.md5(contents.encode('utf-8')).digest()

text = Text(root, width=50, height=30)
text.pack()
text.insert(INSERT, 'I love fishc.com')

contents = text.get(1.0, END)  # 注意这里索引1.0表示第一行第0列
sig1 = getSig(contents)

def click():
    contents2 = text.get(1.0, END)
    sig2 = getSig(contents2)
    print(sig1, sig2)
    print(b64encode(sig1), b64encode(sig2))
    print(b64encode(sig1).decode('utf-8'), b64encode(sig2).decode('utf-8'))
    if sig1 == sig2:
        print("风平浪静")
    else:
        print("变了")

Button(root, text='检查', command=click).pack()

# *******************************************************************************************************************
root.mainloop()
