# -*- coding: utf-8 -*-
# Author: Cynthia

from pygame.locals import *

# 常量的定义由最一般到具体每个阶段用到的

# 通用, 不局限于本程序
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WHITE_TRANSPARENT_HALF = (255, 255, 255, 150)
WHITE_TRANSPARENT_COMPLETE = (255, 255, 255, 0)

# 窗体相关的, 还没到游戏这一层
TITLE = 'Aircraft War'
SIZE = WIDTH, HEIGHT = 480, 700  # 要与背景图保持一致

# 游戏全局常量
FPS = 100  # 游戏整体FPS

PLAY, PAUSE, STOP = 1, 2, 3

# PLAY阶段的常量
NUM_PLAYER = 3
NUM_BOMB = 3
