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

        self.x, self.y = self.rect_player.midtop

        self.speed = speed


    def reset(self):
        self.x, self.y = self.rect_player.midtop

    # 子弹有多个, 且不可操控, 建议设置update函数
    def update(self):

        self.y -= self.speed

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


# 双排子弹, reset的时候要指定是左边还是右边

class Bullet2(pg.sprite.Sprite):

    def __init__(self, player, speed):

        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("image/bullet2.png").convert_alpha()
        self.rect = self.image.get_rect()
        # 子弹跟飞机绑定, 如果不想在主函数里处理, 那就把player传进来
        self.rect_player = player.rect

        self.speed = speed

        self.side = 'left'
        self.reset(self.side)


    def reset(self, side='left'):
        self.side = side
        if side == 'left':
            self.x = self.rect_player.centerx-33
            self.y = self.rect_player.centery
        else:
            self.x = self.rect_player.centerx + 30
            self.y = self.rect_player.centery

    # 子弹有多个, 且不可操控, 建议设置update函数
    def update(self):

        self.y -= self.speed

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
