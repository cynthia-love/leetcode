# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    正式的玩球游戏
    搞清楚游戏的几个阶段
    LAUNCH, START, PLAY, PAUSE, WIN, LOSE = 0, 1, 2, 3, 4, 5

    1. 初始START, 一个暂停按钮
    2. 点击后进入PLAY, 游戏开始, 所有灰色小球随机移动, 摩擦变绿, 移动, 进洞
    3. 按P键暂停, 进入PAUSE
    4. 再按P键, 回到PLAY阶段
    5. 音乐结束前完成, 进入WIN阶段
    6. 音乐结束未完成, 进入LOSE阶段
"""
import sys
import random
import traceback
import pygame as pg
from math import *
from pygame.locals import *

"""
    第一部分, 常量设置, 像是图片大小什么的, 有些外层也要用到,
    建议直接设置了, 而不要等图片载入后再去获取, 不方便代码编写
"""
# 通用常量
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
WHITE_TRANS = (255, 255, 255, 150)

# SURFACE相关的
TITLE = 'Play The Ball'
SIZE = WIDTH, HEIGHT = 1024, 681
FRAME = 100

SIZE_BALL = WIDTH_BALL, HEIGHT_BALL = 100, 100
SIZE_GLASS = WIDTH_GLASS, HEIGHT_GLASS = 368, 218

# 其他游戏相关的数据
LAUNCH, START, PLAY, PAUSE, WIN, LOSE = 0, 1, 2, 3, 4, 5

BALL_NUM = 5
SPEED_MAX = 10
HOLE = (
    (117, 119, 199, 201),
    (225, 227, 390, 392),
    (503, 505, 320, 322),
    (698, 700, 192, 194),
    (906, 908, 419, 421)
)
# 定义两个个性化事件, 一个是每个一段时间发送的事件, 一个是音乐结束事件
TIMER = USEREVENT+1
GAMEOVER = USEREVENT+2

"""
    第二部分, 各种函数方法, 类
