# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    转换图片
    pygame里, 到处都是surface对象, surface是pygame对图像的描述
"""
import sys
import pygame as pg
from pygame.locals import *

title = 'Turtle'
size = width, height = 600, 600
bg = (0, 255, 0)

pg.init()
pg.display.set_caption(title)
screen = pg.display.set_mode(size)

# image.load返回原图像的像素格式, 调convert()转换成统一像素格式
# 否则后面blit的时候, 如果两个surface像素格式不一样,需要实时转换, 影响性能
# 如果图片包含alpha通道(0透明, 255不透明), 那么用convert_alpha()
img1 = pg.image.load('img/turtle.png').convert_alpha()
pos1 = img1.get_rect()

# 如果图片本身没有alpha通道, 那调convert_alpha是没用的, 调convert就行
# 即要么调convert(), 要么调convert_alpha(), 不要什么都不调
img2 = pg.image.load('img/turtle.jpeg').convert()
pos2 = img2.get_rect()
pos2 = pos2.move(0, 200)

"""
对于非透明图片, pygame也可以为其增加透明度设置, 有三种方法:
1. set_colorkey(color), 指定一种颜色, 将其设置为透明
2. set_alpha(透明度), 设置整个图片的透明度, 可以和1配合使用
3. pixel alphas, 每个像素有自己单独的alpha通道, convert_alpha()返回的就是这种
"""
img3 = img2.copy()
pos3 = img3.get_rect()
pos3 = pos3.move(0, 400)
img3.set_alpha(200)  # 设置整个图片透明度
img3.set_colorkey((255, 255, 255))  # 将某种颜色设置完全透明

# 带alpha通道的, 单独修改每个像素的透明度; 透明的地方不改, 不透明的地方设置透明150
img4 = img1.copy()
pos4 = img4.get_rect()
pos4 = pos4.move(200, 0)
for i in range(pos4.width):
    for j in range(pos4.height):
        pixel = img4.get_at((i, j))
        if pixel[3] != 0:
            pixel[3] = 200
        img4.set_at((i, j), pixel)

img5 = img1.copy()
pos5 = img5.get_rect()
pos5 = pos5.move(200, 200)
# 有时候4这种方式效果不好怎么办, 反向考虑
# 搞一个和小乌龟大小相同的区域, 默认全黑, 先盖上背景, 再盖上小乌龟, 整个设置透明度
# 然后将这个surface对象整体渲染

clock = pg.time.Clock()

while True:
    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

    screen.fill(bg)
    screen.blit(img1, pos1)
    screen.blit(img2, pos2)
    screen.blit(img3, pos3)
    screen.blit(img4, pos4)

    temp = pg.Surface((pos5.width, pos5.height)).convert()  # 得到一个和小乌龟等大小的全黑矩形
    temp.blit(screen, (-pos5.x, -pos5.y))
    # 理解这句话什么意思; blit函数, 将目标surface画到自己身上, 以自己左上角为0, 0
    # 这里相当于temp黑框不动, 将screen往左上移动, 移动完和temp重合的部分正是小乌龟五号将要处在位置的背景图
    temp.blit(img5, (0, 0))  # 将乌龟五号画到这个小背景图上
    temp.set_alpha(150)  # 将这块图片设置透明度
    screen.blit(temp, pos5)
    """
    为什么修改带alpha通道的图片透明度, 五的方法会比四的好呢???
    因为原来的透明图并不是非黑即白的, 边缘部分不是从0一下变成250, 每个部分的透明度可能是不一样的
    方法四把非0的全都改成200, 原来小于200的也改了(这里是不是也提供了一种优化方法4的思路)
    如果直接用set_alpha的话问题更大, 全图都统一透明度了, 而我们要的效果更像是按比例修改透明度
    原来100的变60, 原来60的变36, 原来0的乘以0.6还是0 (嗯....这种思路好像和方法五比起来也不差)
    
    为什么方法五效果好呢
    先将目标区域的背景截出来, 画上原小乌龟, 合成之后这张图就没alpha通道了
    然后整体设置透明度, 小乌龟的区域透明了背后是背景; 非小乌龟的区域透明了, 还是原背景
    从而实现只有小乌龟透明的效果
    """

    pg.display.flip()
    clock.tick(100)