# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    第13章 模块
"""

"""
    模块就是程序
    封装的几个级别:
    容器(list等, 是对数据的封装)->函数(对语句的封装)->类(对属性和方法的封装)->模块
    保存的每一个.py都是一个独立的模块
    
    模块的作用: 1. 组织代码更有条理; 2. 代码重用
"""
# 导入方法1, 不推荐
import util  # 同一目录下可直接导入, 不需要当前目录是个package(即没__init__)也行
print(util.x)
util.f()
o = util.C()
o.f()

# 起个别名, 强推
import util as ut
print(ut.x)
ut.f()
o = ut.C()
o.f()

# 容易和当前文件命名冲突, 不建议
from util import C
o = C()
o.f()

# 非同一级目录下的导入, 需要导入目录是package, 即有__ini__.py
import libs.util
print(libs.util.x)
libs.util.f()
o = libs.util.C()
o.f()

# 建议导入方式
import libs.util as u
print(u.x)
u.f()
o = u.C()
o.f()