# -*- coding: utf-8 -*-
# Author: Cynhia

"""
    字符串str
    之所以要和list, tuple放到一起讲, 是因为list, tuple里的很多方法str也支持
    更确切地讲, str更类似于tuple, 其内容不可改变
"""

a = "abc"
print(a)
a[1] = "x"
print(a)