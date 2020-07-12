# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    补给包, 包括炸弹补给包和超级子弹补给包
"""

import random
import pygame as pg


class BombSupply(pg.sprite.Sprite):

    def __init__(self, screen):
        pg.sprite.Sprite.__init__(self)

        self.screen = screen
        self.rect_screen = self.screen.get_rect()

        self.image = pg.image.load("image/bomb_supply.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.left = random.randint(0, self.rect_screen.width-self.rect.width)

        self.rect.bottom = -100

        self.speed = 5

        self.active = False

    def move(self):
        self.rect.top += self.speed

        if self.rect.top > self.rect_screen.height:
            self.active = False

    def release(self):
        self.active = True
        self.rect.left = random.randint(0, self.rect_screen.width-self.rect.width)

        self.rect.bottom = -100


class BulletSupply(pg.sprite.Sprite):

    def __init__(self, screen):
        pg.sprite.Sprite.__init__(self)

        self.screen = screen
        self.rect_screen = self.screen.get_rect()

        self.image = pg.image.load("image/bullet_supply.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.left = random.randint(0, self.rect_screen.width-self.rect.width)

        self.rect.bottom = -100

        self.speed = 5

        self.active = False

    def move(self):
        self.rect.top += self.speed

        if self.rect.top > self.rect_screen.height:
            self.active = False

    def release(self):
        self.active = True
        self.rect.left = random.randint(0, self.rect_screen.width-self.rect.width)

        self.rect.bottom = -100

