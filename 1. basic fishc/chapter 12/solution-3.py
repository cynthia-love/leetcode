# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    定制一个计时器的类
    1. start启动, stop停止
    2. print(实例)显示结果
    3. 未启动时调stop给提示
    4. 两个计时器对象可以相加

    计时器变量有自己独有的特性, 可以抽象成descriptor
    自己写个descriptor类就好, 没必要用property, 还乱
    赋值时取当前时间, 取值时取两者差值
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

