# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    打包成可执行文件
    pyinstaller可以用conda install pyinstaller命令安装
    (像是easygui这种conda里没有的才需要改用pip命令: pip install easygui)

    pyinstaller命令:
    pyinstaller -XX test.py, 其中-XX有:
    -F 产生单个可执行文件
    -D 产生一个目录作为可执行文件
    -w 运行时不带命令行(仅在windows下生效)
    -c 运行时带命令行, 如果是纯命令行程序, 别忘了在文件结尾加os.system("pause"), 不然程序闪一下就没了
    -n 指定生成项目的名字(生成的打包.spec配置文件会和这个同名)
    -i 指定图标

    pyinstaller -D -c -n DemoI -i demo.ico solution-1.py
    pyinstaller -D -w -n DemoII -i demo.ico solution-1.py
    pyinstaller -D -c -n DemoIII -i demo.ico solution-1.py

    除了打一堆参数, 也可以直接根据已有的配置文件打包

"""
from easygui import msgbox
print("hahahha")
# msgbox("Hello World")
import os
os.system("pause")