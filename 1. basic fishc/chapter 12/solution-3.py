# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    descriptor
    猛一看不太好理解, 其实property就是一种descriptor(推荐property写法)
    即descriptor有两种写法:
    1. 老的, 要把get, set, delete单独写到一个类里, 然后在需要用到该变量的类里
    x = 描述符类()
    2. 新的写法, property写法, 不用独立类, 直接在用到该变量的类里写三个函数, 然后
    x = descriptor(get, set, delete)

    还要注意一点, get, set只在descriptor这种特殊场景才有意义, 它和getattribute, getattr
    完全不是一个东西, 后者写到单个类里起到拦截作用, 而get, set写到单个类里一点作用没有
"""
import time

class TimeDes:
    """
        秒表数据类型
        .v = xxx, 赋值, 时间戳
        .v, 访问, 返回: 初始时间戳, 截止时间戳
    """
    def __init__(self):
        self._start = None

    def __set__(self, instance, value):
        self._start = value

    def __get__(self, instance, owner):
        if not self._start:
            raise AttributeError("秒表未启动")
        else:
            now = time.time()
            return self._start, now, now-self._start

class C:
    t = TimeDes()

    def __init__(self):
        self.times = []

    def start(self):
        self.t = time.time()
        self.times.clear()

    def mark(self):
        self.times.append(self.t)

    def stop(self):
        self.t = None

    def __str__(self):
        # time模块的strftime不支持毫秒，datetime模块的支持小数点后6位，毫秒取3位就行
        # datetime.strftime(now, "%Y-%m-%d %H:%M:%S:%f")[:-3]
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.times[0][0]))+"~"+ \
               time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.times[0][1]))+" "+ \
                "{:.3f}".format(self.times[0][2])

c = C()
c.start()
time.sleep(0.018)
c.mark()
c.mark()
c.stop()
print(c)

c.start()
c.mark()
c.stop()
print(c)