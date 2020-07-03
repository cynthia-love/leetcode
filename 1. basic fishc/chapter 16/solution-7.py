# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    使窗口尺寸可变
    一般不会让改, 因为内部的元素不跟着改会影响展示效果
    跟着改, 会增加很多的开发量
"""

import sys
import pygame as pg
from pygame.locals import *

pg.init()

pg.display.set_caption("小乌龟")

size = width, height = 600, 400

bg = (255, 255, 255)

screen = pg.display.set_mode(size, flags=RESIZABLE)

speed, step = [0, 0], 5

img_l = pg.image.load('img/turtle.png')
img_r = pg.transform.flip(img_l, True, False)

# 实际开发的时候不会在代码里频繁转换吧, 先提前转换了存起来???
# 不然每次生成一个新的对象内存受不了???
turtle_l, turtle_r = img_l, img_r

turtle = turtle_r
pos = turtle.get_rect()

clock = pg.time.Clock()

while True:

    for e in pg.event.get():

        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                speed = [-step, 0]
                turtle = turtle_l
            elif e.key == K_RIGHT:
                speed = [step, 0]
                turtle = turtle_r
            elif e.key == K_UP:
                speed = [0, -step]
            elif e.key == K_DOWN:
                speed = [0, step]

        if e.type == VIDEORESIZE:
            size = width, height = e.size
            screen = pg.display.set_mode(size, RESIZABLE)

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