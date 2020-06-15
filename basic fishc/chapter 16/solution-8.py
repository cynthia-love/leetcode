# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    图像的变换, 先演示图像缩放
    主要用transform模块, 方法有:
    flip, 上下左右翻转(无精度损失)
    scale, 快速缩放
    rotate, 旋转
    rotozoom, 缩放并旋转
    scale2x, 快速放大一倍
    smoothscale, 精准缩放
    chop, 裁剪
"""
import sys
import pygame as pg
from pygame.locals import *

# 窗口参数
title = "小乌龟"
size = width, height = 600, 400
bg = (255, 255, 255)

# 控制参数
ratio = 1.0
speed, step = [0, 0], 5

# 素材, 后续变换都是在原始素材基础上变的
img = pg.image.load('img/turtle.png')
img_rect = img.get_rect()


turtle_l, turtle_r = img, pg.transform.flip(img, True, False)

# 开始处理, 计算初始参数等
pg.init()
pg.display.set_caption(title)
screen = pg.display.set_mode(size)

turtle = turtle_r
pos = turtle.get_rect()

clock = pg.time.Clock()

while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

        if e.type == KEYDOWN:
            print(e)
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
            elif e.key in [K_EQUALS, K_MINUS, K_SPACE]:
                if e.key == K_EQUALS:
                    ratio += 0.1
                if e.key == K_MINUS:
                    ratio -= 0.1
                if e.key == K_SPACE:
                    ratio = 1.0

                new_size = int(img_rect.width*ratio), int(img_rect.height*ratio)

                if turtle == turtle_l:
                    turtle_l = pg.transform.smoothscale(img, new_size)
                    turtle_r = pg.transform.flip(turtle_l, True, False)
                    turtle = turtle_l
                else:
                    turtle_l = pg.transform.smoothscale(img, new_size)
                    turtle_r = pg.transform.flip(turtle_l, True, False)
                    turtle = turtle_r

                # 只改pos的width和height, 不改x和y, 即放大缩小不改变左上锚点位置
                pos.width, pos.height = new_size

    pos = pos.move(speed)

    # 这里不建议这么写, 如果放大超限比如-10, 那么这里会变成来回跳而回不到主窗口
    if pos.left < 0 or pos.right > width:
        speed[0] = step if pos.left < 0 else -step
        turtle = turtle_l if turtle == turtle_r else turtle_r

    if pos.top < 0 or pos.bottom > height:
        speed[1] = step if pos.top < 0 else -step

    screen.fill(bg)
    screen.blit(turtle, pos)

    pg.display.flip()
    clock.tick(100)



