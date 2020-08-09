# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第二个hello world
"""
import pygame as pg
import sys

# pygame里有很多模块, init用于初始化这些模块, 让它们做好准备
pg.init()
pg.display.set_caption("第一个小游戏")

# display.set_mode创建一个surface对象, 并将它作为背景画布
size = width, height = 600, 400
screen = pg.display.set_mode(size)

# 加载图片; pygame的image.load支持的类型比tkinter多多了
# 加载完, 返回一个surface对象, 让小乌龟移动, 实际就是移动这个surface在背景surface上的位置
turtle = pg.image.load("img/turtle.png")

# 获取surface对象的矩形区域<rect(0, 0, 200, 200)>
# 注意后两个数是宽度和高度, move后保持不变
pos = turtle.get_rect()

speed = [-6, 3]  # 往左上方移动

# 死循环, 确保游戏可以不断进行下去
clock = pg.time.Clock()
while True:
    # 注意, 没有任何操作的时候, event是空的; 有, 事件入队
    # 每次循环, 先看看用户操作里有没有退出, 有直接退
    # 没有, 移动图片重新渲染, 之后进入下一轮循环
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
    pos = pos.move(speed)  # 第一次移动完变成<rect(-2, 1, 200, 200)>
    # 注意, blit是支持负值的, 此时图片的一部分会超出screen范围
    # 不建议先移动再渲染, 会丢失初始状态, 应该先渲染, 然后一系列当前状态的碰撞检测等逻辑
    # 然后再更新位置啥的

    # 移动完判断是否超限, 超限则左右翻转, 且移动方向反向; 上下只移动方向反向
    # pos.left, pos.right会自动根据位置, 大小算左右边界
    # 注意这里翻转图片不建议在循环里翻转, 会占用太多资源
    # 应该在资源载入的时候就预期到后面可能用到的各种资源, 提前转好了
    # 甚至更进一步, 直接提供各种情况的素材, 而不是在代码里转换
    if pos.left < 0 or pos.right > width:
        turtle = pg.transform.flip(turtle, True, False)  # 是否左右翻转, 是否上下
        speed[0] = -speed[0]
    if pos.top < 0 or pos.bottom > height:
        turtle = pg.transform.flip(turtle, False, True)  # 是否左右翻转, 是否上下
        speed[1] = -speed[1]

    screen.fill((255, 255, 255))  # 翻转后填充背景色
    screen.blit(turtle, pos)  # 然后把新乌龟放到背景surface上去
    # pygame里每一个图像都对应一个surface对象, 画布也不例外
    # 注意, blit之后, 得到的还是一个surface, blit并不是真的把一张图放另一张上面
    # 而是改底部图像的某些位置的像素

    pg.display.flip()
    # 将内存中缓冲好的画面一次性刷到显示器上, 即图像绘制并不是直接在原图上改, 而是画一个新图
    # 然后用flip把新图刷到显示器上和原图重叠; 所以上面才需要fill重新填充背景色

    # pg.time.delay(1000)
    # 除了强制延时, 还可以控制帧率, 即每秒钟可以切换多少次图像/刷新多少次
    clock.tick(200)  # 设置200表示每秒钟最多200帧

