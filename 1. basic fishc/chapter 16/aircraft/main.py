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
from module.supply import *


def main():
    # 先初始化全局部分
    pg.init()
    pg.display.set_caption(TITLE)
    screen = pg.display.set_mode(SIZE)
    screen_alpha = screen.convert_alpha()
    font_score = pg.font.Font("font/font.TTF", 36)
    font_bomb = pg.font.Font("font/font.TTF", 48)

    # 然后是不同阶段可能用到的素材, 先载入不会变得
    image_background = pg.image.load("image/background.png")
    rect_background = image_background.get_rect()

    image_pause1 = pg.image.load("image/pause_nor.png").convert_alpha()
    image_pause2 = pg.image.load("image/pause_pressed.png").convert_alpha()

    image_resume1 = pg.image.load("image/resume_nor.png").convert_alpha()
    image_resume2 = pg.image.load("image/resume_pressed.png").convert_alpha()

    image_bomb = pg.image.load("image/bomb.png").convert_alpha()
    rect_bomb = image_bomb.get_rect()


    image_life = pg.image.load("image/life.png").convert_alpha()
    rect_life = image_life.get_rect()


    rect_pause_resume = image_pause1.get_rect()

    pg.mixer_music.load("sound/game_music.ogg")
    pg.mixer_music.set_volume(0.2)

    sound_upgrade = pg.mixer.Sound("sound/upgrade.wav")
    sound_bomb_use = pg.mixer.Sound("sound/use_bomb.wav")
    sound_bomb_get = pg.mixer.Sound("sound/get_bomb.wav")
    sound_supply = pg.mixer.Sound("sound/supply.wav")
    sound_bullet_get = pg.mixer.Sound("sound/get_bullet.wav")

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

    group_bullet2_notactive = set()

    group_bullet2_active = list()

    supply_bomb = BombSupply(screen)
    supply_bullet = BulletSupply(screen)


    def add_small_enemy(num):
        for i in range(num):
            enemy = SmallEnemy(screen, SPEED_ENEMY_SMALL, HEALTH_ENEMY_SMALL)
            group_enemy_small.add(enemy)
            group_enemy_all.add(enemy)

    def add_mid_enemy(num):
        for i in range(num):
            enemy = MidEnemy(screen, SPEED_ENEMY_MID, HEALTH_ENEMY_MID)
            group_enemy_mid.add(enemy)
            group_enemy_all.add(enemy)


    def add_big_enemy(num):
        for i in range(num):
            enemy = BigEnemy(screen, SPEED_ENEMY_BIG, HEALTH_ENEMY_BIG, FRAME_SPRITE)
            group_enemy_big.add(enemy)
            group_enemy_all.add(enemy)

    def add_bullet1(num):
        for i in range(num):
            bullet = Bullet1(player, SPEED_BULLET1)
            group_bullet1_notactive.add(bullet)

    def add_bullet2(num):
        for i in range(num):
            bullet = Bullet2(player, SPEED_BULLET2)
            group_bullet2_notactive.add(bullet)

    # 各各级别并不是把所有敌机速度都加1, 可能只加小的或中的
    def increase_speed(target, inc):
        for each in target:
            each.speed += inc

    # 定义各阶段的初始化函数 LAUNCH, PLAY, PAUSE, TERMINATE
    # 由于初始化函数还要初始化一些基本类型变量, 这些变量记得用nonlocal
    # 或者用一个字典或者类存这些变量


    class rt:
        image_pause_resume = image_pause1
        index_frame = 0
        score = 0
        level = 1
        num_bomb = NUM_BOMB
        # 设想一种情况, 吃到双倍子弹, 用了5秒, 暂停, 再回来, 应该还能继续用13秒
        # 用set_timer实现不了这个效果, 不如找个字段直接存当前双倍剩余时间以及基准时间
        # 吃到新的子弹补给更新剩余时长和基准时间
        # 每一帧判断, 如果当前tick-tick_base超过了剩余时间, 那么剩余时间置为0
        # 如果点了暂停, 判断还有没有剩余时间, 如果有, 存下来还剩多少
        # 由暂停再回来的时候, 更新基准时间
        bullet_double = 0
        tick_base = 0

        num_player = 3

        group_bullet_active = group_bullet1_active
        group_bullet_notactive = group_bullet1_notactive

    def initialize(stage_to, stage_from):


        if stage_to == PLAY:

            rt.image_pause_resume = image_pause1
            rect_pause_resume.x = WIDTH - rect_pause_resume.width - 10
            rect_pause_resume.top = 10

            rect_bomb.x = 10
            rect_bomb.y = HEIGHT-rect_bomb.height-10

            # 重置发放补给的计时器, 每30秒发一次
            pg.time.set_timer(TIMER_SUPPLY, 0)  # 为防止其他场景没终止计时器, 这里终止一下
            pg.time.set_timer(TIMER_SUPPLY, 5*1000)

            #  不是从暂停过来的, 重置所有游戏状态
            if stage_from == LAUNCH:
                # -1表示无限重复
                pg.mixer_music.play(-1)
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                add_bullet1(NUM_BULLET1)
                add_bullet2(NUM_BULLET2)

                rt.index_frame = 0
                rt.score = 0
                rt.level = 1
                rt.num_bomb = NUM_BOMB
                rt.num_player = 3

            elif stage_from == PAUSE:
                pg.mixer_music.unpause()
                rt.tick_base = pg.time.get_ticks()
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

                rt.index_frame = 0
                rt.score = 0
                rt.level = 1
                rt.num_bomb = NUM_BOMB
                rt.num_player = 3

        elif stage_to == PAUSE:
            # 到PAUSE的只可能来源于PLAY, 所以不用判断from
            rt.image_pause_resume = image_resume1
            pg.time.set_timer(TIMER_SUPPLY, 0)

            if rt.bullet_double:
                rt.bullet_double -= pg.time.get_ticks()-rt.tick_base
        else:
            pg.time.set_timer(TIMER_SUPPLY, 0)
            pg.mixer_music.stop()

    stage = PLAY
    initialize(stage, LAUNCH)

    clock = pg.time.Clock()

    # 一些简单的页面要素就别去创建精灵类了, 直接在主函数里画

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

            # 这里炸弹不能用第二种键盘事件方式
            # 第二种无法区分一次按下, 比如快速按一下空格, 可能接下来的几次
            # 循环, 都会识别空格是按下的
            for e in event:
                if e.type == KEYDOWN and e.key == K_SPACE:
                    if rt.num_bomb:
                        rt.num_bomb -= 1
                        sound_bomb_use.play()
                        for each in group_enemy_all:
                            if each.active:
                                each.active = 0
                                if each in group_enemy_small:
                                    rt.score += 1000
                                if each in group_enemy_mid:
                                    rt.score += 6000
                                if each in group_enemy_big:
                                    rt.score += 10000
                if e.type == TIMER_SUPPLY:
                    sound_supply.play()

                    if random.choice([True, False]):
                        supply_bomb.release()
                    else:
                        supply_bullet.release()

            screen.blit(image_background, rect_background)
            screen.blit(rt.image_pause_resume, rect_pause_resume)

            # 下角画炸弹
            text_bomb = font_bomb.render("x {}".format(rt.num_bomb), True, WHITE)
            rect_bomb_text = text_bomb.get_rect()
            rect_bomb_text.x = rect_bomb.right+10
            rect_bomb_text.y = HEIGHT-rect_bomb_text.height-5
            screen.blit(image_bomb, rect_bomb)
            screen.blit(text_bomb, rect_bomb_text)

            screen.blit(player.image, player.rect)

            for i in range(rt.num_player):
                rect_life.bottom = HEIGHT - 10
                rect_life.right = WIDTH - 10 - i * rect_life.width
                screen.blit(image_life, rect_life)

            # 这里除了每隔一定帧去发射子弹, 也可以通过设置set_timer
            # 每隔一段时间给一个该发射子弹的信号
            # 先判断当前是否处于双倍时间


            if rt.bullet_double:
                rt.group_bullet_active = group_bullet2_active
                rt.group_bullet_notactive = group_bullet2_notactive
            else:
                rt.group_bullet_active = group_bullet1_active
                rt.group_bullet_notactive = group_bullet1_notactive

            if rt.index_frame % FRAME_BULLET == 0:
                if rt.group_bullet_notactive:
                    bullet = rt.group_bullet_notactive.pop()
                    rt.group_bullet_active.append(bullet)
                # 如果弹药库里没有呢, 那得把最先发射那个强制回收回来
                # 这就是为什么group_bullet1_active得设置成有顺序的list
                else:
                    item = rt.group_bullet_active.pop(0)
                    item.reset()
                    rt.group_bullet_active.append(item)

                # 2号子弹的弹药默认是左翼发射的
                # 如果判断是2号, 右翼还得发射一发
                # 不行, 不能这么写, 如果一边一直碰撞, 那一直从弹药库里取
                # 另一边弹药就会超过1/2*NUM_BULLET2
                # 而子弹射程应该是固定的
                # 建议独立俩弹道出来
                # 用三个, fire_left, fire_middle, fire_right
                # 但是这么写有个坏处, 画图, 移动, 碰撞检测等地方都得来好几遍代码
                # 要么就设立个active参数, 发射的时候无脑取最前面俩, 不管是不是碰撞了
                # 然后pop, append虽然少了index逻辑判断, 但性能应该不如那个好
                # 可以给子弹一个位置参数, left, right
                if rt.group_bullet_active == group_bullet2_active:
                    if rt.group_bullet_notactive:
                        bullet = rt.group_bullet_notactive.pop()
                        bullet.reset(side='right')
                        rt.group_bullet_active.append(bullet)
                    else:
                        item = rt.group_bullet_active.pop(0)
                        item.reset(side='right')
                        rt.group_bullet_active.append(item)

            rt.index_frame += 1
            # 子弹只能这么画, 没办法用group统一处理
            for each in rt.group_bullet_active: screen.blit(each.image, each.rect)

            group_enemy_all.draw(screen)

            if rt.bullet_double:
                if pg.time.get_ticks()-rt.tick_base >= rt.bullet_double:
                    rt.bullet_double = TIME_DOUBLE_BULLET
            # 处理补给
            if supply_bomb.active:
                screen.blit(supply_bomb.image, supply_bomb.rect)
                if pg.sprite.collide_mask(player, supply_bomb):
                    sound_bomb_get.play()
                    if rt.num_bomb < 3: rt.num_bomb += 1
                    supply_bomb.active = False
                else:
                    supply_bomb.move()

            if supply_bullet.active:
                screen.blit(supply_bullet.image, supply_bullet.rect)
                if pg.sprite.collide_mask(player, supply_bullet):
                    sound_bullet_get.play()
                    rt.bullet_double = TIME_DOUBLE_BULLET
                    rt.tick_base = pg.time.get_ticks()
                    supply_bullet.active = False
                else:
                    supply_bullet.move()
            # 先处理子弹碰撞
            for each in rt.group_bullet_active:
                # 每一颗子弹去判断是否和敌机有碰撞, 以及是否y小于0
                collides = pg.sprite.spritecollide(each, group_enemy_all, False, pg.sprite.collide_mask)
                if each.y < 0 or collides:
                    rt.group_bullet_active.remove(each)
                    each.reset()  # 重新进入弹药库, 注意不能无限制地生成新的子弹, 内存会慢慢受不了的
                    rt.group_bullet_notactive.add(each)
                for enemy in collides:
                    if enemy.active:
                        enemy.energy -= 1
                        enemy.hit = True
                        if enemy.energy == 0:
                            enemy.active = False
                            if enemy in group_enemy_small:
                                rt.score += 1000
                            if enemy in group_enemy_mid:
                                rt.score += 6000
                            if enemy in group_enemy_big:
                                rt.score += 10000

                # 击中之后, 下一帧, 如果没击中, 就要把hit字段改回来, 取消显示击中图片
                for each in group_enemy_mid:
                    if each not in collides:
                        each.hit = False
                for each in group_enemy_big:
                    if each not in collides:
                        each.hit = False

            # 中大飞机的三种状态都画血条就行了
            for each in group_enemy_mid: each.showHealth()
            for each in group_enemy_big: each.showHealth()

            # 画分数
            text_score = font_score.render("Score: {}".format(rt.score), True, WHITE)
            screen.blit(text_score, (10, 5))

            # 再处理飞机碰撞
            if not player.invincible:
                collides = pg.sprite.spritecollide(player, group_enemy_all, False,
                                                   pg.sprite.collide_mask)
                if collides:
                    # 这里要判断, 非破坏状态下才能再次赋值破坏状态
                    # 因为破坏状态下是不检测碰撞的
                    # 如果不判断, 那每次都赋值False, 而active又用的property, 每次都从第一张破坏图开始, 就死那了
                    if player.active:
                        player.active = False

                    for item in collides:
                        if item.active: item.active = False

            player.update()
            for each in rt.group_bullet_active: each.update()

            # 在敌机下一次移动之前, 根据分数判断是否升级
            if rt.level == 1 and rt.score >= 50000:
                rt.level = 2
                sound_upgrade.play()
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                increase_speed(group_enemy_small, SPEED_INC)
            elif rt.level == 2 and rt.score >= 300000:
                rt.level = 3
                sound_upgrade.play()
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                increase_speed(group_enemy_small, SPEED_INC)
                increase_speed(group_enemy_mid, SPEED_INC)
            elif rt.level == 3 and rt.score >= 600000:
                rt.level = 4
                sound_upgrade.play()
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                increase_speed(group_enemy_small, SPEED_INC)
                increase_speed(group_enemy_mid, SPEED_INC)
            elif rt.level == 4 and rt.score >= 1000000:
                rt.level = 5
                sound_upgrade.play()
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                increase_speed(group_enemy_small, SPEED_INC)
                increase_speed(group_enemy_mid, SPEED_INC)

            group_enemy_all.update()

            # 暂停按钮为什么要放后面, 因为改了状态后不希望继续执行下面的代码了
            for e in event:
                if e.type == MOUSEMOTION and rect_pause_resume.collidepoint(e.pos):
                    rt.image_pause_resume = image_pause2
                else:
                    rt.image_pause_resume = image_pause1

                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if rect_pause_resume.collidepoint(e.pos):
                        stage = PAUSE
                        initialize(stage, PLAY)
                        # 注意这里的break, 一旦点了暂停, 那要立即改变游戏的阶段
                        # 不能再往下遍历其他事件, 否则可能把图片改回去
                        break
                if e.type == EVENT_PLAYER_DESTROYED:
                    if rt.num_player > 1:
                        player.reset()
                        rt.num_player -= 1
                        player.invincible = True
                        pg.time.set_timer(TIMER_INVINCIBLE, 3*1000)
                    else:
                        stage = TERMINATE
                        initialize(stage, PLAY)
                        break
                if e.type == TIMER_INVINCIBLE:
                    player.invincible = False

        elif stage == PAUSE:
            # 暂停状态所有要素都画, 只不过不更新
            screen.blit(image_background, (0, 0))
            screen.blit(player.image, player.rect)
            for each in rt.group_bullet_active: screen.blit(each.image, each.rect)
            group_enemy_all.draw(screen)
            for each in group_enemy_mid: each.showHealth()
            for each in group_enemy_big: each.showHealth()
            text_score = font_score.render("Score: {}".format(rt.score), True, WHITE)
            screen.blit(text_score, (10, 5))

            # 下角画炸弹
            text_bomb = font_bomb.render("x {}".format(rt.num_bomb), True, WHITE)
            rect_bomb_text = text_bomb.get_rect()
            rect_bomb_text.x = rect_bomb.right+10
            rect_bomb_text.y = HEIGHT-rect_bomb_text.height-5
            screen.blit(image_bomb, rect_bomb)
            screen.blit(text_bomb, rect_bomb_text)


            for i in range(rt.num_player):
                rect_life.bottom = HEIGHT - 10
                rect_life.right = WIDTH - 10 - i * rect_life.width
                screen.blit(image_life, rect_life)

            if supply_bomb.active:
                screen.blit(supply_bomb.image, supply_bomb.rect)

            screen_alpha.fill(WHITE_TRANSPARENT)
            screen_alpha.blit(rt.image_pause_resume, rect_pause_resume)
            screen.blit(screen_alpha, (0, 0))

            for e in event:
                if e.type == MOUSEMOTION and rect_pause_resume.collidepoint(e.pos):
                    rt.image_pause_resume = image_resume2
                else:
                    rt.image_pause_resume = image_resume1

                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if rect_pause_resume.collidepoint(e.pos):
                        stage = PLAY
                        initialize(stage, PAUSE)
                        break

        else:
            screen.blit(image_background, (0, 0))

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