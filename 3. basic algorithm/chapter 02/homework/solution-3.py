# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    GUI文本编辑器
"""
from tkinter import *
from tkinter.scrolledtext import ScrolledText
# ScrolledText相当于tkinter给封装好的Text+ScrolledBar

print(ScrolledText.__dict__.keys())  # 类的__dict__存储所有实例共享的数据成员和成员函数, 不包含父类
print(dir(ScrolledText))  # dir会寻找所有属性, 包括从父类继承的, dir返回的才是所有支持的有效属性

root = Tk()
root.title("Simple Editor")

st = ScrolledText(root)
st.pack(side=TOP, expand=True, fill=BOTH)

def fopen():
    with open("data/test.txt", "r") as f:
        st.delete('1.0', END)
        st.insert(INSERT, f.read())

def fsave():
    with open("data/test.txt", "w") as f:
        f.write(st.get('1.0', END))

Button(text='open', command=fopen).pack(side=LEFT)
Button(text='save', command=fsave).pack(side=LEFT)


root.mainloop()