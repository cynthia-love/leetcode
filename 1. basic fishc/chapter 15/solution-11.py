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
# listvariable只支持"鸡蛋 鸭蛋 鹅蛋 李狗蛋"这种形式, 太2了, 不用也罢, 一个个insert吧
listvar = StringVar()
listvar.set(" ".join(items))

frame = Frame()
frame.pack(side=TOP)
# selectmode, 四种, single单选, browse也是单选, 但通过鼠标或者方向键可以直接改变选项
# multiple多选, extended也是多选, 但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现
# setgrid是什么意思网上没搜到详细解释
lb = Listbox(frame, setgrid=True, listvariable=listvar, height=5, selectmode=EXTENDED)
lb.pack(side=LEFT, fill=BOTH)

# 有时候可选项太多, 需要添加滚动条, 即Scrollbar
# 安装滚动条需要做两件事, 设置滚动条的command为组件的yview方法
# 设置组件的yscrollbarcommand为Scrollbar的set方法
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=Y)  # side为RIGHT时fill Y是没有意义的这里

# 在组件初始化后再改配置用config函数
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview())

# delete有俩参数, (0, END)表示删除全部; 只给一个参数则是删除特定位置的, ACTIVE特指选中的
bt = Button(root, text='删除', command=lambda :lb.delete(ACTIVE))
bt.pack(side=LEFT)

# 注意多选的时候, ACTIVE指向最后一个, 而curselection()返回所有选中项的索引, 注意是索引
bt2 = Button(root, text='确定', command=lambda x=lb:print(x.get(ACTIVE), x.curselection()))
bt2.pack(side=RIGHT)

root.mainloop()

