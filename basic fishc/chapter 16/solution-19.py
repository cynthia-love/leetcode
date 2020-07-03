# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    将pygame每一帧分别转成gif和mp4格式
"""
import cv2
import sys
import numpy
import random
import imageio
import pygame as pg
from PIL import Image
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import concatenate_audioclips
from moviepy.editor import CompositeVideoClip
from moviepy.editor import CompositeAudioClip
# concatenate是拼接, Composite是混到一起
from pygame.locals import *

TITLE = "BALL"
SIZE = WIDTH, HEIGHT = 1024, 681
SIZE_BALL = WIDTH_BALL, HEIGHT_BALL = 100, 100

BALL_NUM = 5
SPEED_MAX = 5

FRAME = 100

class Ball(pg.sprite.Sprite):
    def __init__(self, pos, velocity):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("image/green_ball.png")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = pos

        self.velocity = velocity

    def _getpos(self): return self.rect.x, self.rect.y
    def _setpos(self, value): self.rect.x, self.rect.y = value
    pos = property(_getpos, _setpos)

    # 普通的移动直接self.rect.move就行了, 这里要实现越界回来
    # 批量调放group里
    def update(self, surface):

        rect = surface.get_rect()
        self.rect = self.rect.move(self.velocity)

        # 向左完全隐藏
        if self.rect.right < 0:
            self.rect.left = rect.width

        # 向右完全隐藏
        if self.rect.left > rect.width:
            self.rect.right = 0

        # 向上完全隐藏
        if self.rect.bottom < 0:
            self.rect.top = rect.height

        # 向下完全隐藏
        if self.rect.top > rect.height:
            self.rect.bottom = 0

def random_velocity():
    velocity = [random.randint(-10, 10), random.randint(-10, 10)]
    while velocity == [0, 0]:
        velocity = [random.randint(-10, 10), random.randint(-10, 10)]
    return velocity

pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode(SIZE)

image_bg = pg.image.load("image/background.png").convert_alpha()

group_ball = pg.sprite.Group()

for i in range(BALL_NUM):
    pos = random.randint(0, WIDTH-WIDTH_BALL), random.randint(0, HEIGHT-HEIGHT_BALL)
    velocity = random_velocity()

    ball = Ball(pos, velocity)

    while pg.sprite.spritecollide(ball, group_ball, False):
        ball.pos = random.randint(0, WIDTH-WIDTH_BALL), random.randint(0, HEIGHT-HEIGHT_BALL)
    group_ball.add(ball)

clock = pg.time.Clock()

count, frames = 1, 1000
images = []
print("开始")
while count <= frames:
    for e in pg.event.get():
        if e.type == QUIT:
            sys.exit()

    screen.blit(image_bg, (0, 0))
    group_ball.update(screen)
    group_ball.draw(screen)

    for item in group_ball:
        group_ball.remove(item)
        if pg.sprite.spritecollide(item, group_ball, False):
            item.velocity[0] = -item.velocity[0]
            item.velocity[1] = -item.velocity[1]
        group_ball.add(item)


    pg.display.flip()

    # 把screen对象转成图片给存起来; 如果是全屏的话, 用PIL的截屏也行
    # 第三个参数指定是否上下颠倒, 个别图片库要这种格式, 默认不
    image_bytes = pg.image.tostring(screen, 'RGBA', False)
    # 这里先不要处理, 先添加了再说, 免得影响正常的游戏流程
    images.append(image_bytes)

    c = clock.tick(FRAME)  # 这里实际输出的是20-30左右, 而不是1000/100=10
    count += 1

pg.quit()

# 新版python把bytes和string独立开了, 不过部分包还没改方法名
# 先将bytes格式转化成PIL支持的图片格式
images = [Image.frombytes("RGBA", (WIDTH, HEIGHT), x) for x in images]
images = [x.resize((int(WIDTH*0.3), int(HEIGHT*0.3)), Image.ANTIALIAS) for x in images]
# 注意上面两步转换都没有损失图片质量, 存gif的时候位深却变成了8...

# duration指定两张图之间的时间间隔, 也可以用fps代替
# pillow模块也可以存gif, 但好像效果不是特别好, 最好别用
# 图片太多的时候不要去生成gif, 会很慢
# imageio.mimsave("image/ball.gif", images, duration=0.01)
# imageio.mimsave("image/ball.gif", images, fps=FRAME)

# CV2不能直接存PIL的图片格式, 还得转一步
# 如果有现成的图片, 可以直接用CV2读取
# img = cv2.imread(url, flags)
# flags取值cv2.IMREAD_COLOR, 即RGB, IMREAD_UNCHANGED, 即RGBA, IMREAD_GRAYSCALE灰度
images = [cv2.cvtColor(numpy.asarray(x), cv2.COLOR_RGB2BGR) for x in images]
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
mp4_writer = cv2.VideoWriter("image/ball.mp4", fourcc, FRAME/2, (int(WIDTH*0.3), int(HEIGHT*0.3)))
for each in images:
    mp4_writer.write(each)
mp4_writer.release()
# 根据图片张数和视频帧数, 可以直接算出来时长, 比如1000张图, fps取100, 每秒100张, 那总时长10秒

# 完事还可以继续给视频添加背景音乐, 视频处理有专门的包moviepy
video = VideoFileClip("image/ball.mp4")
print(video.duration)
audio = AudioFileClip("sound/bg_music.ogg")
audio = audio.subclip(0, video.duration)
print(audio.duration)
# 注意, 视频, 音频不同长不要直接去合并, 总长度会按长的来, 但
# 视频过长, 后面没声音; 音频过长, 视频虽然显示长度长, 但播放一半闪退
video = video.set_audio(audio)
video.write_videofile("image/ball2.mp4")

# 更灵活的处理方法是截取视频不同的subclip, 混淆声音后设为背景, 再把各视频clip拼接起来
# 比如以bass2.mp4为基础, 在10s位置再混入笑声
video = VideoFileClip("image/ball2.mp4")
video_clip1 = video.subclip(0, 10)
video_clip2 = video.subclip(10, video.duration)

laugh = AudioFileClip("sound/laugh.wav")

audio_clip1 = video_clip1.audio
audio_clip2 = video_clip2.audio

# 注意混入不需要俩音频一般长
audio_clip2 = CompositeAudioClip([audio_clip2, laugh])

video_clip2 = video_clip2.set_audio(audio_clip2)

video = concatenate_videoclips([video_clip1, video_clip2])
video.write_videofile("image/ball3.mp4")