"""
class Ball(pg.sprite.Sprite):

    def __init__(self, pos, velocity, id):
        pg.sprite.Sprite.__init__(self)
        # 注意, 后续更新可能用到的素材都在init里初始化了
        # 不然可能会因为循环生成对象过多导致内存溢出
        self.image_gray = pg.image.load("image/gray_ball.png").convert_alpha()
        self.image_green = pg.image.load("image/green_ball.png").convert_alpha()

        self.image = self.image_gray
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = pos

        self.velocity = velocity

        self.id = id  # id用于决定鼠标滑动后哪个小球变绿

        # 要不要再设置个state变量, 存储球的3个状态, 黑-绿-静止, 都行
        # 建议外部去设置三个group, 因为涉及统一update什么的, 没必要遍历去判断每个的state

    # 根据当前位置和速度去更新下一帧位置
    # 注意update函数只有批量更新时叫这个名才有意义, 如果一个个更新, 叫move什么的更好理解
    # surface用于限制小球位置范围
    def update(self, surface, back=False):

        velocity = self.velocity
        if back: velocity = [-x for x in self.velocity]

        self.rect = self.rect.move(velocity)

        rect = surface.get_rect()

        # 如果完全移出屏幕, 另一个方向再回来
        if self.rect.right < 0: self.rect.left = rect.width
        if self.rect.left > rect.width: self.rect.right = 0
        if self.rect.bottom < 0: self.rect.top = rect.height
        if self.rect.top > rect.height: self.rect.bottom = 0

    # 传入鼠标滑动次数, 根据id判断当前精灵是否要变绿
    def check(self, times):
        if times < 5: return False  # 滑动次数过少, 不处理
        if times % BALL_NUM == self.id: return True
        else: return False

    def _getx(self): return self.rect.x
    def _setx(self, value): self.rect.x = value
    x = property(_getx, _setx)

    def _gety(self): return self.rect.y
    def _sety(self, value): self.rect.y = value
    y = property(_gety, _sety)

    def _getpos(self): return self.rect.x, self.rect.y
    def _setpos(self, value): self.rect.x, self.rect.y = value
    pos = property(_getpos, _setpos)

    def _getwidth(self): return self.rect.width
    width = property(_getwidth)

    def _getheight(self): return self.rect.height
    height = property(_getheight)

    def _getradius(self): return int(self.rect.width / 2)
    radius = property(_getradius)

class Glass(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image_glass = pg.image.load("image/glass.png").convert_alpha()
        self.rect_glass = self.image_glass.get_rect()

        self.image_mouse = pg.image.load("image/mouse.png").convert_alpha()
        self.rect_mouse = self.image_mouse.get_rect()

        # 这里想想为什么要单独生成一个Surface, 因为每次要把鼠标画到glass上生成一个新图
        # 当然, 不是必须这么写, 也可以把外部surface传进来, 直接在上面画glass和mouse
        self.image = pg.Surface((self.rect_glass.width, self.rect_glass.height))
        self.image.blit(self.image_glass, (0, 0))
        self.rect = self.image.get_rect()

        # init里也可以把image_mouse画上, 初始位置左上角, 并调pg.mouse.set_pos
        # 不过感觉意义不大, 因为START状态鼠标肯定会移动, 点开始后鼠标图标会瞬移一下

    def update_mouse(self):
        # mouse除了用与glass的相对位置, 还可以在property里建立glass与mouse的位置映射关系
        # mouse也用相对于屏幕的绝对位置, 这样的话就不用再声明一个Surface了
        # 但是这样也有问题, main函数里得显式去画鼠标, 而不能实现调一次blit把glass和鼠标都画上
        # group更是不能用, 因为其draw只会画self.image

        # 注意, 获取到的鼠标位置是绝对位置, 要转成相对于glass的相对位置
        pos = pg.mouse.get_pos()
        self.rect_mouse.center = pos[0]-self.rect.x, pos[1]-self.rect.y
        # 把鼠标位置置为鼠标图片中心位置后, 要判断是否在glass边界外了
        # 这里的x和y也可以用left, top代替, 一个意思
        self.rect_mouse.x = max(0, self.rect_mouse.x)
        self.rect_mouse.right = min(self.rect.width, self.rect_mouse.right)
        self.rect_mouse.y = max(0, self.rect_mouse.y)
        self.rect_mouse.bottom = min(self.rect.height, self.rect_mouse.bottom)

        # 重置了鼠标图片位置后, 在对应位置画图, 并强制重置鼠标位置
        self.image.blit(self.image_glass, (0, 0))
        self.image.blit(self.image_mouse, self.rect_mouse)

        pg.mouse.set_pos(self.rect_mouse.center[0]+self.rect.x,
                         self.rect_mouse.center[1]+self.rect.y)

    def _getx(self): return self.rect.x
    def _setx(self, value): self.rect.x = value
    x = property(_getx, _setx)

    def _gety(self): return self.rect.y
    def _sety(self, value): self.rect.y = value
    y = property(_gety, _sety)

    def _getpos(self): return self.rect.x, self.rect.y
    def _setpos(self, value): self.rect.x, self.rect.y = value
    pos = property(_getpos, _setpos)

    def _getwidth(self): return self.rect.width
    width = property(_getwidth)

    def _getheight(self): return self.rect.height
    height = property(_getheight)

# 五个洞, 有一个满足左上角点在范围内, 就认为覆盖
def isCover(point):
    for h in HOLE:
        if h[0] <= point.x <= h[1] \
                and h[2] <= point.y <= h[3]:
            return True
    return False

# 随机速度函数, 直到随机出来x方向和y方向都不为0的速度
def randomVelocity():
    while True:
        arc = random.uniform(0, 2*pi)
        speed = random.randint(1, SPEED_MAX)
        x = int(speed * cos(arc))
        y = int(speed * sin(arc))
        if x != 0 and y != 0:
            return [x, y]

# 判断点是否在rect框定的圆内; 矩形判断方法pygame自带
def collidepoint(rect, point):

    distance = sqrt(pow(rect.center[0]-point[0], 2) +
                         pow(rect.center[1]-point[1], 2))
    return distance <= rect.width/2

def velocity1step(velocity, direction):
    n2v = {
        "n": [0, -1],
        "s": [0, 1],
        "w": [-1, 0],
        "e": [1, 0]
    }
    velocity_new = [velocity[0]+n2v[direction][0], velocity[1]+n2v[direction][1]]
    if sqrt(velocity_new[0]**2+velocity_new[1]**2) > SPEED_MAX*0.5:
        return velocity
    else:
        return velocity_new
"""
    第三部分, 初始化, 以及各stage的初始化
