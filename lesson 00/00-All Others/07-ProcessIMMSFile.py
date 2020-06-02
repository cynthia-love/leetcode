# -*- coding: utf-8 -*-

# Author: bbliu

import os
import re
import pandas
import numpy as np
from threading import Thread
from datetime import datetime
from matplotlib import pyplot as plt
from collections import defaultdict
from sys import exit, argv, path

"""
    python process_imms.py -f MOBS_TRADE_182.252.194.76_mobs_20200509_5.imms -s 202005091938 -e 202005091939 -c AC0000
    也支持: -s 20200509193826 -e 20200509193911, -s 20200509193826864 -e 20200509193911521
"""


# ＂20200509193826＂ -> 1856135921.139
def s2t(s):
    return datetime.strptime(s, "%Y%m%d%H%M%S%f").timestamp()


# 1856135921.139 -> ＂20200509193826＂
def t2s(t):
    return datetime.fromtimestamp(t).strftime("%Y%m%d%H%M%S%f")[:-3]


# 1856135921.139 -> "19:26:26:181"
def tps(t):
    return datetime.fromtimestamp(t).strftime("%H:%M:%S:%f")[:-3]


# 1856135921.139 -> "1856135921.139"
def t2k(t):
    return "{:.3f}".format(t)


# "1856135921.139" -> 1856135921.139
def k2t(k):
    return float(k)


# "1856135921.139" -> "19:26:26:181"
def kps(k):
    return tps(float(k))


# 尖点判断, 大于左右各n个元素
def cmp(l: list, i: int, n: int):
    for k in range(i - 1, max(i - n - 1, -1), -1):
        if l[k] >= l[i]:
            return False
    for k in range(i + 1, min(i + n + 1, len(l)), 1):
        if l[k] >= l[i]:
            return False

    return True


