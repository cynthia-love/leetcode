# -*- coding: utf-8 -*-
# Author: Cynthia

from pygame.locals import *

# 常量的定义由最一般到具体每个阶段用到的

"""通用, 不局限于本程序"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE_TRANSPARENT_HALF = (255, 255, 255, 150)
WHITE_TRANSPARENT_COMPLETE = (255, 255, 255, 0)

"""窗体相关的, 还没到游戏这一层"""
TITLE = 'Aircraft War'
SIZE = WIDTH, HEIGHT = 480, 700  # 要与背景图保持一致

"""游戏全局常量, 还没到游戏控制这一层"""
FPS = 60  # 主循环每秒至多60次, 或者说每次循环运行+延时时间至少是1000/60 ms
FPS_ANIMATION = 30  # 精灵动画的帧率, 算出来间隔tick至少为1000/30 ms

FRAME_BULLET = 5  # 子弹的发射是用帧索引控制的, 每10帧发射一次, 实际间隔时间结合主循环FPS才能算出来
# 注意, 子弹最终的射程和子弹发射频次, 子弹速度, 子弹数量都有关系

PLAY, PAUSE, STOP = 1, 2, 3

"""PLAY阶段的常量"""
STATE_PLAYER_FLY = 1
STATE_PLAYER_DESTROY = 2
STATE_PLAYER_INVINCIBLE = 3

NUM_PLAYER = 3
NUM_BOMB = 3

NUM_BULLET1 = 3
NUM_BULLET2 = 3


STATE_ENEMY_FLY = 1
STATE_ENEMY_HIT = 2
STATE_ENEMY_DESTROY = 3

NUM_ENEMY_SMALL = 1
NUM_ENEMY_MIDDLE = 25
NUM_ENEMY_BIG = 3
NUM_INC_ENEMY_SMALL = 5
NUM_INC_ENEMY_MIDDLE = 3
NUM_INC_ENEMY_BIG = 1

SPEED_PLAYER = 5
SPEED_SUPPLY = 8

SPEED_BULLET1 = 20
SPEED_BULLET2 = 20

SPEED_ENEMY_SMALL = 3
SPEED_ENEMY_MIDDLE = 2
SPEED_ENEMY_BIG = 1
SPEED_INC_ENEMY = 1

HEALTH_ENEMY_SMALL = 1
HEALTH_ENEMY_MIDDLE = 10
HEALTH_ENEMY_BIG = 20

EVENT_PLAYER_DESTROYED = USEREVENT+1
EVENT_PLAYER_INVINCIBLE = USEREVENT+2
EVENT_SUPPLY_RELEASE = USEREVENT+3
EVENT_BULLET2_EXPIRATION = USEREVENT+4

TIME_SUPPLY = 5*1000  # 每多少秒发放一次补给
TIME_BULLET2 = 18*1000  # 超级子弹持续时间
TIME_INVINCIBLE = 3*1000  # 玩家飞机每条命初始无敌时间

SCORE_SMALL = 1000
SCORE_MIDDLE = 6000
SCORE_BIG = 15000

SCORE_LEVEL1_UPGRADE = 50000
SCORE_LEVEL2_UPGRADE = 300000
SCORE_LEVEL3_UPGRADE = 600000
SCORE_LEVEL4_UPGRADE = 1000000




