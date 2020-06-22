# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    农民吃苹果
    上一个游戏的升级版, 加入动态贴图什么的
    这里用到更多的碰撞检测函数, 简单做个说明
    1. pygame.sprite.spritecollide(sprite,sprite_group,bool), 第一个精灵会与第二个精灵组里的
    精灵一个个去进行矩形碰撞检测, 并将有发生碰撞的作为一个列表返回; bool为True删除组中碰撞的, False不删
    2. pygame.sprite.spritecollideany(), 与1类似, 但返回是否存在碰撞的bool值
    3. pygame.sprite.groupcollide(), 检测两个组之间的矩形碰撞检测
    4. pygame.sprite.collide_rect(sprite_1,sprite_2), 两个精灵之间的矩形检测, 返回bool
    还有一个类似的pygame.sprite.collide_rect_ratio( 0.5 )(sprite_1,sprite_2), 指定碰撞多少算碰
    5. pygame.sprite.collide_circle(sprite_1,sprite_2), 两个精灵之间的圆形检测, 返回bool
    同样有一个变体pygame.sprite.collide_circle_ratio()
    6. 最关键的, 两个元素之间最有可能用到的更精确的像素遮罩检测
    pygame.sprite.collide_mask(sprite_1,sprite_2)

    另外, 注意几个点
    1. 农民和苹果具有不同的行为, 不要用同一个精灵类
    2. 动画的动作刷新频率不要和整个帧数一致(只能做到小于, 做不到大于)
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

APPLE_NUM = 100

class Velocity:

    def __init__(self, direction, speed):
        self.directions = {
            'n': (0, -1),
            'ne': (1, -1),
            'e': (1, 0),
            'se': (1, 1),
            's': (0, 1),
            'sw': (-1, 1),
            'w': (-1, 0),
            'nw': (-1, -1)
        }
        self.direction = direction
        self.speed = speed

    def _getv(self):
        v_base = self.directions[self.direction]
        return v_base[0]*self.speed, v_base[1]*self.speed

    v = property(_getv)

