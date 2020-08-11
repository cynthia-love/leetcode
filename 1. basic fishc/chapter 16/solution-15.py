# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第二个简单例子, 农民吃苹果
    上一个游戏的升级版, 加入动态贴图什么的
    这里用到更多的碰撞检测函数, 简单做个说明
    1. pygame.sprite.spritecollide(sprite,sprite_group,bool), 第一个精灵会与第二个精灵组里的
    精灵一个个去进行矩形碰撞检测, 并将有发生碰撞的作为一个列表返回; bool为True删除组中碰撞的, False不删,
    注意, 这个函数还有第四个参数, 指定碰撞类型, 可以指定pg.sprite.collide_mask就可以实现一对多
    的像素遮罩检测
    2. pygame.sprite.spritecollideany(), 与1类似, 但返回是否存在碰撞的bool值, 且没有是否删除参数
    3. pygame.sprite.groupcollide(), 检测两个组之间的矩形碰撞检测
    4. pygame.sprite.collide_rect(sprite_1,sprite_2), 两个精灵之间的矩形检测, 返回bool
    还有一个类似的pygame.sprite.collide_rect_ratio( 0.5 )(sprite_1,sprite_2), 指定碰撞多少算碰
    5. pygame.sprite.collide_circle(sprite_1,sprite_2), 两个精灵之间的圆形检测, 返回bool
    同样有一个变体pygame.sprite.collide_circle_ratio()
    6. 最关键的, 两个元素之间最有可能用到的更精确的像素遮罩检测
    pygame.sprite.collide_mask(sprite_1,sprite_2)

    另外, 注意几个点
    1. 农民和苹果具有不同的行为, 不要用同一个精灵类
    2. 动画的动作刷新频率不要和整个帧数一致(只能做到小于, 做不到大于), 这样可以既保证整体刷新频率够高,
    不晃眼, 又能自定义农民的动作不过快. 用pg.time.get_ticks()实现.

    3. 类封装的时候要足够完备, 且对外暴露的要可理解, 比如暴露direction就比暴露行数index好
    4. update函数调的比较频繁, 里面可能用到的子图对象等在初始化的时候就要生成, 不然随着时间进行,
    会生成越来越多的对象, 影响整体游戏性能
    5. 考虑到按键切换时可能会先按下再松开, 所以最好不要直接用e.type == KEYDOWN, e.key == K_UP,
    这种形式是瞬时效果, 而我们要的是延续性效果, 用pygame.key.get_pressed()
    6. 农民切图的时候, 不要无脑切等分矩形, 切的越精细越好, 最好是最小长方形
    7. 此例还用到pg.time.get_ticks()和clock.tick(100), 前者返回自pg.init()后的毫秒数
    后者返回自上一次执行clock.tick()后的毫秒数; 另外注意, clock.tick()的参数是帧, 用1000/100,
    即clock.tick(100)相当于sleep(10)
