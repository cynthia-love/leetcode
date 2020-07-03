# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Hello World
"""
"""
    pygame常用模块
    .cdrom, 访问光驱
    .cursors, 加载光驱
    .display, 访问显示设备
    .draw, 绘制形状, 线, 点
    .event, 管理事件
    .font, 使用字体
    .image, 加载和存储图片
    .key, 读取键盘按键
    .mixer, 声音
    .mouse, 鼠标
    .movie, 播放视频
    .music, 播放音频
    .overlay, 访问高级视频叠加
    .rect, 管理矩形区域
    .sndarry, 操作声音数据
    .spirit, 操作移动对象
    .surface, 管理图像和品目
    .surfarray, 管理点阵图像数据
    .time, 管理时间和帧信息
    .transform, 缩放和移动图像
"""
import pygame as pg
from pygame.locals import *
from sys import exit

# 初始化pygame
pg.init()

# 设置窗口标题
pg.display.set_caption("Hello World")

# 创建一个窗口
# flags传入0表示使用软件驱动窗口; depth表示颜色深度, 最好不要指定
screen = pg.display.set_mode((640, 480), flags=0, depth=32)

bg = pg.image.load("img/tulips.gif")
mc = pg.image.load("img/cute.gif")

# 游戏主循环
while True:
    for e in pg.event.get():
        if e.type == QUIT:
            exit()
    # 将背景图画上去
    screen.blit(bg, (0, 0))

    # 获得鼠标位置
    x, y = pg.mouse.get_pos()
    x -= mc.get_width()/2
    y -= mc.get_height()/2

    # 将光标画上去
    screen.blit(mc, (x, y))

    # 刷新画面
    pg.display.update()