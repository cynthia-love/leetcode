# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import sys
import pickle
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as ticker
from datetime import datetime

def getpath(filename) -> str:
    if sys.path[0].endswith(".zip"):
        return str.replace(sys.path[0], "base_library.zip", filename)
    else:
        return sys.path[0] + "\\" + filename


trancode, date_present, date_base = None, None, None

# imms专属画图工具, 没必要校验那么多东西了
for i in range(len(sys.argv)):
    if sys.argv[i] == '-trancode' and sys.argv[i + 1:]:
        trancode = sys.argv[i + 1]
    elif sys.argv[i] == '-cd' and sys.argv[i + 1:]:
        date_present = sys.argv[i + 1]
    elif sys.argv[i] == '-td' and sys.argv[i + 1:]:
        date_base = sys.argv[i + 1]

print(trancode, date_present, date_base)
with open(getpath("plot.pickle"), "rb") as f:
    present, base = pickle.load(f)

plt.figure(1, figsize=(18, 11), dpi=80)
plt.suptitle(trancode, fontsize=15, fontweight="bold", color='blue', y=0.95)  # 设置多个子图的总标题

plt.subplot(311)
plt.plot([e[0] for e in present], [e[1] for e in present], color='lime', label=date_present)
plt.plot([e[0] for e in base], [e[1] for e in base], color='darkgray', label=date_base)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.legend(loc='upper right')  # 没这行折线label不会出来

# 注意, 分析时段和基准时段的日期这里得置成一样, 不然即使只显示时间, pyplot还是认为是不同的横坐标
plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
# 这里横坐标密度是自动的, 可以关闭默认横坐标, 用plt.xticks()去手动画, 也可以用set_major_locator()去设置间隔
plt.gca().xaxis.set_major_locator(dates.HourLocator(byhour=None, interval=2))
# 设置横坐标上下限; 还有个函数plt.axis([xmin, xmax, ymin, ymax])一次把横纵坐标都设置了
plt.xlim(datetime(1900, 1, 1, hour=0, minute=0), datetime(1900, 1, 2, hour=0, minute=0))

plt.subplot(312)
plt.plot([e[0] for e in present], [e[2] for e in present], color='lime', label=date_present)
plt.plot([e[0] for e in base], [e[2] for e in base], color='darkgray', label=date_base)
plt.xlabel("Time")
plt.ylabel("Success")
plt.legend(loc='lower right')

# 注意, 分析时段和基准时段的日期这里得置成一样, 不然即使只显示时间, pyplot还是认为是不同的横坐标
plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
# 这里横坐标密度是自动的, 可以关闭默认横坐标, 用plt.xticks()去手动画, 也可以用set_major_locator()去设置间隔
plt.gca().xaxis.set_major_locator(dates.HourLocator(byhour=None, interval=2))
# 设置横坐标上下限; 还有个函数plt.axis([xmin, xmax, ymin, ymax])一次把横纵坐标都设置了
plt.xlim(datetime(1900, 1, 1, hour=0, minute=0), datetime(1900, 1, 2, hour=0, minute=0))

# 成功率比较特殊, 纵坐标也得特殊处理
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: "{:.0%}".format(x)))
plt.ylim(bottom=0.0)  # 可以只设置下限bottom, 也可以加上上限top

plt.subplot(313)
plt.plot([e[0] for e in present], [e[3] for e in present], color='lime', label=date_present)
plt.plot([e[0] for e in base], [e[3] for e in base], color='darkgray', label=date_base)
plt.xlabel("Time")
plt.ylabel("Duration")
plt.legend(loc='upper right')

# 注意, 分析时段和基准时段的日期这里得置成一样, 不然即使只显示时间, pyplot还是认为是不同的横坐标
plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
# 这里横坐标密度是自动的, 可以关闭默认横坐标, 用plt.xticks()去手动画, 也可以用set_major_locator()去设置间隔
plt.gca().xaxis.set_major_locator(dates.HourLocator(byhour=None, interval=2))
# 设置横坐标上下限; 还有个函数plt.axis([xmin, xmax, ymin, ymax])一次把横纵坐标都设置了
plt.xlim(datetime(1900, 1, 1, hour=0, minute=0), datetime(1900, 1, 2, hour=0, minute=0))


# plt.gcf().autofmt_xdate()
# 好像加了这句话会把三个子图的横坐标合成一个, 如果不加这句, 那么set_major_formatter什么的得每个子图下执行一次
# 这里的f应该是figure的简写



plt.show()
