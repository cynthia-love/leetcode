# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    输入输出
    包括控制台标准输入输出和文件输入输出
"""

# print, 默认以空格分隔多个参数, 最末尾添加换行符
print(1, 2, 3)  # 非str参数会自动强制抓换str(obj)
print(1, 2, 3, sep="", end="结束\n")  # 分隔符和末尾字符都可以自定义
print(1, 2, 3, sep=", ", end="\n", file=open("data/out.txt", "w"))
# 可以通过file参数直接将print内容直接写入到文件

# input, 直到按下返回键作为一次输入(不包括\n)
# pin = input("Enter integer x and y, separated by spaces: ").split(" ")
# print(int(pin[0]), int(pin[1]))

# open(), 返回文件指针, r和w初始指向0位置, a初始指向文件尾
# close()方法会关闭文件, 确保写入的内容已经保存
with open("data/out.txt", "r") as f:
    print(f.read(1))  # 读取指定个字符
    print(f.tell())
    f.seek(0, 0)
    print(f.read())  # 读取当前位置到文件末尾全部字符
    f.seek(0, 0)
    print(f.readline())
    f.seek(0, 0)
    print(f.readlines())  # ['1, 2, 3\n']
    f.seek(0, 0)
    for line in f:
        print("aaa", line, sep="*", end="")
    print(f.tell())  # 一共8个字符, 0-7, 文件尾索引是8, 即字符个数+1

with open("data/out2.txt", "w") as f:
    f.write("aaaa")
    f.write("bbb\n")
    f.writelines(["ccc", "ddd"])
    # 注意write和writelines都不会自动插入换行符, 如果想要, 得手动去添加