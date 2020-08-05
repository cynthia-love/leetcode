# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Scale组件, 用于选数字
"""

from tkinter import *

root = Tk()

# 注意from后面的下划线,
Scale(root, from_=0, to=42, length=500, resolution=0.5, orient=HORIZONTAL).pack()
# resolution控制步长(每移动一下加多少), 当from_, to不是步长整数倍时, 往整数倍扩展
# tickinterval刻度, 同样也得是步长的整数倍
# 一般情况下, 步长都是1...不然怎么选中间的值, 当然, 步长也可以是小数
value = IntVar()
# 同样, Scale组件可通过variable把值与变量绑定
# 这里参数x好像就是值
Scale(root, from_=0, to=41, length=500, resolution=3, tickinterval=3, variable=value, orient=VERTICAL,
      command=lambda x: print(x, value.get())).pack()

mainloop()

