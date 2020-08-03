# -*- coding: utf-8 -*-

# Author: Cynthia
import time
from datetime import datetime
from datetime import date
"""
    Python的设计哲学, 优雅、明确、简单
    用一种方法, 最好只用一种方法来做一件事, 最好使用现成的模块(标准库或者PyPI里的优秀三方库)
    Python官方文档构成:
    1. What's new in Python 3.8?
    This article explains the new features in Python 3.8, compared to 3.7.
    2. Tutorial
    很简易的教程
    3. Library Reference, Python官方枕边书, 唯一需要重点看的
    Python所有的内置函数和标准库的各个模块
    4. Language Reference
    讨论Python的语法和设计哲学
    5. Python Setup and Usage
    如何安装和使用Python
    6. Python HOWTOs
    一些特定主体的深入探讨区
    7. Installing Python Modules
    如何安装第三方包
    8. Distributing Python Modules
    如何发布自己的包
    9. Extending and Embedding
    介绍如何用C和C++开发Python的扩展模块
    10. Python/C API
    10相当于9相当于3对于2
    11. FAQs, 常见问题解答
    12. 去文档里搜一个timeit模块, 学会

"""
import sys
print(sys.path)
# 00-Backup/00-Packaging PKG里打完包, 上传到PyPI, 用pip命令安装后这里就能导入了
import hellopy.utils.tool as ut
ut.f()
import hellopy.opts.const as oc
print(oc.lines)
import hellopy.hello as hh
hh.f()

# timeit, 用于测试小段代码的执行时间
import timeit
print(timeit.__doc__)  # __doc__只打印模块头部的描述信息
print("**************************")
print(dir(timeit))  # dir打印模块的属性列表
print(timeit.__all__)  # __all__用于控制from xx import *这种导入方式导入的内容范围, 不指定则导入全部
# 不是所有模块都有__all__; 如果有, 那么用from xx import * 只会导入__all__里的定义的东西
print(timeit.__file__)  # 包所在的位置
help(timeit)  # 比__doc__里的多, 除了头部描述, 还有整个结构

def f():
    l = [i**2 for i in range(10000)]

s = timeit.timeit(stmt="f()", setup="from __main__ import f", number=10)
# number表示一次测验中stmt代码运行几次
print(s)
s = timeit.repeat(stmt="f()", setup="from __main__ import f", number=10, repeat=3)
# 相对于timeit, repeat多了个repeat参数, 表示重复测试几次, 相应地返回值也是个list
print(s)

s = timeit.timeit(stmt=f, number=20)  # stmt参数不用非得是代码字符串, 也可以直接是函数名
print(s)  # 然后setup="from __main__ import f"这句话, 如果stmt给的是函数名则不用, 如果是字符串, 得有

# 进一步, 带参数的函数怎么传参
# 方式1, 推荐这种方式
def f(x, y):
    print(time.time())

s = timeit.timeit(stmt=lambda : f(3, 4), number=3)
print(s)

# 方式2, 这种情况要有setup="from __main__ import f"
s = timeit.timeit(stmt="f({}, {})".format(3, 4), setup="from __main__ import f", number=3)
print(s)

# 方式3, 直接写函数主体代码
s = timeit.timeit(stmt="print(datetime.now(), date.today())",
                  setup="from datetime import datetime; from datetime import date", number=3)
print(s)

# 总结
# stmt给函数名, 自带上下文, 不用import什么的
# stmt给f()字符串, 但调的还是当前代码中的函数, 函数本身有上下文, 指定setup="from __main__ import f"就行
# stmt给纯字符串, 没有上下文, 所有import都要写一遍, 多个用分号隔开