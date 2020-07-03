# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    旋转
    让小乌龟逆时针贴着边走
"""

import sys
import pygame as pg
from pygame.locals import *
from collections import deque

# 窗口参数
title = "小乌龟"
size = width, height = 600, 400
bg = (0, 255, 0)

# 控制参数
speed, step, state = [0, 0], 5, deque()

# 素材
turtle_r_b = pg.image.load("img/turtle_small_r.png")
turtle_u_r = pg.transform.rotate(turtle_r_b, 90)
turtle_l_u = pg.transform.rotate(turtle_r_b, 180)
turtle_b_l = pg.transform.rotate(turtle_r_b, 270)

# 开始处理
pg.init()
pg.display.set_caption(title)

screen = pg.display.set_mode(size)

turtle = turtle_r_b
rect = turtle.get_rect()
rect = rect.move([0, height-rect.height])

clock = pg.time.Clock()

while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                # 走走停停基本逻辑
                # 如果本来是停着的, 看是初始还是中间停的
                if speed == [0, 0]:  # 当前停着的, 那按一下得动, 分为初始动和中间继续动
                    if not state:
                        speed = [step, 0]  # 初始停着时, 栈空
                    else:
                        speed = state.pop()  # 非初始, 栈里有上次的速度, 取出来
                else:
                    state.append(speed)  # 当前不是停着的, 那按一下得停, 记住当前状态
                    speed = [0, 0]

    rect = rect.move(speed)

    if rect.right > width:
        turtle = turtle_u_r
        rect = turtle.get_rect()
        rect = rect.move([width-rect.width, height-rect.height])
        # 注意这里四个顶点计算方式不一样, 要计算的是矩形左上角的坐标
        speed = [0, -step]

    if rect.top < 0:
        turtle = turtle_l_u
        rect = turtle.get_rect()
        rect = rect.move([width-rect.width, 0])
        speed = [-step, 0]

    if rect.left < 0:
        turtle = turtle_b_l
        rect = turtle.get_rect()
        rect = rect.move([0, 0])
        speed = [0, step]

    if rect.bottom > height:
        turtle = turtle_r_b
        rect = turtle.get_rect()
        rect = rect.move([0, height-rect.height])
        speed = [step, 0]

    screen.fill(bg)
    screen.blit(turtle, rect)

    pg.display.flip()
    clock.tick(100)