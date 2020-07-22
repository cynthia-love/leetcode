# -*- coding: utf-8 -*-
# Author: Cynthia
import pygame as pg
from module.const import *
from pygame.locals import *

"""
    子弹的state就两种, 生效状态和未生效, 所以用active就行
"""
class Bullet(pg.sprite.Sprite):
    # 子弹的发射严格依赖于player位置, 不如直接传参进来
    def __init__(self, player, side):
        pg.sprite.Sprite.__init__(self)

        self.rect_player = player.rect

        self.side = side

        if self.side == 'middle':
            self.speed = SPEED_BULLET1
            self.image = pg.image.load("image/bullet1.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.rect_player.midtop
        else:
            self.speed = SPEED_BULLET2
            self.image = pg.image.load("image/bullet2.png").convert_alpha()
            self.rect = self.image.get_rect()
            if self.side == 'left':
                self.rect.centerx = self.rect_player.centerx-32
            else:
                self.rect.centerx = self.rect_player.centerx+32
            self.rect.centery = self.rect_player.centery-22

        self.active = False

    def fire(self):
        if self.side == 'middle':
            self.rect.midbottom = self.rect_player.midtop
        else:
            if self.side == 'left':
                self.rect.centerx = self.rect_player.centerx-32
            else:
                self.rect.centerx = self.rect_player.centerx+32
            self.rect.centery = self.rect_player.centery-22
        self.active = True

    def move(self):
        if self.active:  # 这里状态也可以在主函数里控
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.active = False