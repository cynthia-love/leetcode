# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    自己实现一对多碰撞检测函数, 支持矩形检测和圆形检测, 支持配置True, False
"""

import sys
import random
import pygame as pg
from math import *
from pygame.locals import *

TITLE = "Collide Check"
SIZE = WIDTH, HEIGHT = 1024, 681
SIZE_BALL = WIDTH_BALL, HEIGTH_BALL = 100, 100

FRAME = 100

BALL_NUM = 10

def random_velocity():
    velocity = [random.randint(-10, 10), random.randint(-10, 10)]
    while velocity == [0, 0]:
        velocity = [random.randint(-10, 10), random.randint(-10, 10)]
    return velocity

def collide_check_rect(item, target, remove=False):

    res = pg.sprite.Group()
    for each in target:

        if abs(item.rect.x-each.rect.x) < (item.rect.width/2+each.rect.width/2) and \
                abs(item.rect.y-each.rect.y) < (item.rect.height/2+each.rect.height/2):
            res.add(each)
            if remove: target.remove(each)
    return res

# 俩都是width=height时才好使圆检测, 看俩圆心距离是否小于两个半径相加
# 比矩形检测和圆检测都好的是像素遮罩检测
def collide_check_circle(item, target, remove=False):
    res = pg.sprite.Group()
    for each in target:
        r1, r2 = item.rect.width/2, each.rect.width/2
        distance = sqrt(pow((item.rect.center[0]-each.rect.center[0]), 2) +
                        pow((item.rect.center[1]-each.rect.center[1]), 2))
        if distance < r1 + r2:
            res.add(each)
            if remove: target.remove(each)
    return res


class Ball(pg.sprite.Sprite):
    def __init__(self, pos, velocity):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("image/green_ball.png")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = pos

        self.velocity = velocity

    def _getpos(self): return self.rect.x, self.rect.y
    def _setpos(self, value): self.rect.x, self.rect.y = value
    pos = property(_getpos, _setpos)

    # 普通的移动直接self.rect.move就行了, 这里要实现越界回来
    # 批量调放group里
    def update(self, surface):

        rect = surface.get_rect()
        self.rect = self.rect.move(self.velocity)

        # 向左完全隐藏
        if self.rect.right < 0:
            self.rect.left = rect.width

        # 向右完全隐藏
        if self.rect.left > rect.width:
            self.rect.right = 0

        # 向上完全隐藏
        if self.rect.bottom < 0:
            self.rect.top = rect.height

        # 向下完全隐藏
        if self.rect.top > rect.height:
            self.rect.bottom = 0


pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode(SIZE)

image_background = pg.image.load("image/background.png").convert_alpha()

group_ball = pg.sprite.Group()

for i in range(BALL_NUM):

    pos = random.randint(0, WIDTH-WIDTH_BALL), random.randint(0, HEIGHT-HEIGTH_BALL)
    velocity = random_velocity()

    ball = Ball(pos, velocity)

    while collide_check_rect(ball, group_ball, False):
        ball.pos = random.randint(0, WIDTH-WIDTH_BALL), random.randint(0, HEIGHT-HEIGTH_BALL)
    group_ball.add(ball)

print(group_ball)

clock = pg.time.Clock()

while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

    screen.blit(image_background, (0, 0))

    group_ball.update(screen)
    group_ball.draw(screen)

    # 先update还是先draw是个问题
    # 先update, 则本帧有的操作会直接反映到本帧的绘图上
    for item in group_ball:
        group_ball.remove(item)
        if collide_check_circle(item, group_ball, False):
            item.velocity[0] = -item.velocity[0]
            item.velocity[1] = -item.velocity[1]
        group_ball.add(item)



    pg.display.flip()
    clock.tick(FRAME)
