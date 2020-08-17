# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    跟定一个英文句子, 删除所有标点符号
    不知道有多少标点, 反向思考, 非小写大写字母和空格的都过滤掉
"""

import re

s = "Let's try, Mike."

s = re.sub(r"[^a-zA-Z ]", "", s)  # [^xxx]表示匹配不在枚举里的
print(s)