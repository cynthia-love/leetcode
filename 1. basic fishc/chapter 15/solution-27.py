# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Menu组件
"""

from tkinter import *
root = Tk()

m = Menu(root)
root.config(menu=m)  # 注意顶层菜单的布局不能用pack/place什么的, 而是通过config作为root的属性


m1 = Menu(m, tearoff=False)  # tearoff=True表示菜单可以独立出来, 不过在mac里好像没啥用
m.add_cascade(label='文件', menu=m1)  # 里面的菜单用顶层菜单的add_cascade
"""
有点绕, 顶层菜单添加root.config(menu=m), 后面菜单m.add_cascade(label='xx', menu=m1)
叶节点功能按钮添加x.add_command(label='xx', command=xxx)
"""

m1.add_command(label='打开', command=lambda: print("打开"))
m1.add_command(label='保存', command=lambda: print("保存"))

m2 = Menu(m, tearoff=False)
m.add_cascade(label='编辑', menu=m2)

m2.add_command(label='复制', command=lambda : print('复制'))
m2.add_separator()  # 添加分割线
m2.add_command(label='粘贴', command=lambda : print('粘贴'))


m3 = Menu(m2, tearoff=False)
m2.add_cascade(label='更多', menu=m3)
# 单级选项add_command, 多级选项add_cascade

m3.add_command(label='删除', command=lambda : print('删除'))
m3.add_command(label='重置', command=lambda : print('重置'))

root.mainloop()