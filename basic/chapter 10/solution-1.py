# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第10章 图形用户界面入门
    easygui需要单独安装, conda里找不着, 可以用pip install easygui命令
"""

import easygui
easygui.msgbox("HelloWorld")  # 阻塞

from easygui import msgbox
msgbox("Helloworld2")

import easygui as eg  # 推荐这种方式
eg.msgbox("Helloworld3")