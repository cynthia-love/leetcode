# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用tag进行事件绑定
"""
from tkinter import *

import webbrowser

root = Tk()
text = Text(root, width=30, height=10)
text.pack()

text.insert(INSERT, 'I love FishC.com')




root.mainloop()