"""

import sys
import random
import pygame as pg
from pygame.locals import *

# 定义常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

TITLE = "Eat Apples"
SIZE = WIDTH, HEIGHT = 600, 600

# 整体帧数, 农民动画的帧数
FRAME, FRAME_FARMER = 100, 10

APPLE_NUM = 100
SPEED = 5


class Velocity:
    # 速度类, 主要包括两个属性, 方向和speed
    # 初始化和设置v时需要传入方向和speed
    def __init__(self):
        self.d2v = {
            'c': (0, 0),  # c表示原地不动
            'n': (0, -1),
            'ne': (1, -1),
            'e': (1, 0),
            'se': (1, 1),
            's': (0, 1),
            'sw': (-1, 1),
            'w': (-1, 0),
            'nw': (-1, -1)
        }
        self.direction = 'c'
        self.speed = 0

    # v要随时跟着direction和speed更新
    # 每次direction, speed变都重新计算一次没必要, 不如用property
    def _getv(self):
        v_base = self.d2v[self.direction]
        return v_base[0]*self.speed, v_base[1]*self.speed

    # property的set函数只能接受一个参数, 所以这里value得是个元组(方向, speed)
    def _setv(self, value):
        self.direction, self.speed = value

    v = property(_getv, _setv)

# Apple类应该是和其图片绑定的, 比如切边多少, 这些不同图片都是不一样的, 所以filename从外面传意义不大
class Apple(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        filename = "img/apple.png"
        # image_base没有其他地方用到, 没必要加到self里去
        image_base = pg.image.load(filename).convert_alpha()
        rect_base = image_base.get_rect()

        # 有些原图边界太大, 不利于后续设定位置和碰撞检测什么的, 所以要把中间有实际内容的子图提取出来
        # 上下左右的边界宽度可以用ps工具的窗口-信息获取
        left, right, top, bottom = 4, 5, 3, 3
        width, height = rect_base.width-left-right, rect_base.height-top-bottom
        rect = Rect(left, top, width, height)

        # Sprite类的两个必备参数, self.image和self.rect
        self.image = image_base.subsurface(rect)
        self.rect = self.image.get_rect()
        # width和height只读不改, 直接这么设置就行
        # 如果会变, 那这么写就不行了, self.rect变了self.width和self.height不会跟着更新
        # 直接改self.width和self.height也不会反映到self.rect上去
        # 如果是对象的某一个一般类型的属性想要快速访问, 不建议这么写, 最好用property建议绑定关系
        """
        self.width = self.rect.width
        self.height = self.rect.height
        """

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
    def _setwidth(self, value): self.rect.width = value
    width = property(_getwidth, _setwidth)

    def _getheight(self): return self.rect.height
    def _setheight(self, value): self.rect.height = value
    height = property(_getheight, _setheight)

class Farmer(pg.sprite.Sprite):
    # direction表示朝向, 取值n, ne, e, se, s, sw, w, nw; step取值为0-7
    # tick表示farmer本身的帧数, 比如整体帧数100, 即每10ms一帧
    # farmer设置帧数10, 即每100ms一帧, 那么只有整体第10帧的时候farmer才会动一下
    def __init__(self, direction, frame_number=10):
        pg.sprite.Sprite.__init__(self)
        # 四个方向, 32张图, 全都在init里加载完, 不要再update里新生成对象
        filename = "img/farmer.png"
        # 虽然原图就带alpha通道, 但这里的convert_alpha()也是有必要的
        # 不然会在blit的时候实时地转
        image_base = pg.image.load(filename).convert_alpha()
        rect_base = image_base.get_rect()

        self.shape = 8, 8

        # 每一个子图块的宽高, 注意这里并不是最终要的子图的宽高, 还得再去掉上下左右
        width_block, height_block = int(rect_base.width/self.shape[1]), int(rect_base.height/self.shape[0])
        left, right, top, bottom = 28, 24, 16, 12
        width, height = width_block - left - right, height_block - top - bottom

        i2d = {0: 'n', 1: 'ne', 2: 'e', 3: 'se', 4: 's', 5: 'sw', 6: 'w', 7: 'nw' }

        # 用self.frames把8个方向8帧共计64张子图全部存下来, 免得后面再生成
        # 格式: {方向: {第几帧: 子图}}
        self.frames = {}
        for row in range(self.shape[0]):
            self.frames[i2d[row]] = {}
            for col in range(self.shape[1]):
                # 计算块的左上位置
                x_block, y_block = col*width_block, row*height_block
                # 根据块的左上位置, 再计算实际要截取的子图的左上位置, 宽, 高之前已经计算完了
                x, y = x_block+left, y_block+top
                self.frames[i2d[row]][col] = image_base.subsurface((x, y, width, height))

        # 把当前方向, 当前处在第几步也存下来, 默认step取0
        self.direction = direction
        self.step = 0

        self.image = self.frames[self.direction][self.step]
        self.rect = self.image.get_rect()

        # 获取得到第一张图时的时间戳
        self.tick = pg.time.get_ticks()
        # 存储帧更新的最小时间间隔, 10帧则最小时间间隔1000/10 = 100ms
        # 注意这个只影响动作, 不影响方向和位置
        self.delay = int(1000/frame_number)

    # 位置的移动比较复杂, 还涉及是否超出范围, 不过那部分逻辑不要在property
    # property的set只支持一个参数, 这里简单建立映射关系就好
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
    def _setwidth(self, value): self.rect.width = value
    width = property(_getwidth, _setwidth)

    def _getheight(self): return self.rect.height
    def _setheight(self, value): self.rect.height = value
    height = property(_getheight, _setheight)

    # 农民的转向, 移动, 原地动画用了三个函数实现
    # 这三个函数都能改变状态, 比如只调turn不调update, 只是原地转向, 且无动画效果
    def turn(self, direction):
        # 转向后从第一个动作开始
        if self.direction != direction:
            self.direction = direction
            self.step = 0
            self.image = self.frames[self.direction][self.step]

    # 普通移动直接改self.x和self.y就行了, 这里的移动支持在某个surface内部移动
    # velocity格式(vx, vy), 带方向
    def move(self, surface, velocity):
        rect = surface.get_rect()
        if 0 <= self.x + velocity.v[0] <= rect.width-self.width:
            self.x += velocity.v[0]
        if 0 <= self.y + velocity.v[1] <= rect.height-self.height:
            self.y += velocity.v[1]

    # 注意update函数什么时候用, 批量更新
    # 比如farmer就一个, 能直接改它的image和rect, 那么可以直接改, update就不是必须的
    # 需要整个组调用的时候update才有用, 其他函数名group调的时候无法传导到每个精灵
    # 这里借用update做一下动作更新, 取其他名也行, 别用group调就行了
    def update(self):
        # 更新分两块, 第一块是换帧, 即动画效果
        tick = pg.time.get_ticks()
        if tick-self.tick >= self.delay:
            self.step = self.step+1 if self.step < self.shape[1]-1 else 0
            self.image = self.frames[self.direction][self.step]
            self.tick = tick

# Health和Text这种简单要素直接渲染就行, 不要再去写精灵类了
class Health(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()

        self.color = color
        self.percent = 0

        self.font = pg.font.Font('font/Symbol.ttf', int(height*0.7))

        self.draw(self.percent)

    # 直接在Surface上画图比较特殊, 每次有变化得整个重画, 所以独立一个函数出来
    def draw(self, percent):
        self.image.fill((255, 255, 255))  # 这里设置fill是为了设置透明度
        self.image.set_colorkey((255, 255, 255))
        # 画外面的框
        pg.draw.rect(self.image, self.color, (0, 0, self.width, self.height), 3)
        # 画里面的血条, 0表示填充
        pg.draw.rect(self.image, self.color, (0, 0, int(self.width * percent), self.height), 0)

        # 参数2为是否抗锯齿, 参数3为字体颜色
        text_percent = self.font.render("{:.0%}".format(percent), True, (0, 0, 0))
        text_rect = text_percent.get_rect()
        # 计算中间位置
        x = int((self.width - text_rect.width) / 2)
        y = int((self.height - text_rect.height) / 2)

        self.image.blit(text_percent, (x, y))

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
    def _setwidth(self, value): self.rect.width = value
    width = property(_getwidth, _setwidth)

    def _getheight(self): return self.rect.height
    def _setheight(self, value): self.rect.height = value
    height = property(_getheight, _setheight)

    def update(self, percent):
        if self.percent != percent:
            # 数字修改得整个重画
            self.draw(percent)

class Text(pg.sprite.Sprite):
    def __init__(self, text, size):
        pg.sprite.Sprite.__init__(self)

        self.font = pg.font.Font(None, size)
        self.image = self.font.render(text, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.text = text

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
    def _setwidth(self, value): self.rect.width = value
    width = property(_getwidth, _setwidth)

    def _getheight(self): return self.rect.height
    def _setheight(self, value): self.rect.height = value
    height = property(_getheight, _setheight)

    def update(self, text):
        if self.text != text:
            self.image = self.font.render(text, True, (0, 0, 0))
            self.rect = self.image.get_rect()
            self.text = text

pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode(SIZE)

# farmer就一个, 其实没必要加到Group里去
group_farmer = pg.sprite.Group()
farmer = Farmer(direction='n', frame_number=FRAME_FARMER)
group_farmer.add(farmer)

group_apple = pg.sprite.Group()
for i in range(APPLE_NUM):
    apple = Apple()
    # 这里和farmer之间用和后面同样的碰撞检测函数, 确保生成时和农民没碰撞; 同时检测和之前生成的苹果是否碰撞
    while pg.sprite.collide_mask(farmer, apple) or pg.sprite.spritecollideany(apple, group_apple):
        apple.x = random.randint(0, WIDTH-apple.width)
        apple.y = random.randint(0, HEIGHT-apple.height)
    group_apple.add(apple)

group_health = pg.sprite.Group()
health = Health(GREEN, width=200, height=20)
health.x = int((WIDTH-health.width)/2)
health.y = HEIGHT-health.height-40
group_health.add(health)

group_text = pg.sprite.Group()
text_over = Text("Game Over", size=50)
text_over.x = int((WIDTH-text_over.width)/2)
text_over.y = int((HEIGHT-text_over.height)/2)
group_text.add(text_over)

# 初始速度
velocity = Velocity()

# 初始分数
score = 0

k2d = {
    K_UP: 'n',
    K_RIGHT: 'e',
    K_DOWN: 's',
    K_LEFT: 'w'
}

clock = pg.time.Clock()

while True:

    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

    keys = pg.key.get_pressed()
    sum = keys[K_UP]+keys[K_RIGHT]+keys[K_DOWN]+keys[K_LEFT]
    # 注意方向键系统有控制
    # 已经按下一个, 再按第二个, 可以识别为两个
    # 但已经按下两个, 再按第三个, 第三个识别为没按, 还按原来的两个来
    # 同时按下三个和四个会识别为都没按, 即0个

    if sum == 1 or sum == 2:
        direction = "{}{}{}{}".format(
            k2d[K_UP] if keys[K_UP] else "",
            k2d[K_DOWN] if keys[K_DOWN] else "",
            k2d[K_RIGHT] if keys[K_RIGHT] else "",
            k2d[K_LEFT] if keys[K_LEFT] else ""
        )
        if direction == 'ns' or direction == 'ew':
            velocity.speed = 0
        else:
            velocity.direction = direction
            velocity.speed = SPEED

            farmer.turn(direction)
            farmer.move(screen, velocity)
    else:
        velocity.speed = 0

    screen.fill(WHITE)

    # 这里的移动可以放在update里做, 也可以在上面的按键部分
    # 检测到按键, 就直接move了(改x和y), 再用update更新子图
    # 注意, 精灵改变后, 不需要调update, 直接调draw也能更新成新的
    # 比如这里只调move不调update, farmer位置也会移动
    # update什么时候用呢, 精灵组按照一定逻辑批量更新
    # 这里farmer只有一个, 直接更新farmer本身就行, 组级的update不是必要的

    if score < APPLE_NUM:
        # 如果动了, 检测碰撞, 全部检测完, 更新分数
        # 如果不想全部遍历也可以加一步1对多的矩形碰撞检测; 注意这里的False, 这一步不删apple精灵
        # 这里可以直接指定第四个参数实现一对多的像素遮罩检测
        if velocity.speed and pg.sprite.spritecollideany(farmer, group_apple, False):
            for apple in group_apple:
                if pg.sprite.collide_mask(farmer, apple):
                    group_apple.remove(apple)
                    score += 1

            # Health里有控制同样百分比不更新, 所以这里无脑调就行
            group_health.update(score / APPLE_NUM)

        # # farmer的update里只更新动画, 这里不调update, 转向和移动是不影响的
        group_farmer.update()
        group_apple.draw(screen)
        group_farmer.draw(screen)
        group_health.draw(screen)
    else:

        # 单个体的精灵其实没必要加到组里去, 可以直接blit渲染
        # 需要批量更新的时候group才有用

        group_text.draw(screen)

        text_score = Text("Score: {}".format(score), 33)
        text_score.x = int((WIDTH-text_score.width)/2)
        text_score.y = text_over.y+text_over.height+10
        screen.blit(text_score.image, text_score.rect)

    pg.display.flip()
    clock.tick(FRAME)