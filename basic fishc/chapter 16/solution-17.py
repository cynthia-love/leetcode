# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    播放音乐
    注意, 音乐是单启动了一个线程进行的
    此样例实现播放背景音乐, 点按钮播放猫叫, 暂停或播放完毕
"""
import sys
import math
import pygame as pg
from pygame.locals import *

WHITE = (255, 255, 255)

TITLE = 'PLAY MUSIC'
SIZE = WIDTH, HEIGHT = 600, 600

FRAME = 100

pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode(SIZE)

# pygame里支持两种播放
# 一种是音乐, mp3, ogg, wma等, 用pg.mixer_music模块
# 另一种是声音, wav, 用pg.mixer模块
# 两个模块的get_busy()函数互相独立

pg.mixer_music.load('sound/bg_music.ogg')
pg.mixer_music.set_volume(0.3)
pg.mixer_music.play(-1)  # 第一个参数是播放次数, -1表示循环播放


# mixer相对于mixer_music, 后者有点像pyplot, 而mixer能直接拿到声音对象;
cat_sound = pg.mixer.Sound('sound/cat.wav')
# 如果要对声音进行精细化管理, Sound本身就没那么多什么定义结束事件等的方法了, 得用channel
cat_sound.set_volume(0.3)
channel = pg.mixer.find_channel()  # 这个方法比自己指定通道号好
channel.set_endevent(USEREVENT+3)  # 后面加的数字是自己随便定的

# 不要学了精灵就什么都用精灵了
image_play = pg.image.load('image/pause.png').convert_alpha()
image_pause = pg.image.load('image/unpause.png').convert_alpha()
# 这俩图片一般大, 位置计算一次就行
rect = image_play.get_rect()
rect.x = int((WIDTH-rect.width)/2)
rect.y = int((HEIGHT-rect.height)/2)

clock = pg.time.Clock()

# 状态0, 初始状态; 点播放, 状态1, 点暂停状态2, 再点状态1; 播放完状态0
# 养成这种思路, 比设置一堆字段要好
state = 0

def collidepoint(rect, point):

    distance = math.sqrt(math.pow(rect.center[0]-point[0], 2) +
                         math.pow(rect.center[1]-point[1], 2))
    return distance <= rect.width/2

while True:
    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

        # 这里collidepoint建议自己写, 去判断点是否在圆内而不是矩形内, 因为图标是圆形的
        # rect自带的collidepoint是矩形检测
        if e.type == MOUSEBUTTONDOWN and collidepoint(rect, e.pos):
            if state == 0:
                pg.mixer_music.pause()
                channel.play(cat_sound)
                state = 1
            elif state == 1:
                channel.pause()
                pg.mixer_music.unpause()
                state = 2
            elif state == 2:
                pg.mixer_music.pause()
                channel.unpause()
                state = 1

        if e.type == USEREVENT + 3:
            pg.mixer_music.unpause()
            state = 0

    screen.fill(WHITE)

    # 这里图片切换也可以放在上面事件逻辑里, 但不建议, 用作记忆状态的参数尽量少
    if state == 0 or state == 2:
        screen.blit(image_play, rect)
    else:
        screen.blit(image_pause, rect)

    pg.display.flip()
    clock.tick(FRAME)
