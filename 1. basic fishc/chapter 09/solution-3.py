# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    with语句, 保证不管处理过程中是否发生异常都会执行规定的__exit__（“清理”）操作，释放被访问的资源，比如有文件
    读写后自动关闭、线程中锁的自动获取和释放等。
    注意, with是释放资源, 不是自动处理Exception!!!
"""

try:
    with open("aaa.txt") as f:  # 这里用with, 那么不管程序有没有正确打开, 清理工作都不用自己去做了
        for line in f: print(line)
except OSError as e:
    print("出错了", e)
else:
    print("没出错")