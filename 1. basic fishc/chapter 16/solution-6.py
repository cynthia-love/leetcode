# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    更多的设置
"""

import sys
import pygame as pg
from pygame.locals import *  # 导入常量

pg.init()

pg.display.set_caption("小乌龟")

size = width, height = 600, 400
size_f = width_f, height_f = pg.display.list_modes()[0]

fullscreen = False

screen = pg.display.set_mode(size, flags=RESIZABLE)
"""
flags的选项有:
FULLSCREEN  全屏模式
DOUBLEBUF   双缓冲模式
HWSURFACE   硬件加速支持(仅全屏时可用)
RESIZABLE   窗口可以调整大小
NOFRAME     窗口去掉边框和控制按钮
"""

bg = (255, 255, 255)

speed, step = [0, 0], 5

turtle = pg.image.load('img/turtle.png')
pos = turtle.get_rect()

turtle_l, turtle_r = turtle, pg.transform.flip(turtle, True, False)

clock = pg.time.Clock()

while True:

    for e in pg.event.get():

        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:
            if e.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pg.display.set_mode(size_f, FULLSCREEN | HWSURFACE)
                else:
                    screen = pg.display.set_mode(size)
                pos = pos.move((-pos.left, -pos.top))
            elif e.key == K_LEFT:
                speed = [-step, 0]
                turtle = turtle_l
            elif e.key == K_RIGHT:
                speed = [step, 0]
                turtle = turtle_r
            elif e.key == K_UP:
                speed = [0, -step]
            elif e.key == K_DOWN:
                speed = [0, step]
    pos = pos.move(speed)

    w, h = (width, height) if not fullscreen else (width_f, height_f)

    if pos.left < 0 or pos.right > w:
        speed[0] = -speed[0]
        turtle = turtle_l if turtle == turtle_r else turtle_r

    if pos.top < 0 or pos.bottom > h:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle, pos)

    pg.display.flip()

    clock.tick(100)

