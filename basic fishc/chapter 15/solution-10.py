# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用Entry组件实现一个小计算器
"""

import re
from tkinter import *

class Calculator:
    def __init__(self, parent):

        self.state = {
            'num1': StringVar(),
            'num2': StringVar(),
            'sum': StringVar()
        }

        testCMD = parent.register(self.test)
        Entry(parent, width=10, textvariable=self.state['num1'], validate='key', validatecommand=(testCMD, '%P')).grid(
            row=0, column=0
        )
        Label(parent, text='+').grid(row=0, column=1)
        Entry(parent, width=10, textvariable=self.state['num2'], validate='key', validatecommand=(testCMD, '%P')).grid(
            row=0, column=2
        )
        Label(parent, text='=').grid(row=0, column=3)
        Entry(parent, width=10, textvariable=self.state['sum'], state='disabled').grid(row=0, column=4)
        Button(parent, text="计算", height=1, command=self.cal).grid(row=0, column=5, padx=2, pady=5)


    def test(self, content):
        if re.match(r'^\d*$', content):
            return True
        else:
            return False

    def cal(self):
        num1, num2 = self.state['num1'].get(), self.state['num2'].get()
        if num1 and num2:
            self.state['sum'].set(str(int(num1)+int(num2)))


root = Tk()
frame = Frame(root)
frame.pack(padx=10, pady=10)
calculator = Calculator(frame)
root.mainloop()