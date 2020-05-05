# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    Python的设计哲学, 优雅、明确、简单
    用一种方法, 最好只用一种方法来做一件事, 最好使用现成的模块(标准库或者PyPI里的优秀三方库)

"""
import sys
print(sys.path)
# chapter 0/01-PKG Packaging里打完包, 上传, 用pip命令安装后这里就能导入了
import hellopy.utils.tool as ut
ut.f()
import hellopy.opts.const as oc
print(oc.lines)
import hellopy.hello as hh
hh.f()