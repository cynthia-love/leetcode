# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    我方飞机
"""

import pygame as pg
from module.const import *

class Player(pg.sprite.Sprite):

    # screen参数表示精灵要渲染到哪个surface上去
    # speed控制按下方向键时飞机的移动速度
    # frame控制飞机动画的刷新帧数, 独立于游戏帧数
    def __init__(self, screen, speed, frame):
        pg.sprite.Sprite.__init__(self)

        self.image1 = pg.image.load("image/me1.png").convert_alpha()
        self.image2 = pg.image.load("image/me2.png").convert_alpha()

        self.sound_destroy = pg.mixer.Sound("sound/enemy1_down.wav")
        self.sound_destroy.set_volume(0.8)

        self.image = self.image1
        self.rect = self.image.get_rect()

        # 动画效果是来回切, 而毁灭效果是遍历一次
        self.image_destroy = [
            pg.image.load("image/me_destroy_1.png").convert_alpha(),
            pg.image.load("image/me_destroy_2.png").convert_alpha(),
            pg.image.load("image/me_destroy_3.png").convert_alpha(),
            pg.image.load("image/me_destroy_4.png").convert_alpha(),
        ]

        self._active = True  # 加入毁灭状态, 则需要有一个字段存这个状态

        rect_screen = screen.get_rect()
        self.width_screen = rect_screen.width
        self.height_screen = rect_screen.height

        self.speed = speed
        self.delay = int(1000/frame)

        self.tick = pg.time.get_ticks()

        # 初始化将飞机放在下方中间稍微往上60像素的地方
        self.x = int((self.width_screen-self.width)/2)
        self.y = self.height_screen-self.height-60

    # 游戏重新开始时, 重置飞机状态
    # 除了用函数实现, 其实还可以在active的property里实现图片和位置重置
    def reset(self):
        self.active = True

        self.x = int((self.width_screen-self.width)/2)
        self.y = self.height_screen-self.height-60

    # 添加动画效果, 注意动画的速度要独立于游戏本身的帧数
    # 这里有个问题, 当生命还有剩余的时候, player飞机怎么在坠毁动画完成后通知主应用可以重置飞机了
    # 用pg.event.post()
    def update(self):
        tick = pg.time.get_ticks()
        if tick-self.tick >= self.delay:
            if self.active:
                self.image = self.image1 if self.image == self.image2 else self.image2
            else:
                index = self.image_destroy.index(self.image)
                if index < len(self.image_destroy) - 1:
                    self.image = self.image_destroy[index + 1]
                else:
                    # 第二个参数比如KEYDOWN里的key, 不过貌似不指定也不报错
                    pg.event.post(pg.event.Event(EVENT_PLAYER_DESTROYED, dict={"some_attr": 1}))

            self.tick = tick

    # 其实有时候去定义一堆复杂参数真不如直接给用户多个简单函数调
    def moveUp(self):
        self.rect.top = max(0, self.rect.top-self.speed)

    def moveDown(self):
        self.rect.bottom = min(self.height_screen-60, self.rect.bottom+self.speed)

    def moveLeft(self):
        self.rect.left = max(0, self.rect.left-self.speed)

    def moveRight(self):
        self.rect.right = min(self.width_screen, self.rect.right+self.speed)

    def _getx(self): return self.rect.x
    def _setx(self, value): self.rect.x = value
    x = property(_getx, _setx)

    def _gety(self): return self.rect.y
    def _sety(self, value): self.rect.y = value
    y = property(_gety, _sety)

    def _getwidth(self): return self.rect.width
    width = property(_getwidth)

    def _getheight(self): return self.rect.height
    height = property(_getheight)

    def _getactive(self): return self._active
    def _setactive(self, value):
        if not value:
            self.sound_destroy.play()
            self.image = self.image_destroy[0]
        else:
            self.image = self.image1

        self._active = value
    active = property(_getactive, _setactive)
