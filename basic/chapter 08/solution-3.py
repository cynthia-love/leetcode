# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    python默认文件操作只能读写字符串/二进制
    如果想比较方便地读取数字类型, 读写python对象等, 可以用pickle模块
    pickle模块读写需要用二进制形式
"""

x = {
    "a": 1,
    "b": 2
}

import pickle

with open("data/data.pickle", "wb") as f:
    pickle.dump(x, f)

with open("data/data.pickle", "rb") as f:
    m = pickle.load(f)
    print(m, type(m))