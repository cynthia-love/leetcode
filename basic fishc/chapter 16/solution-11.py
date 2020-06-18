# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    截图小工具
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

pointA, w, h = None, None, None

while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

        if e.type == MOUSEBUTTONDOWN:
            pointA = pg.mouse.get_pos()
            print(pointA)

        if e.type == MOUSEMOTION:
            if pointA:
                mouse_pos = pg.mouse.get_pos()
                print(mouse_pos)
                w, h = mouse_pos[0]-pointA[0], mouse_pos[1]-pointA[1]

        if e.type == MOUSEBUTTONUP:
            if pointA and w and h:
                pointA = None

    screen.fill(bg)
    screen.blit(img, pos)
    if pointA and w and h: pg.draw.rect(screen, (0, 0, 0), (*pointA, w, h), 1)

    pg.display.flip()

    clock.tick(100)
