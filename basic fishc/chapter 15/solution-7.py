# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Radiobutton单选组件, 和多选的区别在于, 选中状态是单个值而不是一个list, 每一项的onvalue不能相同(这里的变量名是value)
    多选的选中状态为[0, 1, 0, 1, 0], 单选的选中状态为 3, 即单个int
"""

from tkinter import *

