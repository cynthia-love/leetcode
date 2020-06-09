# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    三种布局管理器
    pack, 按添加顺序排列, 适用少量组件的情况
    grid, 按行列形式排列, 支持更复杂的组件排列, 当然, 复杂的也可以用多个Frame去拼
    place, 直接指定组件大小和位置
"""
"""
    pack
"""
from tkinter import *

root = Tk()
root.geometry('500x300')

# pack会自动填充空间，哪怕没指定fill, 下一个控件pack的地方永远是上一个空间pack完后剩余空间

# pack默认将父组件的空间分为上下左右四部分, 重叠的部分先到先得
# fill只是把组件显示去占满分配的空间, 不指定fill实际上也已经占了
# 比如这里, 实际上把左边从上到下的一个长条区域都占了; 注意, 不是左边50%, 会最小化占用
Label(root, text="red", bg='red').pack(side='left', fill='y')

# expand会占满整个父组件空间, 此时side就没啥意义了, 但expand只是占, 并未填充, 所以fill还是有意义的
t = Toplevel(); t.geometry('500x300')
Label(t, text="red", bg='red').pack(expand=True, fill='both')

# 下面这个例子可以很好演示什么叫从剩余空间中继续按上下左右分配
t = Toplevel(); t.geometry('500x300')
Label(t, text="red", bg='red').pack(side='left', fill='y')
Label(t, text="red", bg='green').pack(side='top', fill='x')
Label(t, text="red", bg='yellow').pack(side='right', fill='y')
Label(t, text="red", bg='blue').pack(side='bottom', fill='x')

# anchor即锚点, 将子组件放在所占空间的什么位置, nw表示左上
t = Toplevel(); t.geometry('500x300')
Label(t, text="red", bg='red').pack(expand=True, anchor='nw')

root.mainloop()