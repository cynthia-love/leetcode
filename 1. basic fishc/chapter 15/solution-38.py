# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    三种布局管理器
    pack, 按添加顺序排列, 适用少量组件的情况, 可以去solution-3里看更详细的解释
    grid, 按行列形式排列, 支持更复杂的组件排列, 当然, 复杂的也可以用多个Frame去拼
    place, 直接指定组件大小和位置
"""
"""
    pack
"""
from tkinter import *

root = Tk()
root.geometry('500x300')

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
Label(t, text="red", bg='red').pack(expand=True, side='left', anchor='nw')
Label(t, text="green", bg="green").pack(side='right', anchor='n')
# 这里就比较有意思了, green居然跑右下去了
# 后辈的独占空间挤占前辈的可扩展空间, 这里的挤占是沿父辈的扩展方向往回挤占
# 比如父辈side设置top时, 后辈跑右下去了, 即往上挤占, 在下方挤出来一个矩形作为容器可用空间
# 注意挤出来的是可用空间, 在可用空间基础上, 再side为right占用右侧一小块作为独占空间
# 这种情况下后辈设置anchor实际上是没啥用的, 因为其独占空间基本相当于其自身大小了
# 而父辈side设置left时, 后辈才会在右上角, 即往左挤占, 右侧矩形作为容器可用空间
# 然后side又设置的right, 此时anchor为n或s才有意义
root.mainloop()