# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    模块和import语句
    默认情况下, python会将abs, max, list等加到内置命名空间中, 可以直接访问到
    但全部加进来显然不现实, 更多的标识符会放在模块中, 比如math里的sin等
    通过import可以手动将模块中的一些内容载入当前命名空间
"""

from math import sin  # 导入模块中的部分标识符
print(sin(3))

from math import *  # 导入模块中的全部标识符, 慎用, 可能导致命名冲突
print(cos(3))

import math
print(math.tan(1))  # 比较保险的做法, 控制导入的标识符范围

import math as mt  # 个别模块名比较长, 可以给简称
print(mt.sin(1))

from libs.utils import f
f()

"""random模块"""
# random模块, 实际上是伪随机的, 其下一个数字生成是基于最近选择的数和一些额外参数
# 可以手动指定初始的数字, 即seed, 该初始数字得是可hash的
# 为了达到相对强随机的效果, 可以把当前时间作为初始数字
import random
import time
random.seed(100)
print(random.random())  # 无参数, 返回开区间(0.0, 1.0)内的小数
random.seed(time.time())
print(random.randint(1, 10))  # 返回闭区间[a, b]内的整数

print(random.randrange(1, 10, 3))  # 返回闭区间[a, b]内以step为间隔的整数, 这里相当于1, 4, 7, 10随机

print(random.choice([8, 1.1, 100, 'a']))  # 给定随机范围

l = [1, 2, 100, -1, 8]
random.shuffle(l)  # shuffle比较特殊, 不是随机数, 而是洗牌, 打乱序列的顺序, 可变有序序列就一个list吧
print(l)

"""其它与数据结构和算法相关的模块"""
# 1. array
# 自带的, 不是numpy里的array, 它与list类似, 但要求成员同类型(占用空间大小相同), 从而搜索等更高效
# list其实是链表, 元素存储的是指针; array才是最基础的顺序存储数组
import array
print(array.typecodes)  # bBuhHiIlLqQfd
a = array.array("i", [1, 2, 3])
print(a, a.typecode, len(a), a.itemsize, a.buffer_info())
# itemsize是单个元素占用的空间大小; 其他append, count什么的类似list

# 2. collections
# 定义额外的数据结构, 以提供dict, list, set, tuple的替代选择
from collections import *

# 2.1 dict的子类Counter, 提供了可哈希对象的计数功能
x = Counter("hello world")
print(x)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
x = Counter(a=1, b=2, c=3)
print(x)  # Counter({'c': 3, 'b': 2, 'a': 1})
x = Counter({"a":1, "b": 2, "c": 3})
print(x)  # Counter({'c': 3, 'b': 2, 'a': 1})
x = Counter(["a", "b", "a", "x", "a"])
print(x)  # Counter({'a': 3, 'b': 1, 'x': 1})
# 可以看出, Counter参数可以直接是计数字典, 也可以是iterable, 后者会自动计数转换成计数字典
# 灵活用法
print(Counter("hello world hahah hello".split(" ")))  # 就变成了统计单词而不是单个字符

# 2.2 defaultdict, 当然, 用原始dict也可以实现
x = dict()
print(x.get("a", 100))
x = defaultdict(int)
print(x['a'])  # 0, 返回对应类型的空类型
x = defaultdict(lambda: 8)
print(x['a'])
print(x)  # 访问过一次之后, 'a'就进到key里了

# 2.3 OrderedDict
# 保留添加时的位置, 修改值不会改变原顺序
x = OrderedDict(a=1, b=2, c=3)  # 几种初始化方法同dict
print(x)
x['d'] = 4
x['a'] = 8
print(x)  # OrderedDict([('a', 8), ('b', 2), ('c', 3), ('d', 4)])
# 猜测OrderedDict直接存的dict的items()形式[(xx, xx), (xx, xx)]

# 2.4 namedtuple
# 看着像类呢, 或者说c++里的Struct
class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

h = Human('Tom', 18, 180)
print(h.age, h.height)

Struct = namedtuple('Human2', ('name', 'age', 'height'))
h2 = Struct(name='lucy', age=18, height=166)
print(h2)  # 一般其概况下, 前面的Struct和后面的'Human2'会起同一个名字

# 2.5 deque, 双向队列, 初始化调用append, 所以是从左到右的
# deque支持线程安全
# 对于插入来讲, deque优于list的是从左侧插入, 复杂度变为O(1)
# deque可以设定最大长度, 超出后一侧插入, 另一次pop
d = deque([8, 9, 10], maxlen=5)
print(d)
d.appendleft(11)
print(d)
d.append(12)
print(d)  # deque([11, 8, 9, 10, 12], maxlen=5)
d.appendleft(100)
print(d)  # deque([100, 11, 8, 9, 10], maxlen=5)
d.clear()
print(d)

# 2.6 ChainMap
# 将多个字典连接, 注意只是视图, 而非赋值, 原字典修改会反映到ChainMap上
# 感觉这种访问会向父级查找, 增删改只影响最末子级的特性有点像变量的作用域关系
# 至于什么情况下可能有妙用, 暂时还没想到
d1 = {"a": 1, "b": 2}
d2 = {"b": 8, "d": 88}
cm = ChainMap(d1, d2)  # ChainMap是appendleft, 靠左的是子(新), 靠右的是老
print(cm)  # ChainMap({'a': 1, 'b': 2}, {'b': 8, 'd': 88})
print(cm['a'], cm['d'])  # 1, 88
cm['d'] = 1000
print(cm)  # ChainMap({'a': 1, 'b': 2, 'd': 1000}, {'b': 8, 'd': 88})
# 可以看出来, 取值时可以按子->父->父的路径查找, 但赋值时只能赋给/修改最左的子字典
print(cm.parents)  # ChainMap({'b': 8, 'd': 88})
cm2 = cm.new_child({"e": 100})  # 添加新的child好像没法直接在原ChainMap上改
print(cm2)  # ChainMap({'e': 100}, {'a': 1, 'b': 2, 'd': 1000}, {'b': 8, 'd': 88})
print(cm2.maps[2]['d'])  # 除了一级一级parents去找, 还可以直接根据索引获取到父级dict


# 3. copy
import copy
d = {"a":[1, 2, 3]}
d2 = copy.copy(d)  # 浅拷贝, d2变成{"a":[1, 2, 3]}, 这里的[1, 2, 3]和d的是同一个
d["a"][2] = 1000
print(d2)  # {'a': [1, 2, 1000]}

d3 = copy.deepcopy(d)
d["a"][0] = -8  # 深拷贝下, d对[1, 2, 1000]的修改不会反应到d3上面
print(d, d2, d3)  # {'a': [-8, 2, 1000]} {'a': [-8, 2, 1000]} {'a': [1, 2, 1000]}

# 4. heapq, 基于堆的优先队列
# 貌似没有完全给封装好, 需要额外给定一个list
# 且不支持大顶堆, 也不支持自定义比较函数
# 不是特别好使, 建议自己再做一层封装
import heapq
# 构建一个堆, 可以从0开始构建
heap = []
heapq.heappush(heap, 123)
heapq.heappush(heap, 8)
heapq.heappush(heap, -1)
heapq.heappush(heap, 22)
print(heap)  # [-1, 22, 8, 123], 小顶堆
print([heapq.heappop(heap) for _ in range(len(heap))])

# 也可以给定一个非空list, 转化成堆顺序
heap = [123, 8, -1, 22]
heapq.heapify(heap)
print([heapq.heappop(heap) for _ in range(len(heap))])

# 5. math, 常见的数学常数和函数
import math
print(math.pi)
print(math.sin(3))
print(math.log(4, 2))

# 6. os, 提供与操作系统底层交互
import os
"""
os.remove(path/filename)删除文件
os.rename(old, new)重命名文件
os.walk()遍历
os.chdir(dirname)改变目录

"""

# 7. sys, 提供了与python解释器交互, 用于操控python的运行时环境