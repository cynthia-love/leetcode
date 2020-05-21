# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Text组件索引专题
"""

from tkinter import *

root = Tk()

text = Text(root, width=50, height=20)
text.pack()
text.insert('end', '初始字符串这里是哈哈哈 like you')

button = Button(root, text="结尾", command=lambda :text.insert('end', "结尾"))
button.pack(side='left')

button = Button(root, text="光标", command=lambda :text.insert('insert', "光标"))
button.pack(side='left')

# 行从1开始索引, 列从0开始索引, 这里表示插到第一行第3个位置; 索引超限插到最后
button = Button(root, text="行列", command=lambda :text.insert('1.2', "行列"))
button.pack(side='left')

# 同样, 索引超限, 插到最后
button = Button(root, text="行尾", command=lambda :text.insert('2.end', "行尾"))
button.pack(side='left')

button = Button(root, text="鼠标", command=lambda :text.insert('current', "鼠标"))  # 好像用处不大这个
button.pack(side='left')


# 除了插入, 还能获取值; 注意insert代表的是光标后面那个位置
button = Button(root, text="获取单", command=lambda :print(text.get('insert')))  # 好像用处不大这个
button.pack(side='left')

button = Button(root, text="获取多", command=lambda :print(text.get('1.2', 'end')))  # 好像用处不大这个
button.pack(side='left')

# 相对位置
button = Button(root, text="相对", command=lambda :print(text.get('1.2', 'end - 3 chars')))  # 好像用处不大这个
button.pack(side='left')

button = Button(root, text="行尾", command=lambda :print(text.get('1.2', '1.2 lineend')))  # 好像用处不大这个
button.pack(side='left')

button = Button(root, text="单词", command=lambda :print(text.get('1.13', '1.13 wordend')))  # 好像用处不大这个
button.pack(side='left')

root.mainloop()