# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用列表解析语法在不输入所有26个英文字母的情况下产生['a', 'b'...'z']
"""

l = [chr(i) for i in range(97, 123, 1)]
print(l)