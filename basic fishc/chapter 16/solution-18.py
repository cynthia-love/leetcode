# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    正式的玩球游戏
    搞清楚游戏的几个阶段
    1. 所有小球随机移动
    2. 摩擦, 个别小球变绿, 初始移动速度0
    3. 按键移动绿色小球
    4. 对准洞按空格后, 小球保持绿色且位置不再变化

"""

import sys
import random
import pygame as pg
from math import *
from pygame.locals import *

WHITE = (255, 255, 255)

TITLE = 'Play The Ball'
SIZE = WIDTH, HEIGHT = 1024, 681
SIZE_BALL = WIDTH_BALL, HEIGTH_BALL = 100, 100

FRAME = 109

BALL_NUM = 30
SPEED_MAX = 10

# 注意这里每个洞指定的是x, y的范围
HOLE = [
    (117, 119, 199, 201),
    (225, 227, 390, 392),
    (503, 505, 320, 322),
    (698, 700, 192, 194),
    (906, 908, 419, 421)
]


def isCover(item):
    for hole in HOLE:
        if hole[0] <= item.x <= hole[1] \
                and hole[2] <= item.y <= hole[3]:
            return True
    return False


def random_velocity():
    while True:
        arc = random.uniform(0, 2 * pi)
        speed = random.randint(1, SPEED_MAX)
        x = int(speed * cos(arc))
        y = int(speed * sin(arc))
        if x != 0 and y != 0:
            return [x, y]


class Ball(pg.sprite.Sprite):

    def __init__(self, pos, velocity, id):
        pg.sprite.Sprite.__init__(self)

        self.image_gray = pg.image.load("image/gray_ball.png")
        self.image_green = pg.image.load("image/green_ball.png")

        self.image = self.image_gray
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = pos

        self.velocity = velocity
        self.id = id  # id用于决定鼠标滑动后抽哪个小球变绿

        # 阶段1灰色自由移动, 阶段2绿色受控, 阶段3绿色位置不再变化
        # 这里每个精灵的state是不一样的, 所以需要写到类里而不能像solution-17那样写在外面
        # 为了控制state赋2或3的时候初始速度强制置为0, 赋1的时候随机速度, 可以将其设置为property
        # 还想赋初值怎么办, property和这里的变量名不用同一个就行了
        self._state = 1

    def _getx(self):
        return self.rect.x

    def _setx(self, value):
        self.rect.x = value

    x = property(_getx, _setx)

    def _gety(self):
        return self.rect.y

    def _sety(self, value):
        self.rect.y = value

    y = property(_gety, _sety)

    def _getpos(self):
        return self.rect.x, self.rect.y

    def _setpos(self, value):
        self.rect.x, self.rect.y = value

    pos = property(_getpos, _setpos)

    def _getwidth(self):
        return self.rect.width

    def _setwidth(self, value):
        self.rect.width = value

    width = property(_getwidth, _setwidth)

    def _getheight(self):
        return self.rect.height

    def _setheight(self, value):
        self.rect.height = value

    height = property(_getheight, _setheight)

    def _getradius(self):
        return int(self.rect.width / 2)

    radius = property(_getradius)

    def _getstate(self):
        return self._state

    def _setstate(self, value):
        self._state = value
        # 切换状态时图片切换可以放在这里做, 也可以放在update里
        # 函数里做, 建议这里做, 因为是一次性行为
        if self.state == 1:
            self.image = self.image_gray

        if self._state == 2 or self._state == 3:
            self.image = self.image_green
            self.velocity = [0, 0]

    state = property(_getstate, _setstate)

    def update(self, surface, back=False):

        if back:
            velocity = [-x for x in self.velocity]
        else:
            velocity = self.velocity

        # 这里注意, state为3的时候也是要移动的, 所以要置速度为(0, 0)
        self.rect = self.rect.move(velocity)

        rect = surface.get_rect()

        # 向左完全隐藏
        if self.rect.right < 0: self.rect.left = rect.width

        # 向右完全隐藏
        if self.rect.left > rect.width: self.rect.right = 0

        # 向上完全隐藏
        if self.rect.bottom < 0: self.rect.top = rect.height

        # 向下完全隐藏
        if self.rect.top > rect.height: self.rect.bottom = 0

    def check(self, times):
        if times < 3: return False  # 滑动次数过少, 不变
        if times % BALL_NUM == self.id and self.state == 1: return True

        return False


class Glass(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        pg.mouse.set_visible(False)

        self.image_glass = pg.image.load("image/glass.png").convert_alpha()
        self.rect_glass = self.image_glass.get_rect()

        self.image_mouse = pg.image.load("image/mouse.png").convert_alpha()
        self.rect_mouse = self.image_mouse.get_rect()

        self.image = pg.Surface((self.rect_glass.width, self.rect_glass.height))
        self.image.blit(self.image_glass, (0, 0))
        self.rect = self.image.get_rect()

    def _getx(self):
        return self.rect.x

    def _setx(self, value):
        self.rect.x = value

    x = property(_getx, _setx)

    def _gety(self):
        return self.rect.y

    def _sety(self, value):
        self.rect.y = value

    y = property(_gety, _sety)

    def _getwidth(self):
        return self.rect.width

    width = property(_getwidth)

    def _getheight(self):
        return self.rect.height

    height = property(_getheight)

    def _getpos(self):
        return self.rect.x, self.rect.y

    def _setpos(self, value):
        self.rect.x, self.rect.y = value

    pos = property(_getpos, _setpos)

    def update(self):
        center = pg.mouse.get_pos()
        self.rect_mouse.center = (center[0] - self.rect.x, center[1] - self.rect.y)
        if self.rect_mouse.x < 0: self.rect_mouse.x = 0
        if self.rect_mouse.right > self.rect.width: self.rect_mouse.right = self.rect.width
        if self.rect_mouse.y < 0: self.rect_mouse.y = 0
        if self.rect_mouse.bottom > self.rect.height: self.rect_mouse.bottom = self.rect.height

        pg.mouse.set_pos(self.rect_mouse.center[0] + self.rect.x,
                         self.rect_mouse.center[1] + self.rect.y)

        self.image.blit(self.image_glass, (0, 0))
        self.image.blit(self.image_mouse, self.rect_mouse)


pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode(SIZE)

image_bg = pg.image.load("image/background.png").convert_alpha()

# 状态1和2的存一个group, 因为相互之间会进行碰撞检测
group_ball_1 = pg.sprite.Group()

for i in range(BALL_NUM):
    pos = random.randint(0, WIDTH - WIDTH_BALL), random.randint(0, HEIGHT - HEIGTH_BALL)
    velocity = random_velocity()
    ball = Ball(pos, velocity, i)

    # 保证初始化的时候不会碰撞
    while pg.sprite.spritecollideany(ball, group_ball_1, pg.sprite.collide_circle):
        ball.pos = random.randint(0, WIDTH - WIDTH_BALL), random.randint(0,
                                                                         HEIGHT - HEIGTH_BALL)
    group_ball_1.add(ball)

# 进入状态3以后, 不再参与碰撞, 建议单独摘个group出来
group_ball_2 = pg.sprite.Group()
group_ball_3 = pg.sprite.Group()

glass = Glass()
glass.x = int((WIDTH - glass.width) / 2)
glass.y = HEIGHT - glass.height

# 添加背景音乐
pg.mixer_music.load("sound/bg_music.ogg")
pg.mixer_music.play(1)
pg.mixer_music.set_endevent(USEREVENT)

# 载入其他音效
sound_loser = pg.mixer.Sound("sound/loser.wav")
sound_winner = pg.mixer.Sound("sound/winner.wav")
sound_hole = pg.mixer.Sound("sound/hole.wav")
sound_laugh = pg.mixer.Sound("sound/laugh.wav")

pg.time.set_timer(USEREVENT + 1, 1000)  # 每隔1000ms发送一次USEREVENT+1事件
clock = pg.time.Clock()

times = 0

while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == USEREVENT:
            channel = pg.mixer.find_channel()
            channel.play(sound_loser)
            channel.queue(sound_laugh)

        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                sys.exit()
            # 键盘控制state为2的球有一个坑
            # 得控制最大速度, 不然相撞以后, 可能random不出来足够逃逸的速度
            # 另外, 由于state 2的速度有垂直和水平的, state 1的没有, 所以这里
            # 不能直接用SPEED_MAX为边界, 得比SPEED小
            if e.key == K_w:
                for item in group_ball_2:
                    item.velocity[1] -= 1
                    if sqrt(item.velocity[0]**2+item.velocity[1]**2) > SPEED_MAX*0.5:
                        item.velocity[1] += 1

            if e.key == K_s:
                for item in group_ball_2:
                    item.velocity[1] += 1
                    if sqrt(item.velocity[0]**2+item.velocity[1]**2) > SPEED_MAX*0.5:
                        item.velocity[1] -= 1

            if e.key == K_a:
                for item in group_ball_2:
                    item.velocity[0] -= 1
                    if sqrt(item.velocity[0]**2+item.velocity[1]**2) > SPEED_MAX*0.5:
                        item.velocity[0] += 1

            if e.key == K_d:
                for item in group_ball_2:
                    item.velocity[0] += 1
                    if sqrt(item.velocity[0]**2+item.velocity[1]**2) > SPEED_MAX*0.5:
                        item.velocity[0] -= 1

            if e.key == K_SPACE:
                for item in group_ball_2:
                    if isCover(item):

                        item.state = 3
                        group_ball_2.remove(item)
                        group_ball_3.add(item)

                        channel = pg.mixer.find_channel()
                        if len(group_ball_3) < BALL_NUM:
                            channel.play(sound_hole)
                        else:
                            # 每个通道只能排队一个声音
                            channel.play(sound_winner)
                            channel.queue(sound_laugh)

        if e.type == MOUSEMOTION:
            times += 1

        if e.type == USEREVENT + 1:
            for each in group_ball_1:
                if each.check(times):
                    each.state = 2
                    group_ball_1.remove(each)
                    group_ball_2.add(each)
                    times = 0

    screen.blit(image_bg, (0, 0))

    glass.update()
    screen.blit(glass.image, glass.rect)

    group_ball_3.draw(screen)

    group_ball_1.update(screen)
    group_ball_2.update(screen)

    group_ball_1.draw(screen)
    group_ball_2.draw(screen)

    print(group_ball_1, group_ball_2)
    # 怎么能写一个彻底完备的碰撞检测逻辑
    # 对于state为1的, 只要碰撞了, 直接反向
    for item in group_ball_1:
        group_ball_1.remove(item)
        if pg.sprite.spritecollideany(item, group_ball_1, pg.sprite.collide_circle) \
                or pg.sprite.spritecollideany(item, group_ball_2,
                                              pg.sprite.collide_circle):
            print("1hao", item.id, item.rect, item.velocity)
            item.velocity[0] = -item.velocity[0]
            item.velocity[1] = -item.velocity[1]
        group_ball_1.add(item)

    # 对于state为2的, 由于其碰撞后state要变成1, 后面就是速度一直取反了
    # 那么要保证当前碰撞的, 下一次移动后不能再碰撞, 不然就一直在那抖动了

    # 把当前2-1碰撞, 2-2碰撞全记住
    collides21 = pg.sprite.groupcollide(group_ball_2, group_ball_1,
                                        False, False, pg.sprite.collide_circle)
    collides22 = pg.sprite.groupcollide(group_ball_2, group_ball_2,
                                        False, False, pg.sprite.collide_circle)

    if collides21 or sum([len(item[1]) for item in collides22.items()]) > len(collides22):
        group_ball_1.update(screen)  # 先把所有状态为1的移动一次

        finded = False
        while not finded:

            # 再给状态2的随机一组速度后移动
            for item in group_ball_2:
                if item in collides21 or len(collides22[item]) > 1:
                    item.velocity = random_velocity()
                    print("重新给速度", item.id, item.rect, item.velocity)

            finded = True  # 先假设随机的速度可行

            # 然后把state为2的也移动了, 看一下下一帧是否满足要求
            group_ball_2.update(screen)

            # 拿到移动后的2-1, 2-2碰撞结果
            target21 = pg.sprite.groupcollide(group_ball_2, group_ball_1,
                                              False, False, pg.sprite.collide_circle)
            target22 = pg.sprite.groupcollide(group_ball_2, group_ball_2,
                                              False, False, pg.sprite.collide_circle)

            print("21-old")
            for item in collides21.keys():
                for s in collides21[item]:
                    print(item.id, s.id)

            print("21-new")
            for item in target21.keys():
                for s in target21[item]:
                    print(item.id, s.id)

            for item in collides21.keys():
                for s in collides21[item]:
                    if item in target21 and s in target21[item]:
                        print(item.id, s.id)
                        print(item.rect, s.rect)
                        finded = False

            for item in collides22.keys():
                if len(collides22[item]) == 1:
                    continue
                for s in collides22[item]:
                    if item == s: continue
                    if item in target22 and s in target22[item]:
                        print(item.id, s.id)
                        finded = False

            # 无论找到没找到, 都要先把位置回退了
            group_ball_2.update(screen, True)

        # 先把state为1的位置回退了
        group_ball_1.update(screen, True)

        # 再把有碰撞的状态2的state改为1后换group
        for item in collides21:
            item.state = 1
            group_ball_2.remove(item)
            group_ball_1.add(item)

        for item in collides22:
            if len(collides22[item]) == 1:
                continue
            item.state = 1
            group_ball_2.remove(item)
            group_ball_1.add(item)

    if len(group_ball_3) == BALL_NUM:
        img = pg.image.load("image/win.png")
        rect = img.get_rect()
        x = int((WIDTH-rect.width)/2)
        y = int((HEIGHT-rect.height)/2)
        screen.blit(img, (x, y))

    pg.display.flip()

    clock.tick(FRAME)
