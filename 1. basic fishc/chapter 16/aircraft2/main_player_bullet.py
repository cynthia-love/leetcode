# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在main_player的基础上, 继续添加bullet逻辑
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
    # 先把各阶段简单的静态背景图, 分数, 暂停键什么的的逻辑写了, 把PLAY, PAUSE, STOP串起来
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

        # 音乐
        self.s1_sound_supply = self.s1_sound_getbullet = self.s1_sound_getbomb = None
        self.s1_sound_usebomb = self.s1_sound_upgrade = None

        # 动态精灵
        self.s1_player = self.s1_list_bullet1 = self.s1_list_bullet2 = None
        self.s1_group_enemy_all = self.s1_group_enemy_small = self.s1_group_enemy_middle = self.s1_group_enemy_big = None
        self.s1_supply_bullet = self.s1_supply_bomb = None


        """PAUSE阶段"""
        # 右上角继续键
        self.s2_img_resume = self.s2_rect_resume = None
        self.s2_img_resume_pressed = self.s2_rect_resume_pressed = None
        """STOP阶段"""
        # 左上角分数
        self.s3_font_score_best = self.s3_text_score_best = self.s3_rect_score_best = None
        # 中间Your Score
        self.s3_font_score_your = self.s3_text_score_your = self.s3_rect_score_your = None
        # 中间本次分数
        self.s3_font_score_this = self.s3_text_score_this = self.s3_rect_score_this = None
        # 下方重新开始图标
        self.s3_img_retry = self.s3_rect_retry = None
        # 下放结束游戏图标
        self.s3_img_stop = self.s3_rect_stop = None

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
        self.s1_img_pause_pressed = pg.image.load("image/pause_pressed.png").convert_alpha()
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

        # 音乐
        pg.mixer_music.load("sound/game_music.ogg")
        pg.mixer_music.set_volume(0.2)

        self.s1_sound_supply = pg.mixer.Sound("sound/supply.wav")
        self.s1_sound_getbullet = pg.mixer.Sound("sound/get_bullet.wav")
        self.s1_sound_getbomb = pg.mixer.Sound("sound/get_bomb.wav")
        self.s1_sound_usebomb = pg.mixer.Sound("sound/use_bomb.wav")
        self.s1_sound_upgrade = pg.mixer.Sound("sound/upgrade.wav")

        # 精灵
        # 玩家
        self.s1_player = Player()
        # WIDTH, HEIGHT, SPEED_PLAYER, FPS_ANIMATION没必要通过主函数传参吧, 本来就是为了简洁
        # 提取了全局变量, 再传参岂不是又变复杂了
        # 子弹
        self.s1_list_bullet1 = list()
        for i in range(NUM_BULLET1):
            self.s1_list_bullet1.append(Bullet(self.s1_player, "middle"))
        self.s1_list_bullet2 = list()
        for i in range(NUM_BULLET2):
            self.s1_list_bullet2.append(Bullet(self.s1_player, "left"))
            self.s1_list_bullet2.append(Bullet(self.s1_player, "right"))
        # 敌机
        self.s1_group_enemy_all = pg.sprite.Group()
        self.s1_group_enemy_small = pg.sprite.Group()
        self.s1_group_enemy_middle = pg.sprite.Group()
        self.s1_group_enemy_big = pg.sprite.Group()

        self.add_enemy_small(NUM_ENEMY_SMALL)
        self.add_enemy_middle(NUM_ENEMY_MIDDLE)
        self.add_enemy_big(NUM_ENEMY_BIG)

        # 补给
        self.s1_supply_bullet = Supply("bullet")
        self.s1_supply_bomb = Supply("bomb")

        """PAUSE阶段"""
        self.s2_img_resume = pg.image.load("image/resume_nor.png").convert_alpha()
        self.s2_rect_resume = self.s1_rect_pause  # 位置一样, 可以直接借用
        self.s2_img_resume_pressed = pg.image.load("image/resume_pressed.png").convert_alpha()
        self.s2_rect_resume_pressed = self.s1_rect_pause_pressed

        """STOP阶段"""
        # 最佳分数可能是历史最高分, 也可能是本次的, 所以这里暂时不render text
        self.s3_font_score_best = pg.font.Font("font/font.TTF", 36)
        # Your Score文本可以直接计算了
        self.s3_font_score_your = pg.font.Font("font/font.TTF", 48)
        self.s3_text_score_your = self.s3_font_score_your.render("Your Score", True, WHITE)
        self.s3_rect_score_your = self.s3_text_score_your.get_rect()
        self.s3_rect_score_your.left = int((WIDTH-self.s3_rect_score_your.width)/2)
        self.s3_rect_score_your.top = HEIGHT // 3  # 注意这个技巧, 不用再用int强转
        # 本次分数text也得后面进到STOP阶段的时候实时生成
        self.s3_font_score_this = pg.font.Font("font/font.TTF", 48)
        # 重新开始图标, 注意x值可以直接初始化, 但y值需要后面根据s3_rect_score_this算
        self.s3_img_retry = pg.image.load("image/again.png").convert_alpha()
        self.s3_rect_retry = self.s3_img_retry.get_rect()
        self.s3_rect_retry.left = (WIDTH-self.s3_rect_retry.width) // 2
        # 结束游戏图标, 同样x值可以初始化, y需要后面算
        self.s3_img_stop = pg.image.load("image/gameover.png").convert_alpha()
        self.s3_rect_stop = self.s3_img_stop.get_rect()
        self.s3_rect_stop.left = (WIDTH-self.s3_rect_stop.width) // 2

    def add_enemy_small(self, num):
        for i in range(num):
            self.s1_group_enemy_all.add(EnemySmall())
            self.s1_group_enemy_small.add(EnemySmall())

    def add_enemy_middle(self, num):
        for i in range(num):
            self.s1_group_enemy_all.add(EnemyMiddle())
            self.s1_group_enemy_middle.add(EnemyMiddle())

    def add_enemy_big(self, num):
        for i in range(num):
            self.s1_group_enemy_all.add(EnemyBig())
            self.s1_group_enemy_big.add(EnemyBig())

    # 虽然定义这么多函数有点多余, 但用的时候方便啊
    def inc_speed_enemy_small(self):
        for each in self.s1_group_enemy_small:
            each.speed += SPEED_INC_ENEMY

    def inc_speed_enemy_middle(self):
        for each in self.s1_group_enemy_middle:
            each.speed += SPEED_INC_ENEMY

    def inc_speed_enemy_big(self):
        for each in self.s1_group_enemy_big:
            each.speed += SPEED_INC_ENEMY

