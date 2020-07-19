# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    飞机大战
"""
"""
    先明确几个阶段: PLAY, PAUSE, STOP, 分别设置阶段状态码1, 2, 3
    
"""
import os
import sys
import random
import traceback
import pygame as pg
from module.const import *
from module.player import *
from module.bullet import *
from module.enemy import *
from module.supply import *
from pygame.locals import *


# 获取程序所在目录, 兼容.py和.exe
def getpath(filename):
    if sys.path[0].endswith(".zip"):
        return sys.path[0].replace("base_library.zip", filename)
    else:
        return os.path.join(sys.path[0], filename)

# 声明一个类管理全部资源, 至于要用到哪些变量, 对着UI图一个个往里码就行了

class Resource:
    # __init__函数里只声明变量, 声明顺序可以按由大到小, 由上到下, 由静到动来
    # 包括后面的初始化以及再后面的渲染, 也可以按这个顺序来, 更清晰
    # 另外, 从头开始写程序的时候建议先搭架子出来, 什么意思呢
    # 先把各阶段简单的背景图, 分数, 暂停键什么的的逻辑写了, 把PLAY, PAUSE, STOP串起来
    # 然后再去一个个添加复杂的player, enemy什么的(这里也提供了一种思路, 到底什么样的要素要独立成精灵)
    def __init__(self):

        """PLAY阶段"""
        # 背景图
        self.s1_img_bg = self.s1_rect_bg = None
        # 左上角分数
        self.s1_font_score = self.s1_text_score = self.s1_rect_score = None
        # 右上角暂停
        self.s1_img_pause = self.s1_rect_pause = None
        self.s1_img_pause_pressed = self.s1_rect_pause_pressed = None
        # 左下角炸弹
        self.s1_img_bomb = self.s1_rect_bomb = None
        self.s1_font_bombtxt = self.s1_text_bombtxt = self.s1_rect_bombtxt = None
        # 右下角剩余生命数
        self.s1_img_life = self.s1_rect_life = None

        """PAUSE阶段"""
        # 右上角继续键
        self.s2_img_resume = self.s2_rect_resume = None
        self.s2_img_resume_pressed = self.s2_rect_resume_pressed = None
        """STOP阶段"""

    def init(self):
        # 也不是所有的元素都能在这里初始化, 比如有一些文字需要渲染的时候才能知道渲染什么
        """PLAY阶段"""
        # 背景图
        self.s1_img_bg = pg.image.load("image/background.png")
        self.s1_rect_bg = self.s1_img_bg.get_rect()
        # 左上角分数, text和其rect运行时生成
        self.s1_font_score = pg.font.Font("font/font.TTF", 36)
        # 右上角暂停
        self.s1_img_pause = pg.image.load("image/pause_nor.png").convert_alpha()
        self.s1_rect_pause = self.s1_img_pause.get_rect()
        self.s1_rect_pause.right = WIDTH - 10
        self.s1_rect_pause.top = 10
        self.s1_img_pause_pressed = pg.image.load(
            "image/pause_pressed.png").convert_alpha()
        self.s1_rect_pause_pressed = self.s1_rect_pause
        # 左下角炸弹, text和其rect运行时生成
        self.s1_img_bomb = pg.image.load("image/bomb.png").convert_alpha()
        self.s1_rect_bomb = self.s1_img_bomb.get_rect()
        self.s1_rect_bomb.left = 10
        self.s1_rect_bomb.bottom = HEIGHT - 10
        self.s1_font_bombtxt = pg.font.Font("font/font.TTF", 48)
        # 右下角剩余生命数
        self.s1_img_life = pg.image.load("image/life.png").convert_alpha()
        self.s1_rect_life = self.s1_img_life.get_rect()

        """PAUSE阶段"""
        self.s2_img_resume = pg.image.load("image/resume_nor.png").convert_alpha()
        self.s2_rect_resume = self.s1_rect_pause  # 位置一样, 可以直接借用
        self.s2_img_resume_pressed = pg.image.load("image/resume_pressed.png").convert_alpha()
        self.s2_rect_resume_pressed = self.s1_rect_pause_pressed


def main():
    pg.init()
    pg.display.set_caption(TITLE)
    screen = pg.display.set_mode(SIZE)
    rect_screen = screen.get_rect()  # 声明了备用
    screen_alpha = screen.convert_alpha()
    rect_screen_alpha = screen_alpha.get_rect()  # 声明了备用

    r = Resource()

    stage = PLAY
    r.init()

    # 各个阶段都要用到的变量
    clock = pg.time.Clock()


    """PLAY阶段"""
    s1_score = 0
    s1_img_pause = r.s1_img_pause  # pause这里rect没必要再声明个变量了, 因为位置一样, 实在不行用三元表达式也行, 总比多个变量强
    s1_num_bomb = NUM_BOMB
    s1_num_player = NUM_PLAYER

    s1_frame = 0  # PLAY阶段运行的帧索引
    s1_leftb = 0  # 记录剩余时长, 给双倍子弹计时用的
    s1_tickb = 0  # 记录基准时间, 给双倍子弹计时用的

    """PAUSE阶段"""
    s2_img_resume = r.s2_img_resume

    while True:

        event = pg.event.get()
        for e in event:
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_SPACE:
                sys.exit()

        if stage == PLAY:
            # 1. 先画背景图
            screen.blit(r.s1_img_bg, r.s1_rect_bg)
            # 2. 再画左上角分数
            r.s1_text_score = r.s1_font_score.render("Score: {}".format(s1_score), True, WHITE)
            r.s1_rect_score = r.s1_text_score.get_rect()
            r.s1_rect_score.topleft = (10, 5)
            screen.blit(r.s1_text_score, r.s1_rect_score)
            # 3. 再画右上角暂停键
            screen.blit(s1_img_pause, r.s1_rect_pause if s1_img_pause == r.s1_img_pause else r.s1_rect_pause_pressed)
            # 4. 再画左下角炸弹数
            screen.blit(r.s1_img_bomb, r.s1_rect_bomb)
            r.s1_text_bombtxt = r.s1_font_bombtxt.render(" x {}".format(s1_num_bomb), True, WHITE)
            r.s1_rect_bombtxt = r.s1_text_bombtxt.get_rect()
            r.s1_rect_bombtxt.left = r.s1_rect_bomb.right + 10
            r.s1_rect_bombtxt.bottom = HEIGHT - 8
            screen.blit(r.s1_text_bombtxt, r.s1_rect_bombtxt)
            # 5. 画右下角生命数
            for i in range(s1_num_player):
                r.s1_rect_life.bottom = HEIGHT - 10
                r.s1_rect_life.right = WIDTH - 10 - i*r.s1_rect_life.width
                screen.blit(r.s1_img_life, r.s1_rect_life)

            # -2. 暂停键的图片切换不建议用瞬时事件去判断, 比如点了暂停后鼠标是在继续按钮上的, 但因为没移动, 不会变黑
            if r.s1_rect_pause.collidepoint(pg.mouse.get_pos()):
                s1_img_pause = r.s1_img_pause_pressed
            else:
                s1_img_pause = r.s1_img_pause

            # -1. 阶段转换的事件监测建议放在循环最底下, 因为一旦阶段转换, 不希望再执行本阶段的任何代码
            for e in event:
                if e.type == MOUSEBUTTONDOWN and e.button == 1 and r.s1_rect_pause_pressed.collidepoint(e.pos):
                    stage = PAUSE
                    break

        elif stage == PAUSE:
            # 大部分资源的画法和PLAY阶段是一样的, 主要区别是动态资源不更新状态
            # 包括各精灵不动, 音乐暂停, 计时器暂停, 帧计数器frame和时计数器ticks也暂停

            # 1. 先画背景图
            screen.blit(r.s1_img_bg, r.s1_rect_bg)
            # 2. 再画左上角分数
            r.s1_text_score = r.s1_font_score.render("Score: {}".format(s1_score), True,WHITE)
            r.s1_rect_score = r.s1_text_score.get_rect()
            r.s1_rect_score.topleft = (10, 5)
            screen.blit(r.s1_text_score, r.s1_rect_score)
            # 3. 再画左下角炸弹数
            screen.blit(r.s1_img_bomb, r.s1_rect_bomb)
            r.s1_text_bombtxt = r.s1_font_bombtxt.render(" x {}".format(s1_num_bomb), True, WHITE)
            r.s1_rect_bombtxt = r.s1_text_bombtxt.get_rect()
            r.s1_rect_bombtxt.left = r.s1_rect_bomb.right + 10
            r.s1_rect_bombtxt.bottom = HEIGHT - 8
            screen.blit(r.s1_text_bombtxt, r.s1_rect_bombtxt)
            # 4. 画右下角生命数
            for i in range(s1_num_player):
                r.s1_rect_life.bottom = HEIGHT - 10
                r.s1_rect_life.right = WIDTH - 10 - i * r.s1_rect_life.width
                screen.blit(r.s1_img_life, r.s1_rect_life)


            # -3. PAUSE阶段的继续键要放在最底下画, 因为要先给其他要素套上蒙版, 再在上面画继续键
            screen_alpha.fill(WHITE_TRANSPARENT_HALF)
            screen_alpha.blit(s2_img_resume, r.s2_rect_resume if s2_img_resume == r.s2_img_resume else r.s2_rect_resume_pressed)
            screen.blit(screen_alpha, rect_screen_alpha)

            # -2. 同样, 继续键的图片切换不建议用瞬时事件去判断, 比如点了暂停后鼠标是在继续按钮上的, 但因为没移动, 不会变黑
            if r.s2_rect_resume.collidepoint(pg.mouse.get_pos()):
                s2_img_resume = r.s2_img_resume_pressed
            else:
                s2_img_resume = r.s2_img_resume

            # -1. 同样, 阶段转换的事件监测建议放在循环最底下, 因为一旦阶段转换, 不希望再执行本阶段的任何代码
            for e in event:
                if e.type == MOUSEBUTTONDOWN and e.button == 1 and r.s2_rect_resume_pressed.collidepoint(e.pos):
                    stage = PLAY
                    break

        elif stage == STOP:
            pass

        pg.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    try:
        main()
    except SystemExit as e:
        # 注意如果调sys.exit()的时候没传参数这里e的code值会是None
        print("调用sys.exit()退出")
    except:
        pg.quit()
        traceback.print_exc()