# Apple类应该是和其图片绑定的, 比如切边多少, 这些不同图片都是不一样的, 没法从外面传入
class Apple(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        filename = "img/apple.png"
        # 上下左右的边界宽度可以用ps工具的窗口-信息获取
        left, right, top, bottom = 4, 5, 3, 3

        self.image_base = pg.image.load(filename).convert_alpha()
        self.rect_base = self.image_base.get_rect()

        width, height = self.rect_base.width-left-right, self.rect_base.height-top-bottom
        rect = Rect(left, top, width, height)

        self.image = self.image_base.subsurface(rect)
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    # 为什么width可以直接写而x和y要用property
    # 因为x和y需要支持设置, 直接self.x = self.rect.x的话, 设置的时候无法设置到self.rect.x
    def getx(self): return self.rect.x
    def setx(self, value): self.rect.x = value
    x = property(getx, setx)

    def gety(self): return self.rect.y
    def sety(self, value): self.rect.y = value
    y = property(gety, sety)

    def getpos(self): return self.rect.x, self.rect.y

    def setpos(self, value):
        self.rect.x = value[0]
        self.rect.y = value[1]

    pos = property(getpos, setpos)


class Farmer(pg.sprite.Sprite):
    # direction表示朝向, 取值n, e, s, w; step取值为0-7
    # tick表示farmer本身的帧数, 比如整体帧数100, 即每10ms一帧
    # farmer设置帧数10, 即每100ms一帧, 那么只有整体第10帧的时候farmer才会动一下
    def __init__(self, direction, tick=10):
        pg.sprite.Sprite.__init__(self)
        # 四个方向, 32张图, 全都在init里加载完, 不要再update里新生成对象
        filename = "img/farmer.png"
        self.image_base = pg.image.load(filename).convert_alpha()
        self.rect_base = self.image_base.get_rect()

        width_block, height_block = 96, 96
        left, right, top, bottom = 28, 24, 16, 12
        directions = {
            'n': 0,
            'ne': 1,
            'e': 2,
            'se': 3,
            's': 4,
            'sw': 5,
            'w': 6,
            'nw': 7
        }
        self.steps = 8
        self.frames = {}
        for key in directions.keys():
            self.frames[key] = {}
            for col in range(self.steps):
                x_block = col*width_block
                y_block = directions[key]*height_block
                x, y = x_block+left, y_block+top
                width, height = width_block-left-right, height_block-top-bottom
                rect = Rect(x, y, width, height)
                self.frames[key][col] = self.image_base.subsurface(rect)

        self.direction = direction
        self.step = 0

        self.image = self.frames[self.direction][self.step]
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        self.tick = pg.time.get_ticks()
        self.delay = int(1000/tick)

    def getx(self): return self.rect.x
    def setx(self, value): self.rect.x = value
    x = property(getx, setx)

    def gety(self): return self.rect.y
    def sety(self, value): self.rect.y = value
    y = property(gety, sety)

    def getpos(self): return self.rect.x, self.rect.y

    def setpos(self, value):
        self.rect.x = value[0]
        self.rect.y = value[1]

    pos = property(getpos, setpos)

    # 移动直接在update里做了, 没必要再单整个移动函数
    def move(self, surface, velocity):
        rect = surface.get_rect()
        if 0 <= self.x + velocity.v[0] <= rect.width-self.width:
            self.x += velocity.v[0]
        if 0 <= self.y + velocity.v[1] <= rect.height-self.height:
            self.y += velocity.v[1]

    def update(self, surface, velocity):
        # 更新分两块, 第一块是换帧, 即动画效果
        tick = pg.time.get_ticks()
        if tick-self.tick >= self.delay:
            self.step = self.step+1 if self.step < self.steps-1 else 0
            self.image = self.frames[self.direction][self.step]
            self.tick = tick

        # 第二块是设置图片新的位置
        # 如果不换帧只移动位置, 那只能看到静态图片移动, 而没有动画效果
        rect = surface.get_rect()
        if 0 <= self.x + velocity.v[0] <= rect.width-self.width:
            self.x += velocity.v[0]
        if 0 <= self.y + velocity.v[1] <= rect.height-self.height:
            self.y += velocity.v[1]

class Health(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        pg.draw.rect(self.image, color, (0, 0, width, height), 3)

        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        self.color = color
        self.percent = 0

        self.font = pg.font.Font(None, int(self.height*0.9))

    def getx(self): return self.rect.x
    def setx(self, value): self.rect.x = value
    x = property(getx, setx)

    def gety(self): return self.rect.y
    def sety(self, value): self.rect.y = value
    y = property(gety, sety)

    def getpos(self): return self.rect.x, self.rect.y

    def setpos(self, value):
        self.rect.x = value[0]
        self.rect.y = value[1]

    pos = property(getpos, setpos)

    def update(self, percent):
        if self.percent != percent:
            # 数字修改得整个重画
            self.image.fill((255, 255, 255))
            self.image.set_colorkey((255, 255, 255))
            pg.draw.rect(self.image, self.color, (0, 0, self.width, self.height), 3)
            pg.draw.rect(self.image, self.color, (0, 0, int(self.width*percent), self.height), 0)
            self.percent = percent

            img = self.font.render("{:.0%}".format(percent), True, (0, 0, 0))
            rect = img.get_rect()

            w = int((self.width-rect.width)/2)
            h = int((self.height-rect.height)/2)

            self.image.blit(img, (w, h))

class Text(pg.sprite.Sprite):
    def __init__(self, text, size):
        pg.sprite.Sprite.__init__(self)

        self.font = pg.font.Font(None, size)
        self.image = self.font.render(text, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.text = text

    def getx(self): return self.rect.x
    def setx(self, value): self.rect.x = value
    x = property(getx, setx)

    def gety(self): return self.rect.y
    def sety(self, value): self.rect.y = value
    y = property(gety, sety)

    def getpos(self): return self.rect.x, self.rect.y

    def setpos(self, value):
        self.rect.x = value[0]
        self.rect.y = value[1]

    pos = property(getpos, setpos)

    def update(self, text):
        if self.text != text:
            self.image = self.font.render(text, True, (0, 0, 0))
            rect_new = self.image.get_rect()
            self.rect.width = rect_new.width
            self.rect.height = rect_new.height
            self.text = text

title = "Eat Apples"
size = width, height = 600, 600

pg.init()
pg.display.set_caption(title)
screen = pg.display.set_mode(size)

group_farmer = pg.sprite.Group()
farmer = Farmer(direction='n', tick=10)
group_farmer.add(farmer)

group_apple = pg.sprite.Group()

for i in range(APPLE_NUM):
    apple = Apple()

    # 这里和farmer之间用和后面同样的碰撞检测函数, 确保生成时没碰撞; 同时检测和之前生成的苹果是否碰撞
    while pg.sprite.collide_mask(farmer, apple) or pg.sprite.spritecollideany(apple, group_apple):
        apple.x = random.randint(0, width-apple.width)
        apple.y = random.randint(0, height-apple.height)

    group_apple.add(apple)

group_health = pg.sprite.Group()
health = Health(GREEN, 200, 20)
health.x = int((screen.get_rect().width-health.width)/2)
health.y = screen.get_rect().height-health.height-20
group_health.add(health)

group_text = pg.sprite.Group()
text = Text("Game Over", 50)
text.x = int((screen.get_rect().width-text.width)/2)
text.y = int((screen.get_rect().height-text.height)/2)
group_text.add(text)

velocity = Velocity(direction='n', speed=0)
speed = 5

score = 0

text_score = Text("Score: {}".format(score), 30)

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
            farmer.direction = direction
            velocity.direction = direction
            velocity.speed = speed
            # farmer.move(screen, velocity)
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
        if velocity.speed:
            for apple in group_apple:
                if pg.sprite.collide_mask(farmer, apple):
                    group_apple.remove(apple)
                    score += 1
            group_farmer.update(screen, velocity)
            group_health.update(score / APPLE_NUM)

        group_apple.draw(screen)
        group_farmer.draw(screen)
        group_health.draw(screen)
    else:
        # group_text.draw(screen)
        # 单个体的精灵其实没必要加到组里去, 可以直接blit渲染
        # 需要批量更新的时候group才有用
        screen.blit(text.image, text.rect)

        text_score.update("Score: {}".format(score))
        text_score.x = int((screen.get_rect().width-text_score.width)/2)
        text_score.y = text.y+text.height+5

        screen.blit(text_score.image, text_score.rect)

    pg.display.flip()
    clock.tick(100)