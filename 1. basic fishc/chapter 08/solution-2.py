# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    操作系统模块os和os.path
"""
import os
print(os.getcwd())  # C:\Projects\leetcode\basic fishc\chapter 08, 当前工作目录

os.chdir("C:/Projects")
print(os.getcwd())
os.chdir("C:/Projects/leetcode/basic fishc/chapter 08")

print(os.listdir("."))  # 当前目录
print(os.listdir("C:/Projects"))  # 指定目录

# 创建文件夹, 存在抛出异常
try:
    os.mkdir("data")
except FileExistsError:
    print("创建失败, 文件存在")

# 递归创建多级目录, 存在抛出异常
"""
try:
    os.makedirs(r"data2\aaaa\aaa")
except:
    print("创建失败")
"""

# 删除文件, 删除目录, 删除多级目录
# os.remove("test/test.txt"), remove删除单个文件
# os.rmdir("test"), 注意, rmdir只能删除非空目录
# os.removedirs("test"), removedirs递归删除目录, 但也必须是非空的
# 递归删除非空, 用shutil里的rmtree
# import shutil
# shutil.rmtree(r"test")

# rename重命名目录或文件
os.rename("data/boy_2.txt", "data/boy_2.txt")
os.rename("data", "data")

print(os.name)  # 指代当前使用的操作系统

# os.system()用于执行一些命令
os.system("ls")
# os.system("python solution-1.py")

# 递归遍历, 深度优先返回(路径, [包含目录], [包含文件])
print(list(os.walk("dir")))

# ******************************************************************
# 相对于os, os.path模块更专业地去处理path(大部分其实可以直接通过字符串操作实现)
from os import path
print(path.dirname("aaa/aaa/aaaa.txt"))  # 可以是不存在的目录, 返回最后一个/前面的目录, aaa/aaa
print(path.basename("aaa/aaa/aaaa.txt"))  # 可以是不存在的目录, 直接返回最后一个/后面的字符串, aaaa.txt
print(path.split("aaa/aaa/aaaa.txt"))  # 上面两个操作的合体, 不带/
print(path.splitext("aaa/aaa/aaaa.txt")) # 按最后一个.而不是/拆分, 扩展名带.
print(path.join("aaa", "bbb", "ccc"))  # 无非拿/拼到了一起而已, aaa\bbb\ccc

# 拿到目录/文件的基本信息
print(path.getsize("data"))  # 4096
print(path.getsize("data/data.txt")) # 6
print(path.getctime("data"))
print(path.getatime("data"))
import time
print(time.localtime(path.getmtime("data")))  # 转换成time.struct_time类型

# 是否判断
print(path.exists("data/data.txt"))  # 是否是目录或文件
print(path.isdir("data"))  # 是否是目录
print(path.isfile("data/data.txt"))  # 是否是文件
print(path.isabs("data"))  # 是否是绝对路径
print(path.isabs("C:/"))
print(path.samefile("data", "../chapter 08/data"))  # 判断俩路径是否是同一个目录/文件