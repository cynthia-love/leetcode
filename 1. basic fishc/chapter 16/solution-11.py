# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    截图小工具
    先捋清楚过程, 初始select0, 开始选择select1(直接松开重置0), 选择过程中select2, 选择结束select3
    开始拖拽select3 drag1(直接松开重置0), 拖拽过程中select3 drag2, 拖拽结束select3 drag3
    之后点击所选择区域和其他区域, 分别执行不同操作
    这里其实和后面的stage是一个思路, 无非是设置了两个参数
"""

import sys
import pygame as pg
from pygame.locals import *

# 窗口参数
title = 'Turtle'
size = width, height = 600, 400
bg = (255, 255, 255)

# 素材
img = pg.image.load('img/turtle.png')
pos = img.get_rect()

# 开始处理
pg.init()
pg.display.set_caption(title)

screen = pg.display.set_mode(size)

clock = pg.time.Clock()

select, drag, select_rect = 0, 0, pg.Rect(0, 0, 0, 0)
while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

        if e.type == MOUSEBUTTONDOWN:
            # 1. 第一次点击, 表示开始选择, select由0变成1, 记住初始位置
            # 如果此状态下又单击了鼠标, 重置初始位置
            if select == 0 or select == 1:
                select = 1
                start = pg.mouse.get_pos()

            # 4. 如果画框已经结束, 又单击, 在选择区域外面, select置为1开始选择状态
            # drag置为0, 未拖拽状态; 在选择区域里面, select不变, drag置为开始拖拽状态1
            if select == 3:
                point = pg.mouse.get_pos()
                if not select_rect.collidepoint(*point):
                    # 这里select置为了1而不是0, 因为有可能直接执行选择过程
                    # 如果不是, 重置操作放在直接松开鼠标键的逻辑里了
                    select, drag = 1, 0
                    start = pg.mouse.get_pos()
                else:
                    drag = 1
                    capture = screen.subsurface(select_rect).copy()
                    cap_rect = capture.get_rect()

        if e.type == MOUSEMOTION:
            # 2. 开始移动光标, select置为2, 不断更新鼠标移动位置, 开始画框
            if select == 1 or select == 2:
                select = 2
                end = pg.mouse.get_pos()
                select_rect.x, select_rect.y = start
                select_rect.width, select_rect.height = end[0] - start[0], end[1] - start[1]

            # 5. 开始拖拽, drag置为2, 不断更新鼠标移动位置, 画剪切的图片
            if select == 3:
                if drag == 1 or drag == 2:
                    drag = 2
                    cap_pos = pg.mouse.get_pos()
                    cap_rect.center = cap_pos

        if e.type == MOUSEBUTTONUP:
            # 特别地, 如果开始画框状态还没移动鼠标就松了, 那么置为画框初始状态
            if select == 1:
                select = 0

            # 3. 移动结束, 松开鼠标, select置为3, 鼠标结束位置不再变化
            if select == 2:
                select = 3

            if select == 3:
                # 同样特别地, 如果开始拖拽状态还没移动鼠标就松了, 那么置为拖拽初始状态
                if drag == 1:
                    drag = 0
                if drag == 2:
                    drag = 3
    screen.fill(bg)
    screen.blit(img, pos)

    # 3. 画框的过程中和画框结束, 都要把矩形渲染出来
    if select == 2 or select == 3:
        pg.draw.rect(screen, (0, 0, 0), select_rect, 1)

    if drag == 2 or drag == 3:
        screen.blit(capture, cap_rect)

    pg.display.flip()

    clock.tick(100)
