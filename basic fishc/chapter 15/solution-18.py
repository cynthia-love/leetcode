# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    再演示事件绑定
"""
from tkinter import *
import webbrowser
root = Tk()
# *******************************************************************************************************************

text = Text(root, width=30, height=10)
text.pack()

text.insert(INSERT, 'I love FishC.com')
# 先加下划线样式
text.tag_add("link", '1.7', '1.16')
text.tag_config('link', foreground='blue', underline=True)

# 再给tag对应的内容对象绑定鼠标悬浮事件; 注意<xxx>这种事件函数一般都有个参数event
text.tag_bind('link', '<Enter>', lambda e: text.config(cursor='arrow'))
text.tag_bind('link', '<Leave>', lambda e: print(e))
# 绑定鼠标左键点击事件, 使用默认浏览器打开指定网址
text.tag_bind('link', '<Button-1>', lambda e: webbrowser.open("http://www.fishc.com"))
text.tag_bind('link', '<Double-Button-3>', lambda e: print(e))  # 鼠标右键双击

# *******************************************************************************************************************
root.mainloop()