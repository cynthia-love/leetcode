# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    事件绑定
"""
from tkinter import *
root = Tk()
root.geometry('300x800')

frame = Frame(root, height=100, width=300, bg='red')
frame.pack()
# 绑定鼠标左键双击事件, Button-2中键, Button-3右键; x_root, y_root是相对于整个屏幕
frame.bind('<Double-Button-1>', lambda e: print(e, e.x, e.y, e.x_root, e.y_root))

frame = Frame(root, height=100, width=300, bg='green')
frame.pack()
# 绑定键盘事件
frame.bind('<Key>', lambda e: print(e))
frame.focus_set()  # 得先获得焦点才能接收键盘事件; 或者设置takefocus为True, 然后用Tab移动焦点
# <KeyPress event keysym=d keycode=100 char='d' x=-5 y=-150>

frame = Frame(root, height=100, width=300, bg='yellow')
frame.pack()
# 捕获鼠标运动轨迹
frame.bind('<Motion>', lambda e: print(e.x, e.y))

frame = Frame(root, height=100, width=300, bg='blue')
frame.pack()
frame.bind('<Lock-Motion>', lambda e: print(e))
# 这里这么写, 只有Lock是按下的状态才会去捕捉鼠标运动轨迹

"""
tkinter里的事件格式为'<modifier-type-detail>'
比如: <Button-1>, modifier为空, type为Button即鼠标按键, 1表示鼠标按键的第一个, 即左键
<KeyPress-H>, 表示用户按下H键(KeyPress可简写为Key)
<Control-Shift-KeyPress-H>, 同时按下Ctrl+Shift+H键
其中modifier主要有:
Control, Shift, Alt
Any, 比如Any-Key
Lock, 当打开CapsLock的时候
Double, Triple, 配合后面的使用, 比如<Double-Button-1>, 鼠标左键双击

"""

frame = Frame(root, height=100, width=300, bg='red')
frame.pack()
frame.bind('<Activate>', lambda e: print(e))  # 组件激活时, 比如从后台切到前台; 对应Deactivate

frame = Frame(root, height=100, width=300, bg='green')
frame.pack()
frame.bind('<ButtonRelease>', lambda e: print(e))  # 松开鼠标左键触发

frame = Frame(root, height=100, width=300, bg='yellow')
frame.pack()
frame.bind('<Enter>', lambda e: print(e))  # 进入组件触发

frame = Frame(root, height=100, width=300, bg='blue')
frame.pack()
frame.bind('<Visibility>', lambda e: print(e))  # <Visibility event state=VisibilityUnobscured>

"""
    其他事件还有Destroy, Expose
    FocusIn, 获得焦点时触发, 需要设置组件takefocus为True
    FocusOut, 失去焦点时触发
    KeyPress/Key, 按下键盘时触发
    KeyRelease, 松开键盘时触发
    Leave, 离开组件时触发
    Motion, 鼠标移动
    Visibility, 当应用程序至少有一部分在屏幕中是可见的时候
"""

root.mainloop()