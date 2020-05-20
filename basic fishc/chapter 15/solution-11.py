# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Listbox组件
"""

from tkinter import *

root = Tk()

# setgrid启用网格控制
# lb = Listbox(root, setgrid=True)
# lb.pack()

items = ['鸡蛋', '鸭蛋', '鹅蛋', '李狗蛋', '蛋蛋1', '蛋蛋2']
# for item in items:
#     lb.insert('end', item)
# 可以一个一个添加, 也可以用listvariable指定
# listvariable只支持"鸡蛋 鸭蛋 鹅蛋 李狗蛋"这种形式, 太2了, 不用也罢, 一个个添加吧
listvar = StringVar()
listvar.set(" ".join(items))

frame = Frame()
frame.pack(side=TOP)
# selectmode开启多选模式
lb = Listbox(frame, setgrid=True, listvariable=listvar, height=5, selectmode=EXTENDED)
lb.pack(side=LEFT, fill=BOTH)

# 有时候可选项太多, 需要添加滚动条, 即Scrollbar
# 安装滚动条需要做两件事, 设置滚动条的command为组件的yview方法
# 设置组件的yscrollbarcommand为Scrollbar的set方法
sb = Scrollbar(frame, command=lb.yview)
sb.pack(side=RIGHT, fill=Y)  # fill=Y表示窗体发生改变时随窗体在Y方向上变化

# 在组件初始化后再改配置用config函数
lb.config(yscrollcommand=sb.set)


# delete有俩参数, (0, END)表示删除全部; 只给一个参数则是删除特定位置的, ACTIVE特指选中的
bt = Button(root, text='删除', command=lambda :lb.delete(ACTIVE))
bt.pack(side=LEFT)

# 注意多选的时候, ACTIVE指向最后一个, 而curselection()返回所有选中项的索引
bt2 = Button(root, text='确定', command=lambda x=lb:print(x.get(ACTIVE), x.curselection()))
bt2.pack(side=RIGHT)

root.mainloop()

