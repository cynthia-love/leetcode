# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    飞机大战
    STAGE: LAUNCH->PLAY->PAUSE->TERMINATE, 分别设值0, 1, 2, 3
    注意理解大项目的开发过程, 先搭主函数框架, 然后一个个元素往里加, 加的同时配合修改主函数
"""
import sys
import random
import traceback
import pygame as pg
from module.const import *
from module.player import *
from module.enemy import *
from pygame.locals import *
from module.bullet import *


def main():
    # 先初始化全局部分
    pg.init()
    pg.display.set_caption(TITLE)
    screen = pg.display.set_mode(SIZE)
    screen_alpha = screen.convert_alpha()

    # 然后是不同阶段可能用到的素材, 先载入不会变得
    image_background = pg.image.load("image/background.png")
    rect_background = image_background.get_rect()

    pg.mixer_music.load("sound/game_music.ogg")
    pg.mixer_music.set_volume(0.2)

    # 再处理会变的东西
    player = Player(screen, SPEED_PLAYER, FRAME_SPRITE)

    # 设置all的目的是便于同一进行碰撞检测等, 不然得来三遍
    group_enemy_all = pg.sprite.Group()
    group_enemy_small = pg.sprite.Group()
    group_enemy_mid = pg.sprite.Group()
    group_enemy_big = pg.sprite.Group()

    # 子弹有点像之前的灰, 绿小球, 不同的组具有不同的行为
    # 给精灵加状态字段如声明多个group更易操作
    # 发射时机, 碰撞检测, 碰到上沿这些逻辑不仅仅涉及子弹内部
    # 所以这些逻辑放在主函数里做就好
    # group_bullet1_notactive不渲染, 用set比用group更方便
    group_bullet1_notactive = set()
    # 激活状态的弹药和notactive弹药库不一样, 其需要知道弹药的发射顺序
    # 所以这里不能直接用group
    group_bullet1_active = list()


    def add_small_enemy(num):
        for i in range(num):
            enemy = SmallEnemy(screen, SPEED_ENEMY_SMALL)
            group_enemy_small.add(enemy)
            group_enemy_all.add(enemy)

    def add_mid_enemy(num):
        for i in range(num):
            enemy = MidEnemy(screen, SPEED_ENEMY_MID)
            group_enemy_mid.add(enemy)
            group_enemy_all.add(enemy)


    def add_big_enemy(num):
        for i in range(num):
            enemy = BigEnemy(screen, SPEED_ENEMY_BIG, FRAME_SPRITE)
            group_enemy_big.add(enemy)
            group_enemy_all.add(enemy)

    def add_bullet1(num):
        for i in range(num):
            bullet = Bullet1(player, SPEED_BULLET1)
            group_bullet1_notactive.add(bullet)

    # 各各级别并不是把所有敌机速度都加1, 可能只加小的或中的
    def increase_speed(target, inc):
        for each in target:
            each.speed += inc

    # 定义各阶段的初始化函数 LAUNCH, PLAY, PAUSE, TERMINATE
    def initialize(stage_to, stage_from):
        if stage_to == PLAY:
            #  不是从暂停过来的, 重置所有游戏状态
            if stage_from == LAUNCH:
                # -1表示无限重复
                pg.mixer_music.play(-1)
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                add_bullet1(NUM_BULLET1)

            elif stage_from == PAUSE:
                pg.mixer_music.unpause()
            else:
                # 为了防止从其他需要重新开始的地方来的时候背景音乐还在继续
                # 这里强制终止背景音乐
                pg.mixer_music.stop()
                pg.mixer_music.play(-1)

                # 重置玩家飞机
                player.reset()

                # 重置敌机, 注意group的数量可能超过了初始数量
                group_enemy_all.empty()
                group_enemy_small.empty()
                group_enemy_mid.empty()
                group_enemy_big.empty()

                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)

    stage = PLAY
    initialize(stage, LAUNCH)

    clock = pg.time.Clock()
    index_frame = 0
    index_bullet = 0

    while True:

        event = pg.event.get()
        for e in event:
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()

        if stage == PLAY:

            # 响应用户键盘操作有两种方法, 一是通过KEYDOWN和KEYUP事件
            # 另一种是调用key模块的get_pressed()方法
            # 第一种仅适用于偶尔触发的键盘事件, 所以这里用第二种
            keys = pg.key.get_pressed()
            # 注意这里没用else, 所以同时按下两个键是支持的
            if keys[K_w] or keys[K_UP]: player.moveUp()
            if keys[K_s] or keys[K_DOWN]: player.moveDown()
            if keys[K_a] or keys[K_LEFT]: player.moveLeft()
            if keys[K_d] or keys[K_RIGHT]: player.moveRight()

            screen.blit(image_background, rect_background)

            screen.blit(player.image, player.rect)

            if index_frame % FRAME_BULLET1 == 0:
                if group_bullet1_notactive:
                    bullet = group_bullet1_notactive.pop()
                    group_bullet1_active.append(bullet)
                # 如果弹药库里没有呢, 那得把最先发射那个强制回收回来
                else:
                    item = group_bullet1_active.pop(0)
                    item.reset()
                    group_bullet1_active.append(item)

            index_frame += 1
            # 子弹只能这么画, 没办法用group统一处理
            for each in group_bullet1_active: screen.blit(each.image, each.rect)

            group_enemy_all.draw(screen)

            # 先处理子弹碰撞
            for each in group_bullet1_active:
                # 每一颗子弹去判断是否和敌机有碰撞, 以及是否y小于0
                collides = pg.sprite.spritecollide(each, group_enemy_all, False, pg.sprite.collide_mask)
                if each.y < 0 or collides:
                    group_bullet1_active.remove(each)
                    each.reset()  # 重新进入弹药库, 注意不能无限制地生成新的子弹, 内存会慢慢受不了的
                    group_bullet1_notactive.add(each)
                for enemy in collides:
                    if enemy.active: enemy.active = False

            # 再处理飞机碰撞
            collides = pg.sprite.spritecollide(player, group_enemy_all, False, pg.sprite.collide_mask)
            if collides:
                # 这里要判断, 非破坏状态下才能再次赋值破坏状态
                # 因为破坏状态下是不检测碰撞的
                # 如果不判断, 那每次都赋值False, 而active又用的property, 每次都从第一张破坏图开始, 就死那了
                if player.active: player.active = False
                for item in collides:
                    if item.active: item.active = False

            player.update()
            for each in group_bullet1_active: each.update()

            group_enemy_all.update()


        elif stage == PAUSE:
            pass
        else:
            pass

        pg.display.flip()
        clock.tick(FRAME)

if __name__ == '__main__':
    try:
        main()
        print("正常退出")
    except SystemExit as e:
        # 注意, sys.exit()调的时候传了参数这里才有code, 不然会输出None
        # 甚至更进一步, sys.exit()不光可以传数字, 还可以传任意字符串...
        # 那些所谓的0表示正常退出, 其他数字表示不正常是纯主观规定的
        print("调sys.exit()退出", e.code)
    except:
        pg.quit()
        traceback.print_exc()