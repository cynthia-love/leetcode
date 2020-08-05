# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Text组件索引专题
"""

from tkinter import *
root = Tk()
# *******************************************************************************************************************

text = Text(root, width=50, height=20)
text.pack()  # pack不指定参数时，默认为top

# 文件尾部插入
text.insert('end', '初始字符串这里初始字符串这里初始字符串这里初始字符串这里\n这里是第二行')

# 文件尾部插入
button = Button(root, text="结尾", command=lambda :text.insert('end', "结尾"))
button.pack(side='left')

# 光标位置插入
button = Button(root, text="光标", command=lambda :text.insert('insert', "光标"))
button.pack(side='left')

# 第3行，第3列；注意自动换行的认为是一行；注意行超限会变成往文件尾(最后一行行尾)插入，列超限会变成往当前行尾插入
# 注意行索引从1开始, 列从0开始
button = Button(root, text="行列", command=lambda :text.insert('1.2', "行列"))
button.pack(side='left')

# 行尾插入，行超限变成往文件尾插入
button = Button(root, text="行尾", command=lambda :text.insert('2.end', "行尾"))
button.pack(side='left')

# button = Button(root, text="鼠标", command=lambda :text.insert('current', "鼠标"))  # 好像用处不大这个
# button.pack(side='left')
# current绑定鼠标才有意义
text.bind('<Button-1>', lambda e: text.insert('current', '鼠标'))


# 除了插入, 还能获取值; 注意insert代表的是光标后面那个位置
button = Button(root, text="获取单", command=lambda :print(text.get('insert')))
button.pack(side='left')

# 给get两个参数则表示获取区间，end表示文件尾，1.end表示第一行行尾； 这里1.5不包含在内
# 这里表示获取第一行的第3, 4, 5个字符
button = Button(root, text="获取区间", command=lambda :print(text.get('1.2', '1.5')))
button.pack(side='left')

# 相对位置，第一行的行尾往前三个字符； 这里的chars可以简写成c
# 注意, 参数虽然是前面包含后面不包含, 但end比较特殊, 指定end时能包括行尾最后一个字符
# 这里-3个最终也只是少3个字符, 而不是减了3个再不包含一个最终少4个
button = Button(root, text="相对", command=lambda :print(text.get('1.2', '1.end - 3 chars')))
button.pack(side='left')

# 相对位置，某个字符所在行的行尾, 2.2 lineend意义不大, 可能insert lineend更有意义
button = Button(root, text="行尾", command=lambda :print(text.get('1.2', 'insert lineend')))
button.pack(side='left')

# 相对位置，某个位置所在单词的词尾（无法识别中文单词，只能简单地以空格、\n等区分
button = Button(root, text="单词", command=lambda :print(text.get('1.13', '1.13 wordend')))
button.pack(side='left')

# *******************************************************************************************************************
root.mainloop()