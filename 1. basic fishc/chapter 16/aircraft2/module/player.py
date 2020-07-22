# -*- coding: utf-8 -*-
# Author: Cynthia
import pygame as pg
from module.const import *
from pygame.locals import *
"""
    理清楚我方飞机的几个状态:
    状态1, 可控, 可碰撞, 喷气动画
    状态2, 被碰撞, 播放音效, 破坏动画
    状态3, 重置状态, 无敌, 可控, 有动画效果, 无碰撞
"""
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # 加载资源
        self.image_fly = [
            pg.image.load("image/me1.png").convert_alpha(),
            pg.image.load("image/me2.png").convert_alpha()
        ]
        self.image_destroy = [
            pg.image.load("image/me_destroy_1.png").convert_alpha(),
            pg.image.load("image/me_destroy_2.png").convert_alpha(),
            pg.image.load("image/me_destroy_3.png").convert_alpha(),
            pg.image.load("image/me_destroy_4.png").convert_alpha()
        ]
        self.sound_destroy = pg.mixer.Sound("sound/me_down.wav")

        self.image = self.image_fly[0]
        self.rect = self.image.get_rect()

        self.speed = SPEED_PLAYER
        self.delay = 10000//FPS_ANIMATION
        self.tick = pg.time.get_ticks()

        # 定义初始状态
        self._state = STATE_PLAYER_FLY
        self.rect.left = (WIDTH-self.rect.width) // 2
        self.rect.bottom = HEIGHT-60

    def reset(self):
        self.state = STATE_PLAYER_INVINCIBLE  # 新生命开始无敌一段时间
        self.rect.left = (WIDTH-self.rect.width) // 2
        self.rect.bottom = HEIGHT-60

    def move(self, orient):
        if orient == 'n':
            self.rect.top = max(0, self.rect.top-self.speed)
        if orient == 's':
            self.rect.bottom = min(HEIGHT-60, self.rect.bottom+self.speed)
        if orient == 'w':
            self.rect.left = max(0, self.rect.left-self.speed)
        if orient == 'e':
            self.rect.right = min(WIDTH, self.rect.right+self.speed)

    def update(self):
        # 更新动画, 其FPS独立于游戏主循环FPS, 且小于等于
        tick = pg.time.get_ticks()
        # 达到了预期延时
        if tick-self.tick >= self.delay:
            self.tick = tick

            if self.state in [STATE_PLAYER_FLY, STATE_PLAYER_INVINCIBLE]:
                index = self.image_fly.index(self.image)
                self.image = self.image_fly[(index+1)%len(self.image_fly)]
            else:
                index = self.image_destroy.index(self.image)

                if index < len(self.image_destroy)-1:  # 还未播放完坠毁动画
                    self.image = self.image_fly[(index+1) % len(self.image_fly)]
                else:
                    # 销毁结束后要通知主函数, 主函数判断还有没有剩余生命
                    pg.event.post(pg.event.Event(EVENT_PLAYER_DESTROYED, {}))

    # state状态转换的时候有一些特殊动作, 所以声明property
    def _getstate(self): return self._state

    def _setstate(self, value):
        if self._state != value:
            # 状态转换其实就几种情况
            # FLY->DESTROY, DESTROY->INVINCIBLE, INVINCIBLE->FLY
            if self._state == STATE_PLAYER_FLY and value == STATE_PLAYER_DESTROY:
                self.image = self.image_destroy[0]
                self.sound_destroy.play()
            if self._state == STATE_PLAYER_DESTROY and value == STATE_PLAYER_INVINCIBLE:
                self.image = self.image_fly[0]
                # 精灵class内无法取消该定时器, 所以建议逻辑全放在主函数里
                # pg.time.set_timer(EVENT_PLAYER_INVINCIBLE, TIME_INVINCIBLE)

            # 其他情况只改状态就行
            self._state = value

    state = property(_getstate, _setstate)