"""

def main():
    # 先初始化全局部分, 即各阶段都会用到的
    pg.init()
    pg.display.set_caption(TITLE)
    screen = pg.display.set_mode(SIZE)
    screen_alpha = screen.convert_alpha()

    clock = pg.time.Clock()

    # 开启全局长按处理逻辑, 长按某一个按键, 100ms后发出第一个KEYDOWN
    # 之后每间隔100ms发出一次KEYDOWN
    # 不带参数调用表示取消长按逻辑
    pg.key.set_repeat(100, 100)

    # 然后是不同阶段可能用到的素材, 先处理不会变的
    image_bg = pg.image.load("image/background.png").convert_alpha()

    image_pause = pg.image.load("image/pause.png").convert_alpha()
    rect_pause = image_pause.get_rect()

    image_unpause = pg.image.load("image/unpause.png").convert_alpha()
    rect_unpause = image_unpause.get_rect()

    glass = Glass()

    font = pg.font.Font(None, 80)
    text_lose = font.render("You lose! Retry?", True, (0, 0, 0))
    text_rect = text_lose.get_rect()

    image_win = pg.image.load("image/win.png").convert_alpha()
    rect_win = image_win.get_rect()

    pg.mixer_music.load("sound/bg_music.ogg")
    pg.mixer_music.set_endevent(GAMEOVER)

    sound_loser = pg.mixer.Sound("sound/loser.wav")
    sound_winner = pg.mixer.Sound("sound/winner.wav")
    sound_hole = pg.mixer.Sound("sound/hole.wav")
    sound_laugh = pg.mixer.Sound("sound/laugh.wav")

    # 再处理会变的东西
    # 三种状态的小球用三个group存, 即外部控制状态, 不用精灵自己去维护一个state
    group_ball_1 = pg.sprite.Group()
    group_ball_2 = pg.sprite.Group()
    group_ball_3 = pg.sprite.Group()

    # 初始化
    def initialize(stage_to, stage_from):
        # START阶段不可能有其它来源, 不用判断stage_from
        if stage_to == START:

            # 玻璃板位置计算一次就行
            glass.x = int((WIDTH - WIDTH_GLASS) / 2)
            glass.y = HEIGHT - HEIGHT_GLASS

            # 计算暂停键位置, 后面还会用到暂停键
            rect_pause.x = int((WIDTH-rect_pause.width)/2)
            rect_pause.y = int((HEIGHT-rect_pause.height)/2)

            # START阶段就要把group_ball_1的小球先画了, 只不过不动
            for i in range(BALL_NUM):
                pos = random.randint(0, WIDTH - WIDTH_BALL), \
                      random.randint(0, HEIGHT - HEIGHT_BALL)
                velocity = randomVelocity()
                ball = Ball(pos, velocity, i)

                # 保证初始化的时候不会碰撞
                while pg.sprite.spritecollideany(ball, group_ball_1, pg.sprite.collide_circle):
                    ball.pos = random.randint(0, WIDTH - WIDTH_BALL), \
                               random.randint(0, HEIGHT - HEIGHT_BALL)

                group_ball_1.add(ball)

        # 除非前面有return什么的, 否则不要直接用if代替elif
        elif stage_to == PLAY:
            nonlocal times
            # PLAY状态可能从START, PAUSE, WIN, LOSE过来

            # 隐藏鼠标, 从哪来的都要做这个操作
            pg.mouse.set_visible(False)

            # 计算右上角暂停键位置
            rect_unpause.x = WIDTH-rect_pause.width-50
            rect_unpause.y = 30

            # 从START, WIN, LOSE来的, 则要把PLAY状态清空
            # START例外一点, 小球不清
            if stage_from in [START, WIN, LOSE]:
                # 重新播放音乐
                pg.mixer_music.stop()
                pg.mixer_music.play()

                # 计时器重置
                pg.time.set_timer(TIMER, 0)  # 参数2设置0表示取消
                pg.time.set_timer(TIMER, 1000)
                # 鼠标摩擦次数重置
                times = 0
            elif stage_from == PAUSE:
                pg.mixer_music.unpause()

            # 如果是从WIN, LOSE来的, 还要重置小球
            # 从START来的考虑动画连续性, 就不重置了
            if stage_from in [WIN, LOSE]:
                # 初始化状态1的球
                group_ball_1.empty()
                group_ball_2.empty()
                group_ball_3.empty()

                for i in range(BALL_NUM):
                    pos = random.randint(0, WIDTH - WIDTH_BALL), \
                          random.randint(0, HEIGHT - HEIGHT_BALL)
                    velocity = randomVelocity()
                    ball = Ball(pos, velocity, i)

                    # 保证初始化的时候不会碰撞
                    while pg.sprite.spritecollideany(ball, group_ball_1,
                                                     pg.sprite.collide_circle):
                        ball.pos = random.randint(0, WIDTH - WIDTH_BALL), \
                                   random.randint(0, HEIGHT - HEIGHT_BALL)

                    group_ball_1.add(ball)

        # 其他几个状态来源都是单一的PLAY
        elif stage_to == PAUSE:

            # 显示鼠标
            pg.mouse.set_visible(True)
            # 计算重启键位置
            rect_pause.x = WIDTH-rect_pause.width-50
            rect_pause.y = 30

            # 音乐暂停
            pg.mixer_music.pause()

        elif stage_to == LOSE:

            pg.mouse.set_visible(True)

            channel = pg.mixer.find_channel()
            channel.play(sound_loser)
            channel.queue(sound_laugh)

            text_rect.x = int((WIDTH-text_rect.width)/2)
            text_rect.y = int((HEIGHT-text_rect.height)/2)

        elif stage_to == WIN:

            pg.mouse.set_visible(True)

            pg.mixer_music.stop()

            channel = pg.mixer.find_channel()
            channel.play(sound_winner)
            channel.queue(sound_laugh)

            rect_win.x = int((WIDTH-rect_win.width)/2)
            rect_win.y = int((HEIGHT-rect_win.height)/2)


    # PLAY阶段用到碰撞后的速度重置函数
    # 初始状态所有小球不碰撞, 速度随机
    # 然后update一次, 小球移动, 可能达到碰撞状态,
    # 如果碰了, 那么小黑球直接反向, 一定可以达到上一次不碰撞状态
    # 小绿球比较特殊, 小黑球变绿后速度变为0, 根据键盘按的次数速度跟着变化
    # 如果碰了, 其变黑并得到一个初始速度, 这个速度要保证下一次不能碰, 因为碰了就走
    # 小黑球逻辑, 反向再反向就死那抖动了
    def checkCollide(group_ball_1, group_ball_2):
        # 小黑球简单, 碰了就调头
        for each in group_ball_1:
            group_ball_1.remove(each)
            if pg.sprite.spritecollideany(each, group_ball_1, pg.sprite.collide_circle)\
                or pg.sprite.spritecollideany(each, group_ball_2, pg.sprite.collide_circle):
                each.velocity[0] = -each.velocity[0]
                each.velocity[1] = -each.velocity[1]
            group_ball_1.add(each)
        # 小绿球特殊, 碰的之后要保证下一次移动后不和原来那个碰
        # 把碰的记住了{小绿球:[碰1, 碰2]...}
        collides21 = pg.sprite.groupcollide(group_ball_2, group_ball_1,
                                            False, False, pg.sprite.collide_circle)
        collides22 = pg.sprite.groupcollide(group_ball_2, group_ball_2,
                                            False, False, pg.sprite.collide_circle)

        # 把collides22里自己和自己碰的去掉
        # 这里的list不加, 不让循环过程中删除元素
        for each in list(collides22.keys()):
            if len(collides22[each]) == 1:
                collides22.pop(each)

        # 如果有小绿碰撞, 那么要给其随机速度
        if collides21 or collides22:
            # 注意小黑球的移动要放在循环外面
            group_ball_1.update(screen)
            finded = False
            while not finded:
                # 给这批碰撞的绿球赋新速度
                # 注意, 绿球碰了的才赋新速度
                for each in group_ball_2:
                    if each in collides21 or each in collides22:
                        each.velocity = randomVelocity()

                # 反证法, 假设随机的速度可行
                finded = True

                group_ball_2.update(screen)

                # 拿到移动后的2-1, 2-2碰撞结果
                target21 = pg.sprite.groupcollide(group_ball_2, group_ball_1,
                                                  False, False, pg.sprite.collide_circle)
                target22 = pg.sprite.groupcollide(group_ball_2, group_ball_2,
                                                  False, False, pg.sprite.collide_circle)
                for each in list(target22.keys()):
                    if len(target22[each]) == 1:
                        target22.pop(each)

                # 看老的碰撞关系更新后是否还碰撞
                for each in collides21:
                    for item in collides21[each]:
                        if each in target21 and item in target21[each]:
                            finded = False

                for each in collides22:
                    for item in collides22[each]:
                        if each in target22 and item in target22[each]:
                            finded = False

                # 不管找没找到合适的速度, 先把小绿球位置回退了
                group_ball_2.update(screen, True)

            # 循环退出后, 说明碰撞的小绿球都找到了合适的速度, 此时回退小黑球
            group_ball_1.update(screen, True)

            # 然后把碰了的小绿球变黑, 并移到group_1里
            for each in group_ball_2:
                if each in collides21 or each in collides22:
                    each.image = each.image_gray
                    group_ball_2.remove(each)
                    group_ball_1.add(each)

    stage = START
    initialize(stage, LAUNCH)
    times = 0

    while True:
        # 循环里面同样分公共代码和各阶段执行的代码
        # 公共的放外面就行
        event = pg.event.get()
        for e in event:
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()

        if stage == START:

            # 先在screen上画背景图
            screen.blit(image_bg, (0, 0))
            screen.blit(glass.image, glass.rect)

            group_ball_1.draw(screen)
            # 再得到带通道的大小和screen一致的surface
            # 注意这里的fill, 虽然是透明, 但也能实现覆盖之前内容的效果
            # 所以没必要每次生成一个s2
            screen_alpha.fill(WHITE_TRANS)
            screen_alpha.blit(image_pause, rect_pause)
            # 注意这里还要把合成后的图像画到screen上去
            screen.blit(screen_alpha, (0, 0))

            # 这里状态转换为什么要放下面, 因为initialize完一些素材就变了
            # 只有应该走新stage的渲染逻辑而不是老的; 放上面改完会接着往下走
            # 其实其他控制类的事件也能放在下面, 无非是改完, 下一帧update, draw
            for e in event:
                if e.type == MOUSEBUTTONDOWN and collidepoint(rect_pause, e.pos):
                    stage = PLAY
                    initialize(stage, START)

        elif stage == PLAY:

            screen.blit(image_bg, (0, 0))

            glass.update_mouse()
            screen.blit(glass.image, glass.rect)

            screen.blit(image_unpause, rect_unpause)

            group_ball_1.update(screen)
            group_ball_1.draw(screen)
            group_ball_2.update(screen)
            group_ball_2.draw(screen)
            group_ball_3.draw(screen)

            checkCollide(group_ball_1, group_ball_2)

            for e in event:
                if e.type == GAMEOVER:
                    stage = LOSE
                    initialize(stage, PLAY)
                elif e.type == MOUSEMOTION:
                    times += 1
                elif e.type == TIMER:
                    for each in group_ball_1:
                        if each.check(times):
                            each.image = each.image_green
                            each.velocity = [0, 0]
                            group_ball_1.remove(each)
                            group_ball_2.add(each)
                            times = 0

                elif e.type == KEYDOWN:
                    # 不要随便用一堆if, 上面的if可能会改动一些东西对下面的if有影响; 用elif
                    if e.key == K_p:
                        stage = PAUSE
                        initialize(stage, PLAY)
                    elif e.key == K_w:
                        for each in group_ball_2:
                            # 注意同一个方向速度绝对值不能过大, 不然相撞以后
                            # 随机出来新速度可能无法达到逃逸速度
                            each.velocity = velocity1step(each.velocity, 'n')
                    elif e.key == K_s:
                        for each in group_ball_2:
                            each.velocity = velocity1step(each.velocity, 's')
                    elif e.key == K_a:
                        for each in group_ball_2:
                            each.velocity = velocity1step(each.velocity, 'w')
                    elif e.key == K_d:
                        for each in group_ball_2:
                            each.velocity = velocity1step(each.velocity, 'e')

                    elif e.key == K_SPACE:
                        for each in group_ball_2:
                            if isCover(each):
                                each.velocity = [0, 0]
                                group_ball_2.remove(each)
                                group_ball_3.add(each)
                                if len(group_ball_3) < BALL_NUM:
                                    channel = pg.mixer.find_channel()
                                    channel.play(sound_hole)
                                else:
                                    stage = WIN
                                    initialize(stage, PLAY)

        elif stage == PAUSE:
            screen.blit(image_bg, (0, 0))
            screen.blit(glass.image, glass.rect)
            group_ball_1.draw(screen)
            group_ball_2.draw(screen)
            group_ball_3.draw(screen)

            screen_alpha.fill(WHITE_TRANS) # 半透明遮罩
            screen_alpha.blit(image_pause, rect_pause)
            screen.blit(screen_alpha, (0, 0))

            for e in event:
                if e.type == KEYDOWN:
                    if e.key == K_p:
                        stage = PLAY
                        initialize(stage, PAUSE)

        elif stage == WIN:
            screen.blit(image_bg, (0, 0))
            screen.blit(glass.image, glass.rect)
            group_ball_3.draw(screen)

            screen_alpha.fill(WHITE_TRANS)
            screen_alpha.blit(image_win, rect_win)
            screen.blit(screen_alpha, (0, 0))

            for e in event:
                if e.type == MOUSEBUTTONDOWN and rect_win.collidepoint(e.pos):
                    # 这里不能用pg.quit(), 因为逆init后就不能执行flip什么的了
                    # 这里要直接跳出循环
                    sys.exit()

        elif stage == LOSE:
            screen.fill(WHITE)
            screen.blit(text_lose, text_rect)

            for e in event:
                if e.type == MOUSEBUTTONDOWN and text_rect.collidepoint(e.pos):
                    stage = PLAY
                    initialize(stage, LOSE)

        pg.display.flip()
        clock.tick(FRAME)


if __name__ == '__main__':
    try:
        main()
        print("正常退出")
    except SystemExit as e:
        print("sys.exit() with code {}".format(e.code))
        raise e
        # sys.exit()会抛出SystemExit异常
        # 如果不捕获, 则python解释器会退出
        # 捕获了, 如果还想实现提前退出,
        # 得显式raise出来或者再调一次sys.exit()
        # 当然如果后面没其他代码要执行了, 不raise, 直接来个pass等程序结束也行
    except:
        # traceback配合try-except使用, 捕获异常后还能打印traceback信息
        pg.quit()  # pygame.quit()是和pygame.init()对应的, 可多次重复调用, 后面的无效果
        # python解释器退出的时候比如调了sys.exit()会自动调pygame.quit()
        # 如果想在pygame结束后还有其它操作, 那用pygame.quit(), 仅退pygame, 不退主体程序
        traceback.print_exc()



