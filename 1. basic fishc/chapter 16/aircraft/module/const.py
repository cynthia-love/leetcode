# -*- coding: utf-8 -*-
# Author: Cynthia
from pygame.locals import *

# 通用常量
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WHITE_TRANSPARENT = (255, 255, 255, 150)
WHITE_TRANSPARENT_COMPLETE = (255, 255, 255, 0)

# SURFACE相关的
TITLE = 'Aircraft War'
SIZE = WIDTH, HEIGHT = 480, 700
FRAME = 100  # 整个游戏的FPS
FRAME_SPRITE = 15  # 精灵动画的FPS
FRAME_BULLET = 10  # 子弹每几帧发射一次
# 注意这个参数和子弹个数及速度有关系
# 如果这个值很小, 那么先发出去的子弹会很快重新发射
# 在子弹数量不多且速度不够快的情况下, 会导致整个火力距离过短

# 其他游戏相关的
LAUNCH, PLAY, PAUSE, TERMINATE = 0, 1, 2, 3

SPEED_PLAYER = 10  # 玩家每按一下的移动速度
SPEED_BULLET1 = 5  # 子弹每一帧的移动距离
SPEED_BULLET2 = 5

SPEED_ENEMY_SMALL = 3  # 小飞机每一帧的移动距离
SPEED_ENEMY_MID = 2  # 中飞机的每一帧移动距离
SPEED_ENEMY_BIG = 1  # 打飞机的每一帧移动距离

HEALTH_ENEMY_SMALL = 1
HEALTH_ENEMY_MID = 8
HEALTH_ENEMY_BIG = 20

NUM_ENEMY_SMALL = 10
NUM_ENEMY_MID = 3
NUM_ENEMY_BIG = 1

NUM_BULLET1 = 4
NUM_BULLET2 = 4  # 超级子弹一侧的个数, 两侧一共8个

NUM_BOMB = 3

NUM_INC_SMALL = 5
NUM_INC_MID = 3
NUM_INC_BIG = 1

SPEED_INC = 1

TIMER_SUPPLY = USEREVENT+1
TIMER_BULLET = USEREVENT+2
TIMER_INVINCIBLE = USEREVENT+3

TIME_DOUBLE_BULLET = 18*1000

EVENT_PLAYER_DESTROYED = USEREVENT+4