def main():
    filename, time_start, time_end, trancode = None, None, None, None

    for i in range(len(argv)):
        if argv[i] == '-f' and argv[i + 1:]:
            filename = argv[i + 1]

        elif argv[i] == '-s' and argv[i + 1:]:

            if re.match(r"[0-9]{12}$", argv[i + 1]):
                time_start = s2t(argv[i + 1] + "00000")
            elif re.match(r"[0-9]{14}$", argv[i + 1]):
                time_start = s2t(argv[i + 1] + "000")
            elif re.match(r"[0-9]{17}$", argv[i + 1]):
                time_start = s2t(argv[i + 1])
            else:
                print("无效的开始时间！")
                return

        elif argv[i] == '-e' and argv[i + 1:]:

            if re.match(r"[0-9]{12}$", argv[i + 1]):
                time_end = s2t(argv[i + 1] + "59999")
            elif re.match(r"[0-9]{14}$", argv[i + 1]):
                time_end = s2t(argv[i + 1] + "999")
            elif re.match(r"[0-9]{17}$", argv[i + 1]):
                time_start = s2t(argv[i + 1])
            else:
                print("无效的结束时间！")
                return

        elif argv[i] == '-c' and argv[i + 1:]:
            trancode = argv[i + 1]

    # 判断文件是否存在(是个文件)
    if not os.path.isfile(filename):
        print("请输入有效的源文件名")
        return

    if not time_start:
        print("请输入有效的开始时间")
        return

    if not time_end:
        print("请输入有效的结束时间")
        return

    print(time_start, time_end)
    data = pandas.read_csv(filename, sep="|", header=None, usecols=[0, 2, 12],
                           names=["Start", "Trancode", "Duration"], converters=
                           {
                               "Start": lambda x: s2t(x)
                           })

    # 这种一整列的直接计算方式有点像numpy
    data["End"] = data["Start"] + data["Duration"] / 1000
    # 　再加两列转换开始结束时间，　便于肉眼看
    data["Start(format)"] = data["Start"].map(lambda x: tps(x))  # Series自带map
    data = data.reindex(columns=["Start", "Start(format)", "Trancode", "Duration", "End"])
    # 筛选之前存一下原始数据备用
    data_backup = data.copy(deep=True)
    # Pandas的多条件筛选只能用&, 且每个条件得用()括起来, 这点和python原生语法不太一样; 这里是DataFrame而不是Series的筛选
    data = data[(data["Start"] >= time_start) & (data["Start"] <= time_end)]
    if trancode: data = data[data["Trancode"] == trancode]

    data = data.reset_index(drop=True)  # 重置索引从0开始方便后面处理; 涉及个别行被筛掉的情况可以重置行索引
    print(data)

    # ******************************************************************************************************************
    # 画时间-耗时图
    plt.figure(1, figsize=(12, 12 * 0.618))
    plt.title("Time-Consuming(ms)" if not trancode else trancode)
    plt.xlabel("Time")
    plt.ylabel("Time-Consuming(ms)")
    plt.plot(range(len(data["Duration"])), data["Duration"])  # 这里的自变量可以不指定

    step = len(data["Start"]) // 10 + 1
    range_x = range(0, len(data["Start"]), step)
    mark_x = [tps(data["Start"][i]) for i in range(0, len(data["Start"]), step)]
    # print(range_x, mark_x)
    plt.xticks(range_x, mark_x)

    # 对于折线图的上顶点加标注，超过一定阙值, 且大于前后10个元素才添加
    t_y = data["Duration"].mean() * 10.0
    for i in range(len(data["Duration"])):
        if data["Duration"][i] >= t_y and cmp(data["Duration"], i, 10):
            plt.annotate(tps(data["Start"][i]), xy=(i, data["Duration"][i]), xytext=(-20, 10),
                         textcoords="offset pixels", color="red")

    # ******************************************************************************************************************
    # 统计时点线程占用情况
    d_count, d_api = defaultdict(int), defaultdict(
        list)  # {"1856135921.139": 1}, {"1856135921.139": ["AC0008", "TD1002"]}
    # min_start, max_end = data["Start"].min(), data["End"].max(), Series自带的min-max函数

    # 遍历每一行, 每一行从开始时间遍历到结束时间, 时间段内的每个时点为键, 并发数+1, 接口名append
    for index, row in data.iterrows():
        # 这里*1000是因为arange只支持两位小数, 按0.001跳步会有问题
        for j in np.arange(int(row["Start"] * 1000), int(row["End"] * 1000), 1):
            # 为了避免精度问题, 统一转化成三位小数的字符串
            key = t2k(j / 1000)
            d_count[key] += 1
            d_api[key].append(row["Trancode"])
    # 把时点-处理接口数元组分别按照时间, 次数排序 [("1856135921.139": 100), ("1856135921.140": 20), ("1856135921.141": 80)]
    l_count_key = sorted(d_count.items(), key=lambda x: k2t(x[0]))

    # 时点处理接口统计图, 也可以理解成同一时点线程占用数
    plt.figure(2, figsize=(12, 12 * 0.618))
    plt.title("Time-Processing APIs")
    plt.xlabel("Time")
    plt.ylabel("Time-Processing APIs")
    plt.plot(range(len(l_count_key)), [x[1] for x in l_count_key])

    step = len(l_count_key) // 10 + 1
    range_x = range(0, len(l_count_key), step)
    mark_x = [kps(l_count_key[i][0]) for i in range(0, len(l_count_key), step)]
    # print(range_x, mark_x)
    plt.xticks(range_x, mark_x)
    # 对于折线图的上顶点加标注，超过一定阙值, 且是尖点才加
    t_y = 50
    for i in range(len(l_count_key)):
        # 只是大于左右两边一格, 标记密度太大, 控制大于前后10格试试
        if l_count_key[i][1] >= t_y and cmp([x[1] for x in l_count_key], i, 10):
            plt.annotate(kps(l_count_key[i][0]), xy=(i, l_count_key[i][1]), xytext=(-20, 10),
                         textcoords="offset pixels", color="red")

    #   画完图, 打印几个排名靠前的时点, 由于粒度到毫秒级, 多打印点
    #   按并发数排序，　[("1856135921.185": 2000), ("1856135921.001": 1986), ("1856135921.141": 1800)]
    l_count_value = sorted(d_count.items(), key=lambda x: x[1], reverse=True)
    print("并发处理接口数量最多的前100个时点分别为：")  # 由于时间粒度太小, 多打印点
    for i in range(0, 100, 4):
        print(kps(l_count_value[i][0]), l_count_value[i][1], kps(l_count_value[i + 1][0]), l_count_value[i + 1][1],
              kps(l_count_value[+2][0]), l_count_value[i + 2][1], kps(l_count_value[i + 3][0]), l_count_value[i + 3][1])

    # 开一个线程去分析具体时点
    class Analyse(Thread):
        def __init__(self, d_count, d_api, l_count_key, l_count_value, time_start, time_end):
            Thread.__init__(self)
            self.d_count = d_count  # 字典, 时点:　并发数
            self.d_api = d_api  # 字典, 时点: 在处理接口列表
            self.l_count_key = l_count_key  # [(时点: 并发数)], 按时点升序
            self.l_count_value = l_count_value  # # [(时点: 并发数)], 按并发降序
            self.time_start = time_start
            self.time_end = time_end

        def run(self):

            while True:

                print("*********************************************************************")
                ts, te = None, None
                time = input("请输入待分析时间点YYYYMMDDHHMM[SS][MMM]：").strip()
                if re.match(r"[0-9]{12}$", time):
                    ts, te = s2t(time + "00000"), s2t(time + "59999")
                elif re.match(r"[0-9]{14}$", time):
                    ts, te = s2t(time + "000"), s2t(time + "999")
                elif re.match(r"[0-9]{17}$", time):
                    ts = te = s2t(time)
                else:
                    print("无效的时间输入！")
                    continue
                dis = float(input("请输入额外前向时间跨度, 单位S, 可小数指定MS: "))
                ts = ts - dis

                if ts < self.time_start or te > self.time_end:
                    print("不在有效分析时间区间!")
                    continue
                else:
                    print("分析时间区间为: [{}, {}]".format(tps(ts), tps(te)))

                result_count, result_apis = 0, []  # 时间段加总, 28127, ["AC0000", "AB1852", "TP1001"]
                for key in self.d_count.keys():
                    if ts <= k2t(key) <= te:
                        result_count += self.d_count[key]
                        result_apis.extend(self.d_api[key])
                print("1. 区间内总并发数 (以MS为粒度, 加总线程占用数): {}".format(result_count))
                print("2. 接口占用情况为 (以MS为粒度, 加总单个接口的线程占用数): ")
                d_api_dis = defaultdict(int)  # {"AC0000": 30, "TP1001": 100}
                for item in result_apis:
                    d_api_dis[item] += 1

                l_api_dis = d_api_dis.items()
                l_api_dis = sorted(l_api_dis, key=lambda x: x[1], reverse=True)  # ［("TP1001", 100), ("AC0000", 30)]
                print(l_api_dis[:min(5, len(l_api_dis))])

                for i in range(min(5, len(l_api_dis))):
                    l_count_api = []  # 借助{"1856135921.139": ["AC0008", "TD1002"]}, 晒出来单个接口的数量
                    trancode_tmp = l_api_dis[i][0]
                    for key, count in l_count_key:  # 这里枚举的时候尽量不要直接用字典的keys(), 避免无序的情况, 也可以用, 完事再排序
                        if ts <= k2t(key) <= te:
                            l_count_api.append((key, d_api[key].count(trancode_tmp)))
                            # [("1856135921.139", 10), ("1856135921.140", 18)] 单个接口的并发数, 按时点升序
                    file_tmp = "draw{}.npz".format(str(i))
                    # savez可以存储多个变量, 注意这里的x=, y=不要省, 后面读的时候可以直接用这俩key去对应变量
                    # draw.py是公共画图代码, x直接传要显示的东西, 字符串list(坐标上的tick), y传值
                    np.savez(file_tmp, x=[kps(x[0]) for x in l_count_api], y=[x[1] for x in l_count_api])
                    # start可以新启动一个命令行执行, 否则会阻塞主程序; /b表示不显示命令行黑框
                    # draw.py的第一个参数为存储数据的文件名, -x为x数组名, -y为y数组名, -t为title
                    # -pt为均值几倍认为是尖点, -pc为大于前后各几个元素认为是尖点
                    os.system("start /b python draw.py {} -x {} -y {} -t {} -xl {} -yl {} -pt {} -pc {}".
                              format(file_tmp, "x", "y", trancode_tmp + "-Threads", "Time", "Threads", "3", "1"))

    thread_a = Analyse(d_count, d_api, l_count_key, l_count_value, time_start, time_end)
    thread_a.setDaemon(True)
    thread_a.start()

    plt.show()


if __name__ == "__main__":
    main()
