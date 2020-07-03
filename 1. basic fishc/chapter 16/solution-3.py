# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    将事件打印到屏幕上
    pygame没有直接显示文字的功能
    需要调用font模块的render方法将文本渲染成Surface对象
"""
import sys
import pygame as pg

pg.init()
pg.display.set_caption("Hello")

size = width, height = 600, 400
screen = pg.display.set_mode(size)

bg = (0, 0, 0)

font = pg.font.Font(None, 20)  # 字体和尺寸

line_height = font.get_linesize()
# 字体尺寸和行高好像不是一回事, 这里行高为15

pos = 0

screen.fill(bg)
# 所谓的游戏, 就是一个死循环
while True:

    for e in pg.event.get():
        # 注意事件不用在窗口里也能捕获
        if e.type == pg.QUIT:
            sys.exit()
        if e.type == pg.ACTIVEEVENT:
            print('active', e.gain, e.state)
        if e.type == pg.KEYDOWN:
            print('keydown', e.key, e.mod)
        if e.type == pg.KEYUP:
            print('keyup', e.key, e.mod)
        if e.type == pg.MOUSEMOTION:
            print('mousemotion', e.pos, e.rel)  # e.pos是绝对位置, e.rel是相对于上个位置的移动
        if e.type == pg.MOUSEBUTTONDOWN:
            print('mousebuttondown', e.pos, e.button)  # e.pos鼠标点击时位置, button 1左3右
        if e.type == pg.MOUSEBUTTONUP:
            print('mousebuttonup', e.pos, e.button)
        if e.type == pg.VIDEORESIZE:
            print('videoresize', e.size, e.w, e.h)
        surface = font.render(str(e), True, (0, 255, 0))  # 文本, 是否消除锯齿, 颜色
        screen.blit(surface, (0, pos))

        pos += line_height

        if pos > height:
            screen.fill(bg)  # 一行行加, 不会覆盖, 没必要重新涂背景
            pos = 0

    pg.display.flip()  # 也可以放在内存循环, 每有一个事件刷一次