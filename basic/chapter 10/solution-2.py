# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    一个简单的例子
"""
import sys
import easygui as eg

eg.msgbox(msg="hi, 欢迎进入第一个界面小游戏, 点击确定开始", title="小甲鱼")

while True:
    choice = eg.choicebox(msg="请选择你最喜欢的水果", title="小游戏", choices=["橘子", "橙子", "苹果"], preselect=2)
    # choicebox还支持回调函数, 但同步的调用没必要用回调, 等待返回值就行了
    # 这里会直接返回选项值比如橘子, 而不是索引0
    eg.msgbox(msg="你的选择是: "+str(choice), title="小游戏")
    choice = eg.ccbox(msg="是否要继续游戏?", title="小游戏")
    # ccbox返回的是True和False
    if choice:
        continue
    else:
        sys.exit(0)

