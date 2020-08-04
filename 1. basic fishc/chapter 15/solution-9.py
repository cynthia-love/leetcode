# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Entry组件的validate
    validate的取值有:
    focus, 获得或失去焦点时触发
    focusin, focusout
    key, 输入框被编辑时触发
    all, focus+key
    none, 注意是字符串的'none', 关闭校验
    其实就是onchange啥的, 只不过把onchange拆成了两个字段, 一个为什么时候触发, 一个为触发后做什么


"""

import re
from tkinter import *


class MEntry:

    def __init__(self, parent):

        self.state = {
            "text1": StringVar(),
            "text2": StringVar()
        }

        # 要采用%P的形式传参这里得先注册一下, 直接用self.test是不行的
        testCMD =  parent.register(self.test)
        test2CMD = parent.register(self.test2)
        # invalidcommand只有在validatecommand返回False的时候才会调用
        # invalidcommand同样支持%P的形式传最新值
        self.e1 = Entry(parent, textvariable=self.state['text1'], validate='key',
                        validatecommand=(testCMD,'%P', '%s'),  invalidcommand=(test2CMD, '%P'))
        self.e1.grid(row=0)

        self.e2 = Entry(parent, textvariable=self.state['text2'])
        self.e2.grid(row=1)

    def test(self, content, content_old):
        print(content, content_old, self.state['text1'].get())
        # %P表示新值, %s表示老值, %s等价于self.state['text1'].get()
        # 注意validate为key时, validatecommand在前, textvariable改变在后, 所以没办法用textvariable获取最新值
        if re.search(r'^\d*$', content):
            return True  # 不要直接在这里改self.state, 而是return True后系统自己改
        else:
            return False

    def test2(self, content):
        print("输入不合法, 输入域保持原值", content)

root = Tk()
mentry = MEntry(root)
root.mainloop()