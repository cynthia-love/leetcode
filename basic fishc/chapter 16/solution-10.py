# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    裁剪图像
    尝试用chop试试, 失败
    chop函数指定的rect并不是说裁剪得到该区域的图片
    而是把该矩形区域四条边延伸形成的十字贴(井)的竖直长条和水平长条去掉后
    剩余的四个角往中间推, 得到的新图返回

    记住关键点, 左上, 右上, 左下, 右下四个角往中间挤

    相反的一个函数是subsurface, 但这个函数未返回新surface对象, 如果需要, 调一下copy()

"""

import sys
import pygame as pg
from pygame.locals import *

# 窗口参数
title = "小乌龟"
size = width, height = 600, 400
bg = (255, 255, 255)

# 素材
img = pg.image.load('img/turtle.png')

img1 = pg.transform.chop(img, (60, 60, 30, 30))  # 这么写可以实现只切掉竖直长条部分
img2 = img.subsurface(60, 60, 30, 30).copy()

# 开始处理
pg.init()
pg.display.set_caption(title)

screen = pg.display.set_mode(size)

pos1 = img1.get_rect()
pos2 = img2.get_rect()
pos2 = pos2.move(300, 300)

clock = pg.time.Clock()

while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

    screen.fill(bg)
    screen.blit(img1, pos1)
    screen.blit(img2, pos2)

    pg.display.flip()
    clock.tick(100)