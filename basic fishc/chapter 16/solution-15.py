# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    上一个游戏的升级版, 加入动态贴图什么的
    农民吃苹果
    这里用到更多的碰撞检测函数, 简单做个说明
    1. pygame.sprite.spritecollide(sprite,sprite_group,bool), 第一个精灵会与第二个精灵组里的
    精灵一个个去进行矩形碰撞检测, 并将有发生碰撞的作为一个列表返回; bool为True删除组中碰撞的, False不删
    2. pygame.sprite.spritecollideany(), 与1类似, 但返回是否存在碰撞的bool值
    3. pygame.sprite.groupcollide(), 检测两个组之间的矩形碰撞检测
    4. pygame.sprite.collide_rect(sprite_1,sprite_2), 两个精灵之间的矩形检测, 返回bool
    还有一个类似的pygame.sprite.collide_rect_ratio( 0.5 )(sprite_1,sprite_2), 指定碰撞多少算碰
    5. pygame.sprite.collide_circle(sprite_1,sprite_2), 两个精灵之间的圆形检测, 返回bool
    同样有一个变体pygame.sprite.collide_circle_ratio()
    6. 最关键的, 两个元素之间最有可能用到的更精确的像素遮罩检测
    pygame.sprite.collide_mask(sprite_1,sprite_2)

"""
import sys
import pygame as pg
import random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

title = 'Farmer Eat Apples'
size = width, height = 600, 600

pg.init()
pg.display.set_caption(title)
screen = pg.display.set_mode(size)

class Block(pg.sprite.Sprite):

    # 加载图片filename的第index行第column列的宽为width高为height的图片
    # 索引从0开始
    def __init__(self, filename, index, column, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image_base = pg.image.load(filename).convert_alpha()
        self.index, self.column = index, column
        self.rect_base = self.image_base.get_rect()

        rect = Rect(column*width, index*height, width, height)
        self.image = self.image_base.subsurface(rect)
        self.rect = self.image.get_rect()
        self.directions = {
            'n': 0,
            'e': 2,
            's': 4,
            'w': 6
        }

    # 根据绝对tick去更新图片
    def update(self, direction, speed):
        self.index = self.directions[direction]
        if direction == 'n':
            self.rect.y -= speed
        if direction == 'e':
            self.rect.x += speed
        if direction == 's':
            self.rect.y += speed
        if direction == 'w':
            self.rect.x -= speed

        width_dis = pg.display.Info().current_w
        height_dis = pg.display.Info().current_h

        if self.rect.x < 0: self.rect.x = 0
        if self.rect.right > width_dis: self.rect.x = width_dis-self.rect.width
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.bottom > height_dis: self.rect.y = height_dis-self.rect.height

        if self.column == 7: self.column = 0
        else: self.column += 1
        rect = Rect(self.column*self.rect.width, self.index*self.rect.height,
                    self.rect.width, self.rect.height)
        self.image = self.image_base.subsurface(rect)


group_player = pg.sprite.Group()
player = Block("img/farmer.png", 0, 0, 96, 96)
group_player.add(player)

group_apple = pg.sprite.Group()
for i in range(50):
    apple = Block("img/food_low.png", 0, 0, 35, 35)
    apple.rect.x = random.randint(50, 550)
    apple.rect.y = random.randint(50, 550)
    group_apple.add(apple)

clock = pg.time.Clock()
moving, direction = False, 0

while True:
    ticks_old = pg.time.get_ticks()
    ticks_rel = clock.tick(100)
    ticks_new = pg.time.get_ticks()
    """
    好好理解这两个tick
    clock.tick()有点像sleep函数, 只不过参数是最大帧数, 每秒10帧, 意味着延时100ms
    time.get_ticks()返回自pg.init()后的绝对时间, 举例某一次循环这三个值分别为:
    550 100 650
    由于循环体里还有其它代码, 所以帧数不会达到10的
    想计算实际的帧数, 把ticks_new放到循环体最后, 算出来见个时间, 再用1s去除以
    """

    for e in pg.event.get():

        if e.type == QUIT:
            sys.exit()

        if e.type == KEYDOWN:
            if e.key == K_UP:
                moving = True
                direction = 'n'
            if e.key == K_RIGHT:
                moving = True
                direction = 'e'
            if e.key == K_DOWN:
                moving = True
                direction = 's'
            if e.key == K_LEFT:
                moving = True
                direction = 'w'

        if e.type == KEYUP:
            if e.key in [K_UP, K_RIGHT, K_DOWN, K_LEFT]:
                moving = False

    # 直接这么调, 即每次循环更新一次, 即每帧更新一次
    if moving:
        group_player.update(direction, 5)
        # hit_list = pg.sprite.spritecollide(player, group_apple, True)
        for apple in group_apple:
            if pg.sprite.collide_mask(player, apple):
                group_apple.remove(apple)

    screen.fill(WHITE)
    group_player.draw(screen)
    group_apple.draw(screen)
    pg.display.flip()



