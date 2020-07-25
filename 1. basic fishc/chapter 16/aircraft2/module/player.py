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
        self.delay = 1000//FPS_ANIMATION
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

            if self.state in [STATE_PLAYER_FLY, STATE_PLAYER_INVINCIBLE]:
                index = self.image_fly.index(self.image)
                self.image = self.image_fly[(index+1)%len(self.image_fly)]
            else:
                index = self.image_destroy.index(self.image)
                if index < len(self.image_destroy)-1:  # 还未播放完坠毁动画
                    self.image = self.image_destroy[(index+1) % len(self.image_destroy)]
                else:
                    pg.event.post(pg.event.Event(EVENT_PLAYER_DESTROYED, {}))

                    """
                    好好理一下这块逻辑, 首先我机最后一帧坠毁图片渲染完之后需要给主函数通知
                    然后判断是不是最后一架, 不是, reset个新的, 是, 切换至STOP阶段
                    然后主函数里由于阶段转换事件处理放在了最底下, 其最终逻辑顺序为:
                    渲染->update->侦测DESTROY事件
                    
                    渲染最后一张->update里发现当前渲染的事最后一张, 不再更新图片, 给主函数发送
                    DESTROY事件, 主函数侦测到该事件, 如果生命足够, 则生命减一, 然后reset
                    
                    理想情况是这样, 现在的问题是, !主循环里取的event是循环初就取了的!, 新事件
                    并不会进到里面去, 所以遍历这一层的event的时候是侦测不到本轮update加进去的
                    DESTROY事件的, 之后进到下一次循环, 又过了一次渲染和update, 然后从队列取得
                    时候才能取到, 问题是这第二次经过意味着多了一次渲染和update以及事件抛出
                    那么怎么能实现检测特定事件而又不会get的时候把其他事件给弄出去呢?
                    两个办法
                    1. 阶段切换事件检测放在最上面, 检测到了, break, 然后把下面的渲染, 更新代码
                    再包一层放在if stage == xx里
                    2. 还是在底下进行阶段转换事件检测, 但是用:
                    pygame.event.peek(eventtype=None, pump=True)
                    Returns True if there are any events of the given type waiting on the queue
                    但是这里好像只能检测自定义事件吧, 毕竟没提供key字段, 比如检测按了某个键, 那还是得等到下一次
                    循环再循环到底下才能检测到. 其实放上面也差不多, 比如刚过了event.get()就按了某键
                    还是得等到下一次循环才能检测到
                    注意虽然peek不会把对应事件出队, 下一次循环event.get()能拿到该事件, 但后面并不会
                    处理; 而由于主循环头部就把事件队列全部get清空了, 所以下一次循环的event.peek()
                    并不会重复检测到该事件. 没问题, 此方案可行
                      
                    """
            self.tick = tick

    # state状态转换的时候有一些特殊动作, 所以声明property
    def _getstate(self): return self._state

    def _setstate(self, value):
        if self._state != value:
            # 状态转换其实就几种情况
            # FLY->DESTROY, DESTROY->INVINCIBLE, INVINCIBLE->FLY
            if self._state == STATE_PLAYER_FLY and value == STATE_PLAYER_DESTROY:
                self.image = self.image_destroy[0]
                # loops=0表示只播放一次, -1无数次, 1两次
                # 由于给定的player坠毁音效第2秒杂音较多
                # 可以指定播放时长maxtime, 单位ms, 这里表示只播放1s
                self.sound_destroy.play(loops=0, maxtime=1000)
            elif self._state == STATE_PLAYER_DESTROY and value == STATE_PLAYER_INVINCIBLE:
                self.image = self.image_fly[0]
                # 精灵class内无法取消该定时器, 所以建议逻辑全放在主函数里
                # pg.time.set_timer(EVENT_PLAYER_INVINCIBLE, TIME_INVINCIBLE)

            # 其他情况只改状态就行
        self._state = value

    state = property(_getstate, _setstate)


