# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    图片生成
    受solution-19启发, 试一下生成一个指定大小的半透明遮罩, 上面盖个图片
    反过来, 也可以读取一个图片, 截取其中的部分, 再存起来
"""

import pygame as pg

RED = (255, 0, 0)

WHITE_ALPHA = (255, 255, 255, 150)
SIZE = WIDTH, HEIGHT = 1000, 1000

pg.init()
# set_mode好像不能省, 会有窗口闪一下
# 毕竟pygame不是专业处理图片的, 可以接受
pg.display.set_mode(SIZE)

surface = pg.Surface(SIZE)
surface = surface.convert_alpha(surface)
surface.fill(WHITE_ALPHA)  # convert_alpha之后颜色才能带上第四位透明度

# font = pg.font.Font(None, 20)
# text = font.render("Hello~", True, RED)
#
# rect = text.get_rect()
# rect.x = int((WIDTH-rect.width)/2)
# rect.y = int((HEIGHT-rect.height)/2)
#
# surface.blit(text, rect)

img = pg.image.load("img/apple_high.png").convert_alpha()
rect = img.get_rect()
rect.x = int((WIDTH-rect.width)/2)
rect.y = int((HEIGHT-rect.height)/2)
surface.blit(img, rect)

pg.image.save(surface, "image/generate.png")

pg.quit()