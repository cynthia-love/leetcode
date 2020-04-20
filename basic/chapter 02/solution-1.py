# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第2章  用Python设计第一个游戏
"""

"""
    第一个小游戏
"""

temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字: ")

guess = int(temp)

if guess == 8:
    print("猜中啦!")
else:
    print("猜错啦! 小甲鱼现在心里想的是8!")

print("游戏结束, 不玩啦!")

# dir(__builtins__)可以打印出python中的所有内置函数
# help(xx)可以显示具体内置函数的功能描述
print(dir(__builtins__))
help(print)
