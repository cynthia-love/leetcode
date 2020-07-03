# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    solution-4的变体, 将移动代码放到for循环里面
    这样只有按键的时候才会移动
"""
import sys
import pygame as pg

from pygame.locals import *

pg.init()

pg.display.set_caption("小乌龟")

size = width, height = 600, 400
screen = pg.display.set_mode(size)

bg = (255, 255, 255)

speed, step = [0, 0], 20

turtle_l = pg.image.load("img/turtle.png")
turtle_r = pg.transform.flip(turtle_l, True, False)

turtle = turtle_r
pos = turtle.get_rect()

clock = pg.time.Clock()

# 显示初始画面
screen.fill(bg)
screen.blit(turtle, pos)
pg.display.flip()

while True:
    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            print(e)
            if e.key == K_LEFT:
                speed = [-step, 0]
                turtle = turtle_l
            if e.key == K_RIGHT:
                speed = [step, 0]
                turtle = turtle_r
            if e.key == K_UP:
                speed = [0, -step]
            if e.key == K_DOWN:
                speed = [0, step]

            pos = pos.move(speed)

            if pos.left < 0 or pos.right > width:
                speed[0] = -speed[0]
                pos = pos.move(speed)

            if pos.top < 0 or pos.bottom > height:
                speed[1] = -speed[1]
                pos = pos.move(speed)

            screen.fill(bg)
            screen.blit(turtle, pos)

            pg.display.flip()
            clock.tick(100)

