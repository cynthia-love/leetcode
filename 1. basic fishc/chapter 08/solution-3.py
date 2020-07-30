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
    s = f.read()
    print(pickle.loads(s))

    f.seek(0, 0)
    m = pickle.load(f)  # pickle.load等价于先读取二进制流, 再用loads把二进制流转回对象
    print(m, type(m))

ps = pickle.dumps([{"a":1, "b":2}, 8])
print(ps)

d, i = pickle.loads(ps)
print(d, i)

# 即pickle除了把对象转成二进制流持久化到文件, 还能仅仅转成二进制流, 不存在文件
# 并提供灵活的dump和dumps从文件中载入对象, 和将二进制流翻译回对象