# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    filedialog
"""
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry('300x300')
def f():
    filename = askopenfilename()
    print(filename)  # 打印选中文件的全路径; 用户取消则打印空字符串

Button(root, text="打开", command=f).pack()

# askopenfilenames返回是一个文件路径的列表
Button(root, text="打开2", command=lambda :print(askopenfilenames())).pack()

# askopenfile返回的是一个打开的文件对象
Button(root, text="打开3", command=lambda :print(askopenfile())).pack()

# asksaveasfilename返回的也是一个文件的全路径, 比如/Users/soso/Desktop/aaa.txt
# 无非是和打开文件对话框样式不一样
Button(root, text="保存", command=lambda :print(asksaveasfilename())).pack()

# askopenfilename和asksaveasfilename可以指定的一些参数
# defaultextension对于保存才有意义, 用户输入文件名如果不包含后缀, 自动添加
# filetypes在对话框下方加一个筛选功能, 注意, 加了filetype, 那defaultextension就没用了
# initialdir, 指定对话框打开时的初始路径

Button(root, text="打开4", command=lambda :print(asksaveasfilename(
    title='haha', defaultextension='.jpg', filetypes=[('PDF', '.pdf'), ('ZIP', '.zip')],
    initialdir='/Users/soso'
))).pack()


root.mainloop()