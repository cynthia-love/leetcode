# -*- coding: utf-8 -*-
# Author: Cynthia
import pygame as pg
from module.const import *
from pygame.locals import *

class Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
