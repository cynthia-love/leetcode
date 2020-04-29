# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    操作系统模块os
"""
import os
print(os.getcwd())  # C:\Projects\leetcode\basic\chapter 08

os.chdir("C:/Projects")
print(os.getcwd())
os.chdir("C:/Projects/leetcode/basic/chapter 08")

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
import shutil
shutil.rmtree(r"test")