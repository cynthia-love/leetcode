# -*- coding: utf-8 -*-
# Author: Cynthia
import random
import pygame as pg
from module.const import *
from pygame.locals import *

class Supply(pg.sprite.Sprite):
    def __init__(self, type):
        pg.sprite.Sprite.__init__(self)
        if type == "bullet":
            self.image = pg.image.load("image/bullet_supply.png").convert_alpha()
        else:
            self.image = pg.image.load("image/bomb_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = SPEED_SUPPLY
        self.active = False

        # 初始化位置, 其实没什么必要
        self.rect.left = random.randint(0, WIDTH-self.rect.width)
        self.rect.bottom = -HEIGHT//5

    def release(self):
        self.active = True
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = -HEIGHT // 5

    def move(self):
        if self.active:
            self.rect.top += self.speed
            if self.rect.top >= HEIGHT:
                self.active = False
