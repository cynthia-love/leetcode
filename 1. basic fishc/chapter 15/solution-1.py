# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第15章 GUI的最终选择: Tkinter
"""
"""
    helloworld
"""

import tkinter as tk

window = tk.Tk()  # 创建一个主窗口
window.title("Hello World!")  # 设置主窗口的标题

# ************************************************************
# 往主窗口里添加组件

# 注意第一个参数为父组件, 即Label绑定到什么上面, 区别于matplotlib, 直接画
label = tk.Label(window, text="Label组件可以显示文本, 图标或图片")
# 书上说pack是自动调节组件自身的尺寸, 但是好像不光是这个作用, 不加直接不显示了
label.pack()
# ************************************************************

window.mainloop()