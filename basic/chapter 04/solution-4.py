# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    循环语句, while和for
"""

# while
count = 3

while count:
    print(count)
    count -= 1


# for循环会自动调用迭代器的next方法
chars = "Hello World!"
for c in chars:
    print(c, end="")
print("")


for i in range(3):
    print(i)

for i in range(1, 4):
    print(i)

for i in range(2, 8, 2):
    print(i)
