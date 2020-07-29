# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    其它小工具
"""
from sys import path as sys_path
from os import path as os_path
from datetime import datetime, timedelta, date


def getRealPath(filename: str) -> str:
    if sys_path[0].endswith(".zip"):
        return str.replace(sys_path[0], "base_library.zip", filename)
    else:
        return sys_path[0] + "\\" + filename


def getDesktopPath(filename: str) -> str:
    return os_path.join(os_path.expanduser("~"), 'Desktop') + "\\" + filename


def strUtcTimeToLocalDate(timestr: str) -> date:
    # 解析2019-12-20T03:15:50Z格式的时间
    utc_time = datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%SZ")
    return (utc_time + timedelta(hours=8)).date()


def strDateToDate(datestr: str) -> date:
    # 解析2019-12-20
    return datetime.strptime(datestr, "%Y-%m-%d").date()

def disDay(day1: date, day2: date):
    return str((day1-day2).days) if day1 >= day2 else str((day2-day1).days)

def len_cell(s: str) -> int:
    # 根据字符串计算单元格合适的长度
    # 对于含换行符的字符串, 算子串长度
    f = lambda x: (len(x.encode("utf-8"))-len(x))/2+len(x)
    # 为了防止传入的x不是str类型, 先转一道
    return int(max([f(x) for x in str(s).split("\n")]))
