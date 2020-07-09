# -*- coding: utf-8 -*-

# Authro: Cynthia

"""
    自动从cq平台拉取有效数据
"""
from util.post import CQPost
from util.other import getRealPath, getDesktopPath
from util.other import strUtcTimeToLocalDate, strDateToDate, disDay
from util.other import len_cell

from os import path as os_path
from re import match
from collections import defaultdict
from requests import Session
from base64 import b64encode
from sys import exit, argv, path
from threading import Thread
import pandas as pd
from collections import defaultdict
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from json import dumps as json_dumps, loads as json_loads
from pickle import dump as pickle_dump, load as pickle_load
from numpy import std, hstack, save as numpy_save, load as numpy_load

def main():

    login_name, login_password, year = None, None, None
    year_current, today = datetime.now().strftime("%Y"), datetime.now().date()

    for i in range(len(argv)):

        if argv[i] == '-y' and argv[i + 1:]:
            if match(r"^[0-9]{4}$", argv[i + 1]):
                year = argv[i+1]
            else:
                print("无效的考核年度！")
                return
        elif argv[i] == '-n' and argv[i + 1:]:
            login_name = argv[i + 1]
        elif argv[i] == '-p' and argv[i + 1:]:
            login_password = argv[i + 1]

    url_login_info = getRealPath("login_info_cq.npy")

    if login_name and login_password:
        numpy_save(url_login_info, [login_name, login_password])
    else:
        try:
            login_name, login_password = numpy_load(url_login_info)
        except:
            print("首次使用，请设置登录信息：-n 用户名 -p 密码！")
            return

    cq_post = CQPost()
    cq_post.login(login_name, login_password)



    # 开始读取excel
    url_seed, url_target = getRealPath("seed.xlsx"), getDesktopPath("部门需求看板.xlsx")
    seed = pd.read_excel(url_seed).fillna("", inplace=False)
    groups = [seed.iloc[x, 0] for x in range(len(seed))]
    members = [[y for y in seed.iloc[x, 1].split("|") if y] for x in range(len(seed))]
    members_set = set([x for y in members for x in y])
    if sum([len(x) for x in members]) > len(members_set):
        print("成员列存在重复配置的项, 请检查seed文档!")
        return

    groups.append("其它")
    members.append([])

    # 每一列数据的写入具有同质性, 独立个函数出来
    def write_col(worksheet, index, head, col, format_head, format_cell):
        worksheet.set_column(index, index, max(len_cell(head), *[len_cell(x) for x in col]))
        worksheet.write(0, index, head, format_head)
        worksheet.write_column(1, index, col, format_cell)

    with pd.ExcelWriter(url_target) as writer:
        df, workbook = pd.DataFrame(), writer.book
        format_head = workbook.add_format({'bold': True, 'bg_color': '#00CD66', 'border': 1, 'align': 'left'})
        format_cell = workbook.add_format({"text_wrap": True, 'align': 'left', 'valign': "vcenter"})

        # **************************************************************************************************************
        # 处理实时数据, 先拉取
        cq_tmp = cq_post.pullCQ()
        cq_temp_dict = defaultdict(list)
        if cq_tmp['resultSetData']['rowData']:
            for item in cq_tmp['resultSetData']['rowData']:
                item['提出日期'] = strUtcTimeToLocalDate(item['提出日期'])
                item['计划更新UAT日期'] = strUtcTimeToLocalDate(item['计划更新UAT日期'])
                item['计划投产日期'] = strDateToDate(item['计划投产日期'])
                item['标准功能点数'] = float(item['标准功能点数'])
                cq_temp_dict[item['owner']].append(item)

        members[-1] = [x for x in cq_temp_dict.keys() if x not in members_set]
        df.to_excel(writer, index=False, header=False, sheet_name="实时统计")
        worksheet = writer.sheets['实时统计']

        xls = []
        # 处理column-项目组
        head, col = "项目组", groups
        xls.append([head, col])

        # 处理column-成员
        head, col = "成员", ['\n'.join(x) for x in members]
        xls.append([head, col])

        # 第三列以后都需要用到分组cq信息, 构建一次就行了
        cqs = [hstack([cq_temp_dict[y] for y in x]) if x else [] for x in members]

        # 处理column-当前CQ单总数, 不包括驳回存档关闭
        head, col = "未关闭总数", [len(x) for x in cqs]
        xls.append([head, col])

        # 处理column-在开发CQ单总数
        state = {"等待开发", "正在开发", "等待安装SIT", "等待同步安装SIT", "等待SIT测试", "等待安装", "等待同步安装"}
        head, col = "开发阶段", [len([y for y in x if y['State'] in state]) for x in cqs]
        xls.append([head, col])

        # 处理column-在测试CQ单总数
        state = {"等待检测", "正在检测", "等待同步检测"}
        head, col = "测试阶段", [len([y for y in x if y['State'] in state]) for x in cqs]
        xls.append([head, col])

        # 处理column-等待投产CQ单总数
        state = {"等待投产"}
        head, col = "等待投产", [len([y for y in x if y['State'] in state]) for x in cqs]
        xls.append([head, col])

        # 处理column-等待审核CQ单总数
        state = {"等待审核"}
        f_v = lambda x: x['问题编号']+'-'+x['owner.fullname']
        f_if = lambda x: x['State'] in state
        head, col = "等待审核", ["\n".join([f_v(y) for y in x if f_if(y)]) for x in cqs]
        xls.append([head, col])

        # 处理column-涉及功能点总数
        head, col = "总功能点", [int(sum([y['标准功能点数'] for y in x])) for x in cqs]
        xls.append([head, col])

        # 处理column-均功能点
        head, col = "均功能点", [int(sum([y['标准功能点数'] for y in cqs[i]])/len(members[i]) if members[i] else 0) for i in range(len(cqs))]
        xls.append([head, col])

        # 处理column-当天更新UAT, 不考虑等待审核的
        state = {"等待开发", "正在开发", "等待安装SIT", "等待同步安装SIT", "等待SIT测试", "等待安装", "等待同步安装"}
        f_v = lambda x: x['问题编号']+'-'+x['State']+"-"+x['owner.fullname']
        f_if = lambda x: x['计划更新UAT日期'] == today and x['State'] in state
        head, col = "待更新UAT", ["\n".join([f_v(y) for y in x if f_if(y)]) for x in cqs]
        xls.append([head, col])

        # 处理column-超期未更新UAT; 不考虑等待审核的; 这里的算法需要换一下, 目前统计的只是
        # 昨天及以前应该更新uat但没更新的, 而不是所有超期的(比如虽然翻了, 但是翻晚了)
        state = {"等待开发", "正在开发", "等待安装SIT", "等待同步安装SIT", "等待SIT测试", "等待安装", "等待同步安装"}
        f_v = lambda x: x['问题编号']+'-'+disDay(x['计划更新UAT日期'], today)+"天"+'-'+x['owner.fullname']
        f_if = lambda x: x['计划更新UAT日期'] < today and x['State'] in state
        head, col = "UAT逾期", ["\n".join([f_v(y) for y in x if f_if(y)]) for x in cqs]
        xls.append([head, col])

        for i in range(len(xls)):
            write_col(worksheet, i, xls[i][0], xls[i][1], format_head, format_cell)



        # **************************************************************************************************************
        # 把实时CQ详情也存一个sheet, 便于查找
        df.to_excel(writer, index=False, header=False, sheet_name="实时CQ单汇总")
        worksheet = writer.sheets['实时CQ单汇总']

        # **************************************************************************************************************
        # 处理本年累计, 先拉取

        cq_year_current = cq_post.pullCQYear(year_current)
        cq_year_current_dict = defaultdict(list)
        if cq_year_current['resultSetData']['rowData']:
            for item in cq_year_current['resultSetData']['rowData']:
                item['提出日期'] = strUtcTimeToLocalDate(item['提出日期'])
                item['计划更新UAT日期'] = strUtcTimeToLocalDate(item['计划更新UAT日期'])
                item['计划投产日期'] = strDateToDate(item['计划投产日期'])
                item['标准功能点数'] = float(item['标准功能点数'])
                cq_year_current_dict[item['owner']].append(item)

        df.to_excel(writer, index=False, header=False, sheet_name=year_current+"年累计")
        worksheet = writer.sheets[year_current+"年累计"]


        # **************************************************************************************************************
        # 处理输入的年累计, 先拉取
        if year:

            cq_year = cq_post.pullCQYear(year)
            cq_year_dict = defaultdict(list)
            if cq_year['resultSetData']['rowData']:
                for item in cq_year['resultSetData']['rowData']:
                    item['提出日期'] = strUtcTimeToLocalDate(item['提出日期'])
                    item['计划更新UAT日期'] = strUtcTimeToLocalDate(item['计划更新UAT日期'])
                    item['计划投产日期'] = strDateToDate(item['计划投产日期'])
                    item['标准功能点数'] = float(item['标准功能点数'])
                    cq_year_dict[item['owner']].append(item)

            df.to_excel(writer, index=False, header=False, sheet_name=year+"年累计")
            worksheet = writer.sheets[year+'年累计']









if __name__ == "__main__":
    main()