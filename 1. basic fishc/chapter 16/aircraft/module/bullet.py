# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    子弹
"""
import pygame as pg

class Bullet1(pg.sprite.Sprite):

    def __init__(self, player, speed):

        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("image/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        # 子弹跟飞机绑定, 如果不想在主函数里处理, 那就把player传进来
        self.rect_player = player.rect

        # 子弹的位置其实没必要初始化, 因为发射的时候还要取飞机实时位置
        self.x, self.y = self.rect_player.midtop

        self.speed = speed

        self.active = False

    def fire(self):
        self.x, self.y = self.rect_player.midtop
        self.active = True

    # 行为很统一, 用update有利于group直接调
    # 如果预计后面要遍历一个个操作, 建议还是起个明显知道要做什么的名字
    def move(self):
        # 这里的active判不判断都行, 主函数里会判断的
        if self.active:
            self.y -= self.speed
            if self.y < 0:
                self.active = False


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


# 双排子弹

class Bullet2(pg.sprite.Sprite):

    def __init__(self, player, speed, side):

        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("image/bullet2.png").convert_alpha()
        self.rect = self.image.get_rect()
        # 子弹跟飞机绑定, 如果不想在主函数里处理, 那就把player传进来
        self.rect_player = player.rect

        # 子弹的位置其实没必要初始化, 因为发射的时候还要取飞机实时位置
        if side == 'left':
            self.x = self.rect_player.centerx-33
            self.y = self.rect_player.centery
        else:
            self.x = self.rect_player.centerx + 30
            self.y = self.rect_player.centery

        self.speed = speed

        # 两翼弹药实际上是自循环的, 发射的时候是取两边最上面的
        # 所以在初始化的时候, 就把是哪侧给定了
        self.side = side

        self.active = False


    def fire(self):
        if self.side == 'left':
            self.x = self.rect_player.centerx-33
            self.y = self.rect_player.centery
        else:
            self.x = self.rect_player.centerx + 30
            self.y = self.rect_player.centery
        self.active = True

    # 子弹有多个, 且不可操控, 建议设置update函数
    def move(self):
        if self.active:
            self.y -= self.speed
            if self.y < 0:
                self.active = False

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
