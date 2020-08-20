# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    测试生日悖论
    当n >= 24时, 有两个人生日相同的概率是50%以上
    分别输入n=5, 10, ....100, 随机生成生日看生日相同概率
"""
import random

yes, no = 0, 0
for i in range(24, 30, 1):

    birthdays = {(random.randint(1, 12), random.randint(1, 31)) for _ in range(i)}
    if len(birthdays) < i:
        yes += 1
    else:
        no += 1

print(yes/(yes+no))
