# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    敌机
"""
import random
import pygame as pg

class SmallEnemy(pg.sprite.Sprite):

    def __init__(self, screen, speed):

        pg.sprite.Sprite.__init__(self)
        self.image1 = pg.image.load("image/enemy1.png").convert_alpha()
        self.image = self.image1
        self.rect = self.image.get_rect()

        self.image_destroy = [
            pg.image.load("image/enemy1_down1.png").convert_alpha(),
            pg.image.load("image/enemy1_down2.png").convert_alpha(),
            pg.image.load("image/enemy1_down3.png").convert_alpha(),
            pg.image.load("image/enemy1_down4.png").convert_alpha(),

        ]
        self.sound_destroy = pg.mixer.Sound("sound/enemy1_down.wav")
        self.sound_destroy.set_volume(0.8)

        self._active = True  # 加入毁灭状态, 则需要有一个字段存这个状态

        rect_screen = screen.get_rect()

        self.width_screen = rect_screen.width
        self.height_screen = rect_screen.height

        self.speed = speed

        self.tick = pg.time.get_ticks()

        # 初始化位置, 小飞机在-5个屏幕高度到0之间
        self.x = random.randint(0, self.width_screen-self.width)
        self.y = random.randint(-5*self.height_screen-self.height, 0-self.height)

    # 跟player一样, 重新开始时提供一个重置函数
    def reset(self):
        self.active = True
        self.x = random.randint(0, self.width_screen-self.width)
        self.y = random.randint(-5*self.height_screen-self.height, 0-self.height)

    # 移动函数, 敌机移动是自动的, 且后面可能会用group统一移动, 放update里
    # 如果移动到了下边界, 那么reset其位置
    # 也就是说, 打飞机游戏看着是无限的, 实际是一批飞机不停地完事再从上方过来
    # 由于不像playtheball里, 状态变了就基本不回去了, 那里可以用多个group存不同状态的精灵
    # 这里, 建议还是设置状态变量
    def update(self):

        # 激活状态移动
        if self.active:
            self.rect.top += self.speed

            # 这里没限制下方60像素, 即小飞机可以通过状态栏
            if self.rect.top > self.height_screen:
                self.reset()
        # 否则播放破坏效果
        else:
            tick = pg.time.get_ticks()
            if tick - self.tick >= 50:
                index = self.image_destroy.index(self.image)
                if index < len(self.image_destroy) - 1:
                    self.image = self.image_destroy[index + 1]
                else:
                    self.reset()
                self.tick = tick


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

# 中型机和大型机和小型机的逻辑基本一致
# 不过中型机的随机位置范围是-10height~0, 大型机是-15height~-5height
# 且大型机像玩家机一样有特效

class MidEnemy(pg.sprite.Sprite):

    def __init__(self, screen, speed):

        pg.sprite.Sprite.__init__(self)
        self.image1 = pg.image.load("image/enemy2.png").convert_alpha()
        self.image = self.image1
        self.rect = self.image.get_rect()

        self.image_destroy = [
            pg.image.load("image/enemy2_down1.png").convert_alpha(),
            pg.image.load("image/enemy2_down2.png").convert_alpha(),
            pg.image.load("image/enemy2_down3.png").convert_alpha(),
            pg.image.load("image/enemy2_down4.png").convert_alpha(),

        ]
        self.sound_destroy = pg.mixer.Sound("sound/enemy2_down.wav")
        self.sound_destroy.set_volume(0.8)
        self._active = True  # 加入毁灭状态, 则需要有一个字段存这个状态

        rect_screen = screen.get_rect()

        self.width_screen = rect_screen.width
        self.height_screen = rect_screen.height

        self.speed = speed

        self.tick = pg.time.get_ticks()

        # 初始化位置, 小飞机在-5个屏幕高度到0之间
        self.x = random.randint(0, self.width_screen-self.width)
        self.y = random.randint(-10*self.height_screen-self.height, 0-self.height)

    # 跟player一样, 重新开始时提供一个重置函数
    def reset(self):
        self.active = True
        self.x = random.randint(0, self.width_screen-self.width)
        self.y = random.randint(-10*self.height_screen-self.height, 0-self.height)

    # 移动函数, 敌机移动是自动的, 且后面可能会用group统一移动, 放update里
    # 如果移动到了下边界, 那么reset其位置
    # 也就是说, 打飞机游戏看着是无限的, 实际是一批飞机不停地完事再从上方过来
    def update(self):

        # 激活状态移动
        if self.active:
            self.rect.top += self.speed

            # 这里没限制下方60像素, 即小飞机可以通过状态栏
            if self.rect.top > self.height_screen:
                self.reset()
        # 否则播放破坏效果
        else:
            tick = pg.time.get_ticks()
            if tick - self.tick >= 50:
                index = self.image_destroy.index(self.image)
                if index < len(self.image_destroy) - 1:
                    self.image = self.image_destroy[index + 1]
                else:
                    self.reset()
                self.tick = tick


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

class BigEnemy(pg.sprite.Sprite):

    def __init__(self, screen, speed, frame):

        pg.sprite.Sprite.__init__(self)
        self.image1 = pg.image.load("image/enemy3_n1.png").convert_alpha()
        self.image2 = pg.image.load("image/enemy3_n2.png").convert_alpha()

        self.sound_fly = pg.mixer.Sound("sound/enemy3_flying.wav")
        self.sound_fly.set_volume(0.8)
        self.played = False  # 本次循环是否已播放音效

        self.image = self.image1
        self.rect = self.image.get_rect()

        self.image_destroy = [
            pg.image.load("image/enemy3_down1.png").convert_alpha(),
            pg.image.load("image/enemy3_down2.png").convert_alpha(),
            pg.image.load("image/enemy3_down3.png").convert_alpha(),
            pg.image.load("image/enemy3_down4.png").convert_alpha(),
            pg.image.load("image/enemy3_down5.png").convert_alpha(),
            pg.image.load("image/enemy3_down6.png").convert_alpha(),

        ]
        self.sound_destroy = pg.mixer.Sound("sound/enemy3_down.wav")
        self.sound_destroy.set_volume(0.8)
        self._active = True  # 加入毁灭状态, 则需要有一个字段存这个状态

        rect_screen = screen.get_rect()

        self.width_screen = rect_screen.width
        self.height_screen = rect_screen.height

        self.speed = speed

        self.delay = int(1000/frame)

        self.tick = pg.time.get_ticks()

        # 初始化位置, 小飞机在-5个屏幕高度到0之间
        self.x = random.randint(0, self.width_screen-self.width)
        self.y = random.randint(-5*self.height_screen-self.height, 0-self.height)

    # 跟player一样, 重新开始时提供一个重置函数
    def reset(self):
        self.active = True
        self.played = False

        self.x = random.randint(0, self.width_screen-self.width)
        self.y = random.randint(-5*self.height_screen-self.height, 0-self.height)

    # 移动函数, 敌机移动是自动的, 且后面可能会用group统一移动, 放update里
    # 如果移动到了下边界, 那么reset其位置
    # 也就是说, 打飞机游戏看着是无限的, 实际是一批飞机不停地完事再从上方过来
    def update(self):

        if self.active:
            # 更新位置
            self.rect.top += self.speed

            # 大飞机快接近屏幕上方, 播放音效
            # 当然, 这个也可以在main函数里做
            if self.rect.bottom > -50 and not self.played:
                self.sound_fly.play()
                self.played = True

            # 这里没限制下方60像素, 即小飞机可以通过状态栏
            if self.rect.top > self.height_screen:
                self.reset()

            # 更新图片
            tick = pg.time.get_ticks()
            if tick - self.tick >= self.delay:
                self.image = self.image1 if self.image == self.image2 else self.image2
                self.tick = tick
        else:
            tick = pg.time.get_ticks()
            if tick - self.tick >= self.delay:
                index = self.image_destroy.index(self.image)
                if index < len(self.image_destroy) - 1:
                    self.image = self.image_destroy[index + 1]
                else:
                    self.reset()
                self.tick = tick


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
