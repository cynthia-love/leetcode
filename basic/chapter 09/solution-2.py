# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    丰富的else语句
"""

# if-else
if 1 > 10:
    print("if")
else:
    print("else")

# for-else
for i in [1, 2, 3, 4]:
    if i == 2:
        print("找到2")
        break
else:
    print("循环正常执行完才会执行这里, break的不会")  # 利用这个特性可以优化一些代码逻辑
    print("找不到")

# while-else
index = 1
while index <= 100:
    if index % 11 == 0:
        print(index)
        break
    else: index += 1
else:
    print(-1)

# try-else
try:
    x = 1
except:
    print("error")
else:
    print("正常执行")
finally:
    print("无论对错的收尾代码")
