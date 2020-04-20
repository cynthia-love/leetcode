# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    改进我们的小游戏
    1. 三次猜的机会
    2. 提示大了还是小了
    3. 每次运行程序答案随机
"""

from random import randint

ans = randint(1, 10)

count = 3

print("不妨猜一下我现在心里想的是哪个数字: ")
while count > 0:
    guess = int(input())
    if guess == ans:
        print("哎呀, 猜中了!")
        break
    elif guess > ans:
        print("嘿, 大了大了~~~")
    else:
        print("嘿, 小了小了~~~")
    count -= 1

print("游戏结束, 不玩啦!")