def main():
    pg.init()
    pg.display.set_caption(TITLE)
    screen = pg.display.set_mode(SIZE)
    rect_screen = screen.get_rect()  # 声明了备用
    screen_alpha = screen.convert_alpha()
    rect_screen_alpha = screen_alpha.get_rect()  # 声明了备用

    r = Resource()
    r.init()

    # 各个阶段都要用到的变量, 变量变量, 就是会动态变的量
    stage = PLAY
    clock = pg.time.Clock()

    """PLAY阶段"""
    s1_score = 1000
    s1_level = 1  # 声明level是为了保证分数达标后游戏难度只升级一次
    s1_img_pause = r.s1_img_pause  # pause这里rect没必要再声明个变量了, 因为位置一样, 实在不行用三元表达式也行, 总比多个变量强
    s1_num_bomb = NUM_BOMB
    s1_num_player = NUM_PLAYER

    s1_list_bullet = r.s1_list_bullet1  # 初始应该是普通子弹, 之所以设置这个变量, 是为了后面判断碰撞什么的代码更简洁
    s1_frame = 0  # PLAY阶段运行的帧索引, 记录当前是第几次主循环, 用于控制子弹发射频率
    s1_tickb = 0  # 记录基准时间, 给双倍子弹计时用的, 一定要想清楚什么场景要用帧索引控制, 什么场景用tick控制
    s1_leftb = 0  # 记录剩余时长, 给双倍子弹计时用的, 单位ms
    # 这里记录双倍子弹时间为什么用两个变量, 设想一种情况, 吃到双倍子弹, 用了5秒, 暂停, 再回来, 应该还能继续用13秒
    # 用set_timer是不行的, 暂停的时间不能记双倍时间

    # 声明完变量, 启动PLAY阶段需要的音乐, 计时器等
    pg.mixer_music.play(-1)
    pg.time.set_timer(EVENT_SUPPLY_RELEASE, TIME_SUPPLY)

    """PAUSE阶段"""
    s2_img_resume = r.s2_img_resume

    """STOP阶段"""
    try:
        with open(getpath("data/record.txt"), "r") as f:
            s3_score_best = int(f.read())
    except:
        s3_score_best = 0

    while True:

        event = pg.event.get()
        for e in event:
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
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

            """动态精灵渲染区域"""
            # (1)玩家
            screen.blit(r.s1_player.image, r.s1_player.rect)
            # (2)子弹
            for each in s1_list_bullet:
                if each.active:
                    screen.blit(each.image, each.rect)
            # (3)补给
            # (4)敌机

            """***************"""

            """动态精灵更新区域"""
            # (1)玩家
            r.s1_player.update()
            # 除了stage转换, 其他事件遍历没必要都放底下, 还乱
            for e in event:
                if e.type == EVENT_PLAYER_INVINCIBLE:
                    r.s1_player.state = STATE_PLAYER_FLY
                    pg.time.set_timer(EVENT_PLAYER_INVINCIBLE, 0)
            # 响应键盘有两种, 一种是通过KEYDOWN和KEYUP事件, 另一种是用key模块的get_pressed()
            # 第一种适合偶尔触发的事件, 本例需要长时间按键盘, 用第二种方式
            # 由于这个例子不像playtheball, 长按速度会递增, 不需要pygame.key.set_repeat(x, x)
            keys = pg.key.get_pressed()
            if keys[K_w] or keys[K_UP]: r.s1_player.move("n")
            if keys[K_s] or keys[K_DOWN]: r.s1_player.move("s")
            if keys[K_a] or keys[K_LEFT]: r.s1_player.move("w")
            if keys[K_d] or keys[K_RIGHT]: r.s1_player.move("e")

            # (2)子弹, 按双倍判断, 发射, 移动的顺序来
            if s1_leftb:
                tick = pg.time.get_ticks()
                if tick - s1_tickb >= s1_leftb:
                    s1_leftb = 0
                    s1_list_bullet = r.s1_list_bullet1
                    for each in s1_list_bullet:
                        each.active = False
                else:
                    s1_leftb = s1_leftb-(tick-s1_tickb)
                    s1_tickb = tick

            if s1_frame % FRAME_BULLET == 0:
                if not s1_leftb:
                    bullet = s1_list_bullet.pop(0)
                    bullet.fire()
                    s1_list_bullet.append(bullet)
                else:
                    bullet = s1_list_bullet.pop(0)
                    bullet.fire()
                    s1_list_bullet.append(bullet)
                    bullet = s1_list_bullet.pop(0)
                    bullet.fire()
                    s1_list_bullet.append(bullet)
            for each in s1_list_bullet:
                if each.active:
                    each.move()
            # (3)补给
            # (4)敌机

            """***************"""

            # -2. 暂停键的图片切换不建议用瞬时事件去判断, 比如点了暂停后鼠标是在继续按钮上的, 但因为没移动, 不会变黑
            if r.s1_rect_pause.collidepoint(pg.mouse.get_pos()):
                s1_img_pause = r.s1_img_pause_pressed
            else:
                s1_img_pause = r.s1_img_pause

            # -1. 阶段转换的事件监测建议放在循环最底下, 因为一旦阶段转换, 不希望再执行本阶段的任何代码
            for e in event:
                if e.type == MOUSEBUTTONDOWN and e.button == 1 and r.s1_rect_pause_pressed.collidepoint(e.pos):
                    # 先收尾PLAY阶段的东西
                    pg.mixer_music.pause()
                    pg.time.set_timer(EVENT_SUPPLY_RELEASE, 0)  # 暂停计数器是为了防止暂停无限获取补给
                    # 注意leftb和tickb保持实时更新的话, 这里是不用记得, 回来的时候更新tickb就行
                    # 再初始化PAUSE阶段无法在init里初始化的东西, 这里没有
                    stage = PAUSE
                    break
                """先模拟跳到STOP阶段"""
                if e.type == KEYDOWN and e.key == K_SPACE:
                    # 先收尾PLAY阶段的东西
                    pg.mixer_music.stop()
                    pg.time.set_timer(EVENT_SUPPLY_RELEASE, 0)

                    # 再初始化STOP阶段需要的无法在init里初始化东西
                    if s1_score > s3_score_best:
                        s3_score_best = s1_score
                        with open(getpath("data/record.txt"), "w") as f:
                            f.write(str(s3_score_best))
                    r.s3_text_score_best = r.s3_font_score_best.render("Best: {}".format(s3_score_best), True, WHITE)
                    r.s3_rect_score_best = r.s3_text_score_best.get_rect()
                    r.s3_rect_score_best.topleft = (20, 20)

                    r.s3_text_score_this = r.s3_font_score_this.render("{}".format(s1_score), True, WHITE)
                    r.s3_rect_score_this = r.s3_text_score_this.get_rect()
                    r.s3_rect_score_this.left = (WIDTH - r.s3_rect_score_this.width) // 2
                    r.s3_rect_score_this.top = r.s3_rect_score_your.bottom+10
                    # 重新开始和结束游戏初始化的时候就能拿到rect且能算x, 所以这里指定y就行了
                    r.s3_rect_retry.top = r.s3_rect_score_this.bottom + 20
                    r.s3_rect_stop.top = r.s3_rect_retry.bottom + 10

                    stage = STOP
                    break

                if e.type == EVENT_PLAYER_DESTROYED:
                    if s1_num_player > 1:
                        s1_num_player -= 1
                        r.s1_player.reset()
                        pg.time.set_timer(EVENT_PLAYER_INVINCIBLE, TIME_INVINCIBLE)
                    else:
                        stage = STOP
                        break
            # 更新帧计数
            s1_frame += 1

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


            """动态精灵渲染区域"""
            # (1)玩家
            screen.blit(r.s1_player.image, r.s1_player.rect)

            # (2)子弹
            for each in s1_list_bullet:
                if each.active:
                    screen.blit(each.image, each.rect)
            # (3)补给
            # (4)敌机

            """***************"""
            # PAUSE阶段没有精灵更新和控制区域


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
                    # PAUSE阶段收尾, 无
                    # PLAY阶段部分功能继续
                    pg.mixer_music.unpause()
                    pg.time.set_timer(EVENT_SUPPLY_RELEASE, TIME_SUPPLY)
                    if s1_leftb: s1_tickb = pg.time.get_ticks()

                    stage = PLAY
                    break

        elif stage == STOP:
            screen.blit(r.s1_img_bg, (0, 0))
            screen.blit(r.s3_text_score_best, r.s3_rect_score_best)
            screen.blit(r.s3_text_score_your, r.s3_rect_score_your)
            screen.blit(r.s3_text_score_this, r.s3_rect_score_this)
            screen.blit(r.s3_img_retry, r.s3_rect_retry)
            screen.blit(r.s3_img_stop, r.s3_rect_stop)

            # 阶段转换事件监测还是放下面
            for e in event:
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if r.s3_rect_retry.collidepoint(e.pos):
                        # 重新开始直接重新main()就行, 不用在去clear一堆变量, 重新赋值什么的
                        main()
                        break
                    if r.s3_rect_stop.collidepoint(e.pos):
                        sys.exit()

        pg.display.flip()

        clock.tick(FPS)
        # 还有一个函数是clock.tick_busy_loop(FPS), 更精确但更占用资源
        # 这里clock会根据循环主体代码运行的时间和目标FPS去综合计算本次要延时多少ms
        # 由于计算机肯定存在误差, 比如设置FPS=10, 不代表每次运行到同一位置一定是间隔100ms
        # 有可能是100-201-300-402-500这样
        # 那么对于周期性动画或者定期发射子弹这样的场景来说, 前者对于精确度要求不高
        # 且精灵类里面容易获取tick很难获取帧索引号, 所以动画更新可以直接用pg.time.get_ticks()
        # 比如要求间隔100ms才更新一次, 那么201会更新, 300则不会更新, 然后402会更新
        # 而子弹发射一般对精确度要求更高一些, 不能说201发射了, 300就不发射了, 接着402才发射
        # 那么对于子弹频率的控制建议用帧索引, 单独设置一个帧计数器, 每隔几帧发射一次
        # 这两种控制频率的方式一定要好好理解

if __name__ == '__main__':
    try:
        main()
    except SystemExit as e:
        # 注意如果调sys.exit()的时候没传参数这里e的code值会是None
        print("调用sys.exit()退出")
    except:
        pg.quit()  # 这里不能用sys.exit(), 不然后面就不会打印了
        traceback.print_exc()