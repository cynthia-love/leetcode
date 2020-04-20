# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    break和continue
"""

# 输入预期答案才退出

ans = "我爱小甲鱼"

while True:
    pin = input("请输入小甲鱼最想听的一句话:")
    if pin == ans: break
    print("抱歉, 错了, 请重新输入(输入正确才能退出游戏)")

print("哎呦, 猜对啦!")


# continue会跳过本次循环, 之后测试循环条件进行下次循环
count = 10
for i in range(count):
    if i % 2 == 1:
        continue
    print(i)

# 如果在循环体中会改变循环计数变量, 尽量用while而不是for
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(count)
    count += 1
