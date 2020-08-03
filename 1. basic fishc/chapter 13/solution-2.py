# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    搜索路径
"""
# python模块的导入需要一个路径搜索的过程
import sys
print(sys.path)
"""
[
    '/Users/soso/leetcode/1. basic fishc/chapter 13',  当前运行代码所在路径
    '/Users/soso/leetcode', 
    '/Users/soso/leetcode/1. basic fishc/chapter 16/aircraft', 添加的其他Sources Root
    '/Users/soso/leetcode/4. basic other practice/00-Backup', 
    '/Users/soso/leetcode/1. basic fishc/chapter 13', 
    '/opt/anaconda3/lib/python37.zip', 
    '/opt/anaconda3/lib/python3.7', 
    '/opt/anaconda3/lib/python3.7/lib-dynload', 
    '/opt/anaconda3/lib/python3.7/site-packages',  各种安装的第三方包路径
    '/opt/anaconda3/lib/python3.7/site-packages/aeosa']

"""
# 可以手动添加搜索路径, 添加后导入包的时候就不用加这部分了
sys.path.append('/Users/soso/leetcode/1. basic fishc/chapter 13/libs')
import tool as t
# 如果这里不添加搜索路径, 最近的事chapter 13, 那么就得import libs.tool as t这么写了
t.f()