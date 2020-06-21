# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    动画精灵
    指游戏开发中, 那些被赋予灵魂的事物, 比如一只小乌龟, 一条狗
    使用sprite的好处是, 我们可以把游戏里的所有角色在一个组里统一处理, 便于
    同时渲染, 移动, 而且sprite还提供了各种碰撞检测函数等
"""
"""
    第一个简单例子, 红豆吃黑豆
"""

import pygame as pg
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
r = 20

pg.init()
pg.display.set_caption(title)
screen = pg.display.set_mode(size)

block_list = pg.sprite.Group()
all_list = pg.sprite.Group()

# 这里为什么要生成两个
# 因为其中一个用于

for i in range(50):

    block = Block(BLACK, r, r)

    block.rect.x = random.randrange(width-2*r)
    block.rect.y = random.randrange(height-2*r)

    block_list.add(block)
    all_list.add(block)

player = Block(RED, r, r)
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
    player.rect.center = pos

    # player.rect.x = pos[0]-int(0.5*player.rect.width)
    # player.rect.y = pos[1]-int(0.5*player.rect.height)

    # 三个参数分别为检测对象, 检测目标, 以及碰撞后是否移除这个元素
    # 返回值为被移除的精灵list
    # 这里还要注意, 虽然移除的是block_list里的精灵, 但all_list里的也会同步移除
    # 即消除的是这个精灵本身, 而不仅仅是list里的pop
    block_hit_list = pg.sprite.spritecollide(player, block_list, True)

    # 这里用for循环因为是有可能一次碰撞多个的
    for block in block_hit_list:
        score += 1
        print(score)

    # 移除的时候用block_list, 但是draw的时候用的是all_list, 因为all_list里多了player
    # 但all_list里被碰撞的元素也没了, sprite会帮忙处理这些
    all_list.draw(screen)

    pg.display.flip()
    
    clock.tick(60)
