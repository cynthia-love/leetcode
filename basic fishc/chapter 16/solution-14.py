# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    动画精灵
    指游戏开发中, 那些被赋予灵魂的事物, 比如一只小乌龟, 一条狗
    使用sprite的好处是, 我们可以把游戏里的所有角色在一个组里统一处理, 便于
    同时渲染, 移动, 碰撞检测他们
"""
"""
    第一个简单例子, 红豆吃黑豆
"""

import sys
import pygame as pg
from pygame.locals import *

import random

# define colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pg.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        # image决定该精灵长啥样
        self.image = pg.Surface((width, height))
        # 背景置白再设置透明
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pg.draw.ellipse(self.image, color, (0, 0, width, height), 0)

        # 除了image, 还得初始化rect属性
        self.rect = self.image.get_rect()


title = 'Turtle'
size = width, height = 600, 600

pg.init()
pg.display.set_caption(title)
screen = pg.display.set_mode(size)

block_list = pg.sprite.Group()

all_list = pg.sprite.Group()

for i in range(50):

    block = Block(BLACK, 20, 20)

    block.rect.x = random.randrange(width)
    block.rect.y = random.randrange(height)

    block_list.add(block)
    all_list.add(block)

player = Block(RED, 20, 20)
all_list.add(player)

clock = pg.time.Clock()

done = False

score = 0

while not done:

    for e in pg.event.get():
        if e.type == pg.QUIT:
            done = True

    screen.fill(WHITE)

    pos = pg.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # 三个参数分别为检测对象, 检测目标, 以及碰撞后是否移除这个元素
    # 返回值为被移除的精灵list
    block_hit_list = pg.sprite.spritecollide(player, block_list, True)
    print(block_hit_list)
    for block in block_hit_list:
        score += 1
        print(score)

    block_list.draw(screen)

    clock.tick(60)

    pg.display.flip()