# -*- coding: utf-8 -*-
# Author: Cynthia
import random
import pygame as pg
from module.const import *
from pygame.locals import *

# 敌机的状态FLY->被攻击特效->击毁动画效果->FLY
# 注意敌机不同于子弹, 补给还有无效状态, 其击毁后无缝切换到FLY状态
# 所以state给3个取值就够; 特别地小飞机没有HIT状态, 击中一次就挂
# 理论上, 额外再设置个血量变量就够使了(只一个血量是不行的, 不满血也可能是非HIT状态)

class EnemySmall(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_fly = pg.image.load("image/enemy1.png").convert_alpha()
        self.image_destroy = [
            pg.image.load("image/enemy1_down1.png").convert_alpha(),
            pg.image.load("image/enemy1_down2.png").convert_alpha(),
            pg.image.load("image/enemy1_down3.png").convert_alpha(),
            pg.image.load("image/enemy1_down4.png").convert_alpha()

        ]
        self.sound_destroy = pg.mixer.Sound("sound/enemy1_down.wav")

        self.speed = SPEED_ENEMY_SMALL
        self._health = HEALTH_ENEMY_SMALL  # 小飞机也要画血条, 所以也声明个health参数吧

        self._state = STATE_ENEMY_FLY
        self.image = self.image_fly
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(self.rect.width, WIDTH)
        self.rect.bottom = random.randint(-5 * HEIGHT, 0)

        self.tick = pg.time.get_ticks()
        self.delay = 1000 // FPS_ANIMATION

        self.screen = pg.display.get_surface()  # 精灵可以自己获取最底层screen, 不用主函数传

    # 表面上看到的敌机是无限的, 其实是有限的
    def reset(self):
        self.state = STATE_ENEMY_FLY
        self.rect.right = random.randint(self.rect.width, WIDTH)
        self.rect.bottom = random.randint(-5 * HEIGHT, 0)

    def update(self):
        if self.state == STATE_ENEMY_FLY:
            self.rect.top += self.speed
            if self.rect.top >= HEIGHT:
                self.reset()
        else:
            tick = pg.time.get_ticks()
            if tick-self.tick >= self.delay:
                index = self.image_destroy.index(self.image)
                if index < len(self.image_destroy) - 1:
                    self.image = self.image_destroy[index + 1]
                else:
                    self.reset()
                self.tick = tick

    # 血条用粗线段就行, 没必要一定要矩形; 位置稍微往上点
    def showHealth(self):
        percent = self.health / HEALTH_ENEMY_SMALL
        color  = GREEN if percent > 0.2 else RED
        pg.draw.line(self.screen, WHITE, (self.rect.left, self.rect.top-5), (self.rect.right, self.rect.top-5), 2)
        pg.draw.line(self.screen, color, (self.rect.left, self.rect.top-5),
                     (self.rect.left+int(self.rect.width*percent), self.rect.top-5), 2)

    def _getstate(self): return self._state
    def _setstate(self, value):
        # 小敌机state变化就两种情况, FLY->DESTROY, DESTROY->FLY
        if self._state == STATE_ENEMY_FLY and value == STATE_ENEMY_DESTROY:
            self.sound_destroy.play()
            self.image = self.image_destroy[0]
        elif self._state == STATE_ENEMY_DESTROY and value == STATE_ENEMY_FLY:
            # 这俩逻辑放reset里面其实也可以
            self.image = self.image_fly
            self.health = HEALTH_ENEMY_SMALL
        self._state = value
    state = property(_getstate, _setstate)

    def _gethealth(self): return self._health
    def _sethealth(self, value):
        if value < self._health:
            if value == 0:
                self.state = STATE_ENEMY_DESTROY
            else:
                self.state = STATE_ENEMY_HIT
        self._health = value

    health = property(_gethealth, _sethealth)

class EnemyMiddle(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_fly = pg.image.load("image/enemy2.png").convert_alpha()
        self.image_hit = pg.image.load("image/enemy2_hit.png").convert_alpha()
        self.image_destroy = [
            pg.image.load("image/enemy2_down1.png").convert_alpha(),
            pg.image.load("image/enemy2_down2.png").convert_alpha(),
            pg.image.load("image/enemy2_down3.png").convert_alpha(),
            pg.image.load("image/enemy2_down4.png").convert_alpha()

        ]

        self.sound_destroy = pg.mixer.Sound("sound/enemy2_down.wav")

        self.speed = SPEED_ENEMY_MIDDLE
        self._health = HEALTH_ENEMY_MIDDLE

        self._state = STATE_ENEMY_FLY
        self.image = self.image_fly
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(self.rect.width, WIDTH)
        self.rect.bottom = random.randint(-10 * HEIGHT, -1 * HEIGHT)

        self.tick = pg.time.get_ticks()
        self.delay = 1000 // FPS_ANIMATION

        self.screen = pg.display.get_surface()  # 精灵可以自己获取最底层screen, 不用主函数传

    # 表面上看到的敌机是无限的, 其实是有限的
    def reset(self):
        # 搞一堆property, 省一堆参数, 真不如多写几行, 虽然容易漏改变量, 但至少逻辑简单了
        self.state = STATE_ENEMY_FLY
        self.image = self.image_fly
        self.health = HEALTH_ENEMY_MIDDLE
        self.rect.right = random.randint(self.rect.width, WIDTH)
        self.rect.bottom = random.randint(-10 * HEIGHT, -1 * HEIGHT)

    def update(self):
        if pg.event.peek(EVENT_ENEMY_HIT_EXPIRATION):
            pg.time.set_timer(EVENT_ENEMY_HIT_EXPIRATION, 0)
            if self.state == STATE_ENEMY_FLY and self.image == self.image_hit:
                self.image = self.image_fly


        if self.state in [STATE_ENEMY_FLY, STATE_ENEMY_HIT]:
            self.rect.top += self.speed
            if self.rect.top >= HEIGHT:
                self.reset()
        else:
            tick = pg.time.get_ticks()
            if tick - self.tick >= self.delay:
                index = self.image_destroy.index(self.image)
                if index < len(self.image_destroy) - 1:
                    self.image = self.image_destroy[index + 1]
                else:
                    self.reset()
                self.tick = tick

    # 血条用粗线段就行, 没必要一定要矩形; 位置稍微往上点
    def showHealth(self):
        percent = self.health / HEALTH_ENEMY_MIDDLE
        color  = GREEN if percent > 0.2 else RED
        pg.draw.line(self.screen, WHITE, (self.rect.left, self.rect.top-5), (self.rect.right, self.rect.top-5), 2)
        pg.draw.line(self.screen, color, (self.rect.left, self.rect.top-5),
                     (self.rect.left+int(self.rect.width*percent), self.rect.top-5), 2)


    def _getstate(self):
        return self._state

    def _setstate(self, value):
        # 中型机state变化有, FLY->HIT, FLY->DESTROY, HIT->DESTROY, DESTROY->FLY
        # 以及HIT->FLY(击中几下然后就不攻击了)
        if self._state == STATE_ENEMY_FLY and value == STATE_ENEMY_HIT:
            self.image = self.image_hit
        elif self._state == STATE_ENEMY_FLY and value == STATE_ENEMY_DESTROY:
            self.sound_destroy.play()
            self.image = self.image_destroy[0]
        elif self._state == STATE_ENEMY_HIT and value == STATE_ENEMY_DESTROY:
            self.sound_destroy.play()
            self.image = self.image_destroy[0]
        elif self._state == STATE_ENEMY_DESTROY and value == STATE_ENEMY_FLY:
            self.image = self.image_fly
            self.health = HEALTH_ENEMY_MIDDLE
        elif self._state == STATE_ENEMY_HIT and value == STATE_ENEMY_FLY:
            # 如果只用state变量有个小问题, 状态改变是实时的, 比如某一帧碰撞
            # 了, 显示hit图片, 下一帧没碰, 不希望变那么快, 不然肉眼分辨不出来
            # self.image = self.image_fly
            pg.time.set_timer(EVENT_ENEMY_HIT_EXPIRATION, 100)
            # 这里不改, 在update里判断, 如果100ms后, 状态是FLY且图片是hit, 改成FLY的

        self._state = value

    state = property(_getstate, _setstate)

    def _gethealth(self):
        return self._health

    def _sethealth(self, value):
        if value < self._health:
            if value == 0:
                self.state = STATE_ENEMY_DESTROY
            else:
                self.state = STATE_ENEMY_HIT
        self._health = value

    health = property(_gethealth, _sethealth)

class EnemyBig(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_fly = [
            pg.image.load("image/enemy3_n1.png").convert_alpha(),
            pg.image.load("image/enemy3_n2.png").convert_alpha()
        ]
        self.image_hit = pg.image.load("image/enemy3_hit.png").convert_alpha()
        self.image_destroy = [
            pg.image.load("image/enemy3_down1.png").convert_alpha(),
            pg.image.load("image/enemy3_down2.png").convert_alpha(),
            pg.image.load("image/enemy3_down3.png").convert_alpha(),
            pg.image.load("image/enemy3_down4.png").convert_alpha(),
            pg.image.load("image/enemy3_down5.png").convert_alpha(),
            pg.image.load("image/enemy3_down6.png").convert_alpha()

        ]
        self.sound_close = pg.mixer.Sound("sound/enemy3_flying.wav")
        self.sound_destroy = pg.mixer.Sound("sound/enemy3_down.wav")

        self.speed = SPEED_ENEMY_BIG
        self._health = HEALTH_ENEMY_BIG

        self._state = STATE_ENEMY_FLY
        self.image = self.image_fly[0]
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(self.rect.width, WIDTH)
        self.rect.bottom = random.randint(-15 * HEIGHT, -5 * HEIGHT)

        self.tick = pg.time.get_ticks()
        self.delay = 1000 // FPS_ANIMATION

        self.screen = pg.display.get_surface()  # 精灵可以自己获取最底层screen, 不用主函数传

    # 表面上看到的敌机是无限的, 其实是有限的
    def reset(self):
        self.state = STATE_ENEMY_FLY
        self.image = self.image_fly[0]
        self.health = HEALTH_ENEMY_BIG
        self.rect.right = random.randint(self.rect.width, WIDTH)
        self.rect.bottom = random.randint(-15 * HEIGHT, -5 * HEIGHT)

    def update(self):
        # 大飞机的image_fly有俩, 不能跟中飞机一样
        # 中飞机hit一下, state变hit, image变hit, state变fly
        # 100ms以后, update里接到hit事件, 去改image
        # 问题是没接到这个事件之前呢, 中飞机无所谓, state为fly也可以渲染hit图片
        # 但是大飞机有fly图片切换逻辑, 这时候fly图片list里定位不到当前图片, 就抛错了
        # 底下加上一句if self.image == self.image_hit: return
        # 感觉本来想省一个self.hit, 直接用self.state包含各种情况
        # 结果省了之后逻辑更乱了....还得处理各种特殊情况, 还不如多变量, 切状态的时候多赋几个值而已
        if pg.event.peek(EVENT_ENEMY_HIT_EXPIRATION):
            pg.time.set_timer(EVENT_ENEMY_HIT_EXPIRATION, 0)
            if self.state == STATE_ENEMY_FLY and self.image == self.image_hit:
                self.image = self.image_fly[0]

        if self.state == STATE_ENEMY_FLY:
            if self.rect.bottom <= -50 <= self.rect.bottom + self.speed:
                self.sound_close.play()

            self.rect.top += self.speed
            if self.rect.top >= HEIGHT:
                self.reset()

            tick = pg.time.get_ticks()
            if tick-self.tick >= self.delay:
                if self.image == self.image_hit: return
                index = self.image_fly.index(self.image)
                self.image = self.image_fly[(index+1)%len(self.image_fly)]
                self.tick = tick

        elif self.state == STATE_ENEMY_HIT:
            self.rect.top += self.speed
            if self.rect.top >= HEIGHT:
                self.reset()
        else:
            tick = pg.time.get_ticks()
            if tick - self.tick >= self.delay:
                index = self.image_destroy.index(self.image)
                if index < len(self.image_destroy) - 1:
                    self.image = self.image_destroy[index + 1]
                else:
                    self.reset()
                self.tick = tick

    # 血条用粗线段就行, 没必要一定要矩形; 位置稍微往上点
    def showHealth(self):
        percent = self.health / HEALTH_ENEMY_BIG
        color  = GREEN if percent > 0.2 else RED
        pg.draw.line(self.screen, WHITE, (self.rect.left, self.rect.top-5), (self.rect.right, self.rect.top-5), 2)
        pg.draw.line(self.screen, color, (self.rect.left, self.rect.top-5),
                     (self.rect.left+int(self.rect.width*percent), self.rect.top-5), 2)


    def _getstate(self):
        return self._state

    def _setstate(self, value):
        # 大型机state变化和中型机一样, FLY->HIT, FLY->DESTROY, HIT->DESTROY, DESTROY->FLY
        # 以及HIT->FLY(击中几下然后就不攻击了)
        # 唯一区别在于, 切换到FLY状态的图片有多个, 需要指定第一个
        if self._state == STATE_ENEMY_FLY and value == STATE_ENEMY_HIT:
            self.image = self.image_hit
        elif self._state == STATE_ENEMY_FLY and value == STATE_ENEMY_DESTROY:
            self.sound_destroy.play()
            self.image = self.image_destroy[0]
        elif self._state == STATE_ENEMY_HIT and value == STATE_ENEMY_DESTROY:
            self.sound_destroy.play()
            self.image = self.image_destroy[0]
        elif self._state == STATE_ENEMY_DESTROY and value == STATE_ENEMY_FLY:
            self.image = self.image_fly[0]
            self.health = HEALTH_ENEMY_BIG
        elif self._state == STATE_ENEMY_HIT and value == STATE_ENEMY_FLY:
            # self.image = self.image_fly[0], 过100ms后再改
            pg.time.set_timer(EVENT_ENEMY_HIT_EXPIRATION, 100)

        self._state = value

    state = property(_getstate, _setstate)

    def _gethealth(self):
        return self._health

    def _sethealth(self, value):
        if value < self._health:
            if value == 0:
                self.state = STATE_ENEMY_DESTROY
            else:
                self.state = STATE_ENEMY_HIT
        self._health = value

    health = property(_gethealth, _sethealth)