# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    绘制简单图形
"""
import sys
from math import *
import pygame as pg

from pygame.locals import *

title = 'Turtle'
size = width, height = 600, 600
bg = (255, 255, 255)

color = (0, 0, 0)

pg.init()
pg.display.set_caption(title)
screen = pg.display.set_mode(size)

clock = pg.time.Clock()
circle_pos = (300, 100)

while True:
    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            circle_pos = pg.mouse.get_pos()

    screen.fill(bg)

    # 四个参数, 在哪画, 颜色, 左上角坐标和宽高, 边框大小(0填充)
    pg.draw.rect(screen, (0, 255, 0), (0, 0, 200, 200), 0)

    pg.draw.rect(screen, color, (0, 200, 200, 200), 1)

    # 多边形, 类似tkinter里的canvas
    x, y, r = 100, 500, 100
    points = [
        (x - int(r * sin(0.4 * pi)), y - int(r * cos(0.4 * pi))),
        (x + int(r * sin(0.4 * pi)), y - int(r * cos(0.4 * pi))),
        (x - int(r * sin(0.2 * pi)), y + int(r * cos(0.2 * pi))),
        (x, y-r),
        (x + int(r * sin(0.2 * pi)), y + int(r * cos(0.2 * pi))),
    ]

    pg.draw.polygon(screen, color, points, 1)

    # 圆形, 参数3指定圆心, 参数4半径
    pg.draw.circle(screen, color, circle_pos, 100, 1)

    # 椭圆形, 参数三指定矩形, 正方形画出来的就是圆
    pg.draw.ellipse(screen, color, (200, 200, 200, 200), 1)
    pg.draw.ellipse(screen, color, (200, 450, 200, 100), 1)

    # 弧形, 和椭圆一样, 也是先指定矩形, 然后指定开始角度, 结束角度, 即椭圆的一部分
    pg.draw.arc(screen, color, (400, 50, 200, 100), 0, pi, 1)

    # 绘制线段
    pg.draw.line(screen, color, (400, 280), (600, 320), 1)

    # 绘制多条, 类似于polygon(), 参数三指定最后一个点是否和第一个点有连线
    # 与polygon的区别在于, 这里的width不能指定0
    x, y, r = 500, 500, 100
    points = [
        (x - int(r * sin(0.4 * pi)), y - int(r * cos(0.4 * pi))),
        (x + int(r * sin(0.4 * pi)), y - int(r * cos(0.4 * pi))),
        (x - int(r * sin(0.2 * pi)), y + int(r * cos(0.2 * pi))),
        (x, y-r),
        (x + int(r * sin(0.2 * pi)), y + int(r * cos(0.2 * pi))),
    ]
    pg.draw.lines(screen, (255, 0, 0), True, points, 1)

    # 抗锯齿划线, 这里最后一个参数不是width, 而是表示是否通过绘制混合背景的阴影来实现抗锯齿功能
    pg.draw.aaline(screen, color, (400, 300), (600, 340), 1)
    pg.draw.aaline(screen, color, (400, 320), (600, 360), 0)

    pg.display.flip()
    clock.tick(100)  # 每秒绘制100次
