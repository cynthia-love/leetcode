# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    键盘控制乌龟移动
"""
import sys
import pygame as pg
# 导入QUIT, KEYDOWN等常量
from pygame.locals import *

pg.init()

pg.display.set_caption("小乌龟")

size = width, height = 600, 400
screen = pg.display.set_mode(size)

bg = (255, 255, 255)

speed = [0, 0]

turtle = pg.image.load("img/turtle.png")
pos = turtle.get_rect()
# 龟头朝右
turtle_l, turtle_r = turtle, pg.transform.flip(turtle, True, False)

clock = pg.time.Clock()

while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                speed = [-1, 0]
                turtle = turtle_l
            if e.key == K_RIGHT:
                speed = [1, 0]
                turtle = turtle_r
            if e.key == K_UP:
                speed = [0, -1]
            if e.key == K_DOWN:
                speed = [0, 1]
    pos = pos.move(speed)

    if pos.left < 0 or pos.right > width:
        speed[0] = -speed[0]
        turtle = turtle_l if turtle == turtle_r else turtle_r
    if pos.top < 0 or pos.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle, pos)

    pg.display.flip()
    clock.tick(100)