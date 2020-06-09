# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Hello World
"""

import pygame as pg
from pygame.locals import *
from sys import exit

# 初始化pygame
pg.init()

# 创建一个窗口
# flags传入0表示使用软件驱动窗口; depth表示颜色深度, 最好不要指定
s = pg.display.set_mode((640, 480), flags=0, depth=32)

# 设置窗口标题
pg.display.set_caption("Hello World")

bg = pg.image.load("img/tulips.gif")
mc = pg.image.load("img/cute.gif")

# 游戏主循环
while True:
    for e in pg.event.get():
        if e.type == QUIT:
            exit()
    # 将背景图画上去
    s.blit(bg, (0, 0))

    # 获得鼠标位置
    x, y = pg.mouse.get_pos()
    x -= mc.get_width()/2
    y -= mc.get_height()/2

    # 将光标画上去
    s.blit(mc, (x, y))

    # 刷新画面
    pg.display.update()