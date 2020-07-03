# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Message组件
    注意, Text是编辑多行文本, 只是展示的话用Message, Message才是Label的变体
    Message会自动换行, 并调整文本的尺寸使其适应给定的尺寸
"""
from tkinter import *

root = Tk()
root.geometry("500x500")

m = Message(root, text="hello", width=100)
m.pack()

m = Message(root, text="这是到付款的开发的空间疯狂夺金发卡机快递费忌口的今飞凯达今飞凯达", width=100)
m.pack()

root.mainloop()
