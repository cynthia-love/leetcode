# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    lambda表达式, 一种精简的函数书写方式
    结合filter和map用, 强的一匹
"""

l = lambda x, y, z: x+y+z  # 冒号隔开, 左边参数, 右边返回值
print(l(1, 2, 3))

# lambda在filter中的应用
# filter有俩参数, 第一个是过滤条件, 第二个是列表
# 如果过滤条件不指定, 则默认过滤值为True的
x = [1, 2, 3, -1, -2, 0, 0, 8]
x_f = list(filter(None, x))  # 就把俩0过滤掉了
print(x_f)
# 也可以显式指定过滤条件
x_f = list(filter(lambda x: x > 0, x))
print(x_f)  # [1, 2, 3, 8]

# lambda在map中的应用; filter是过滤掉某些元素, 而map则是按照一定规则批量映射
x_m = list(map(lambda i: i**2, x))
print(x_m)

# 注意, filter和map都可以通过列表推导式实现
ll = [1, 2, 3, 4, 5]
print([x+1 for x in ll])  # map
print([x for x in ll if x > 2])  # filter
print([x+1 for x in ll if x > 2])  # filter+map
print([x+1 if x < 4 else x+100 for x in ll if x > 2])  # [4, 104, 105]
# !!! 上面这个一定记好了, filter+条件map, 外层的if是filter, 内层的if是条件map

# 集合推导式
ss = {1, 2, 3, 4, 5}
print({x + 1 if x < 4 else x+100 for x in ss if x > 2})  # {104, 105, 4}

# 字典推导式
dd = {"a":1, "b": 2, "c": 3, "d": 4, "e": 5}
print({k: v+1 for k, v in dd.items() if v > 2})  # 字典推导只能实现filter和普通map, 无法条件map
print(dict([(k, v+1) if v < 4 else (k, v+100) for k, v in dd.items() if v > 2]))
# 字典推导不能直接实现条件map, 主要是:不好处理, 可以借助dict([(k, v)]过渡一下, 实现filter+条件map
# !!! 经进一步研究, 其实是支持的, 只不过写法比较特殊, k和v的条件map是:隔开的
print({(k+"hahah" if k == "d" else k):(v+1 if v >= 4 else 8) for k,v in dd.items() if k!='e' and v >= 3})
# 好好研究这句话的写法, 当然:前后的俩括号都是可以省略的, 加上格式更清晰些
# {key值条件map:value值条件map for key,value in dict.items() if key值条件 and/or value值条件}

# 字符串没有推导式
# 元组也没有, 不过其可以作为in的对象, 得到list后再通过join(), set()等转成字符串, 元组
tt = (1, 2, 3, 4, 5)
print((x for x in tt))  # 得到的并不是个元组, 而是个generator
print(x for x in tt)  # 和上面输出一样, 说明()并不是必须
# 既然是生成器那就可迭代, 所有需要可迭代对象的地方可以直接写, 除非真的涉及优先级问题才加()
for i in (x for x in tt):
    print(i)  # 当然这里没太必要

print(list(x for x in tt))  # 这里也没啥必要, 直接list(tt)不行吗
# 除非没法直接用tt???需要filter+条件map???
print(list(x+1 if x < 4 else x+100 for x in tt if x >2))
ss = sum(x+1 if x < 4 else x+100 for x in tt if x > 2)
print(ss)
# 其实由这里可以看出来, 前面的列表, 集合, 字典推导式其实内部得到是一个generator
# 然后用[], {}, {}去强制转化成了list, set, dict
# [x for x in tt]等价于list(x for x in tt), 即[]等价于list()
# 即[generator], list(generator)