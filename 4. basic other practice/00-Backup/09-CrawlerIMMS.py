# -*- coding: utf-8 -*-
# Author: bbliu

"""

"""
import os
import sys
import copy
from os import system
from threading import Thread
from base64 import b64encode
from re import match
from os.path import isfile
from requests import Session
from pandas import read_csv, read_excel
from sys import exit, argv, path
from collections import defaultdict
from datetime import datetime, timedelta
from json import dumps as json_dumps, loads as json_loads
from pickle import dump as pickle_dump, load as pickle_load


def getpath(filename) -> str:
    if path[0].endswith(".zip"):
        return str.replace(path[0], "base_library.zip", filename)
    else:
        return path[0] + "\\" + filename


def t2s(t):
    return t.strftime("%Y-%m-%d %H:%M")


def s2t(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M")


def main():
    session, base_url = Session(), "http://182.218.155.29:8081"

    # 处理用户输入, 示例:　python imms.py -worse -c "2020-06-29 06:00"
    print("**********************************************************************************************************")
    print("IMMS参数说明: -f 频次阈值, 默认全量 -f2 基准时段频次阈值 -l 分析时长, 默认10 -c 分析时段, 默认上一分钟")
    print("-t 基准时段, 默认上周 -m 打印条数, 默认20 -s 接口文件, 支持csv和xlsx -e 排除接口文件 -n 登录名 -p 秘钥")
    print("-worse, 按交易量增加, 成功率降低, 耗时增加排序 -better 按交易量减少, 成功率增加, 耗时降低排序; 默认混排")
    print("-i 条数, 分析交易量排名前x的接口, 可与-s同步生效; -sys mobs/ecbpin/ecbpout, 指定分析系统, 默认mobs")
    print("-verbose 此参数可以给接口增加更多调用信息, 要保证当前目录有h5_api_all.xlsx, 不能改名, 没有请先执行scan")
    print("如果同时指定-s -e -i -f, 则先提取指定接口, 再去掉要排除的, 再从中选取前x, 再把x个进行低频过滤得到要分析接口")
    print("**********************************************************************************************************")

    login_name, login_password, now = None, None, datetime.now()

    argv_l, argv_c, argv_t, min_freq, max_print, min_freq_old = 10, now, None, 0.0, 20, 0.0

    api_file, apis, api_file_e, apis_e = None, set(), None, set()

    isworse, isbetter = False, False

    isprime = 0

    isverbose = False

    file_verbose = "h5_api_all.xlsx"

    h5_api_all = defaultdict(dict)

    system_process = 'MOBS'

    for i in range(len(argv)):
        if argv[i] == '-l' and argv[i + 1:]:
            s = argv[i + 1]
            if match(r"\d{1,2}", s):
                argv_l = int(s)
            else:
                print("无效的时长！")
                return
        elif argv[i] == '-c' and argv[i + 1:]:
            s = argv[i + 1]
            if match(r"\d:\d\d", s):
                argv_c = s2t(t2s(now)[:11] + '0' + s)
            elif match(r"\d\d:\d\d", s):
                argv_c = s2t(t2s(now)[:11] + s)
            elif match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", s):
                argv_c = s2t(s)
            else:
                print("无效的待比较时间！")
                return
        elif argv[i] == '-t' and argv[i + 1:]:
            s = argv[i + 1]
            if match(r"\d:\d\d", s):
                argv_t = s2t(t2s(now)[:11] + '0' + s)
            elif match(r"\d\d:\d\d", s):
                argv_t = s2t(t2s(now)[:11] + s)
            elif match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", s):
                argv_t = s2t(s)
            else:
                print("无效的基准时间！")
                return
        elif argv[i] == '-f' and argv[i + 1:]:
            s = argv[i + 1]
            if match(r"[0-9]+.?[0-9]*", s):
                min_freq = float(s)
            else:
                print("无效的最低分钟频次！")
                return
        elif argv[i] == '-f2' and argv[i + 1:]:
            s = argv[i + 1]
            if match(r"[0-9]+.?[0-9]*", s):
                min_freq_old = float(s)
            else:
                print("无效的基准时段最低分钟频次！")
                return
        elif argv[i] == '-m' and argv[i + 1:]:
            s = argv[i + 1]
            if match(r"[0-9]+", s):
                max_print = int(s)
            else:
                print("无效的最高打印条数！")
                return
        elif argv[i] == '-n' and argv[i + 1:]:
            login_name = argv[i + 1]
        elif argv[i] == '-p' and argv[i + 1:]:
            login_password = b64encode(argv[i + 1].encode('utf-8')).decode('utf-8')

        elif argv[i] == '-s' and argv[i + 1:]:
            if isfile(argv[i + 1]):
                api_file = argv[i + 1]
            else:
                print("无效的API参照文档！")
                return
        elif argv[i] == '-e' and argv[i + 1:]:
            if isfile(argv[i + 1]):
                api_file_e = argv[i + 1]
            else:
                print("无效的API排除文档！")
                return
        elif argv[i] == '-worse':
            isworse = True

        elif argv[i] == '-better':
            isbetter = True
        elif argv[i] == '-sys' and argv[i + 1:]:
            id = argv[i + 1].upper()
            if id in ['MOBS', 'ECBPIN', 'ECBPOUT']:
                system_process = id
            else:
                print("无效的系统编号！")
                return
        elif argv[i] == '-i' and argv[i + 1:]:
            s = argv[i + 1]
            if match(r"[0-9]+", s):
                isprime = int(s)
            else:
                print("无效的-i参数！")
                return

        elif argv[i] == '-verbose':

            if isfile(file_verbose):
                isverbose = True
            else:
                print("未检测到h5_api_all.xlsx, 无法开启-verbose")
                return


    print("分析系统: ", system_process)
    # 先计算四个时间点, 得到当前时间段, 基准时间段
    if not argv_t: argv_t = argv_c - timedelta(weeks=1)
    time_end, time_start = argv_c - timedelta(minutes=1), argv_c - timedelta(minutes=argv_l)
    base_end, base_start = argv_t - timedelta(minutes=1), argv_t - timedelta(minutes=argv_l)

    time_start, time_end = t2s(time_start), t2s(time_end)
    base_start, base_end = t2s(base_start), t2s(base_end)

    # 读取接口扫描文档
    if isverbose:
        try:
            data = read_excel(file_verbose, usecols=[0, 2, 4, 5, 6], header=None, skiprows=[0])
            # 由于api扫描文档有单元格归并, 这里需要把NaN都填上值

            data[0].fillna(method='ffill', inplace=True)
            data[2].fillna(method='ffill', inplace=True)
            data[5].fillna(value="", inplace=True)
            data[6].fillna(value="", inplace=True)

            data[7] = data[0] + "\\" + data[2] + "\\" + data[4]

            for index, row in data.iterrows():
                h5_api_all[row[7]]['des'] = row[5]
                h5_api_all[row[7]]['api'] = row[6]
            print("详情模式: ", "是")
        except:
            print("接口扫描文档载入失败, 无效的h5_api_all.xlsx!")
            sys.exit(1)

    # 再看看需不需要特殊标记本次涉及的接口
    if api_file:
        if api_file.endswith(".csv"):
            apis = set(read_csv(api_file, usecols=[0], header=None, skiprows=[0])[0].values)
        else:
            apis = set(read_excel(api_file, usecols=[0], header=None, skiprows=[0])[0].values)


    print("指定接口: ", apis if apis else "无")

    if api_file_e:
        apis_e = set(read_excel(api_file_e, usecols=[0], header=None, skiprows=[0])[0].values)

    print("排除接口: ", apis_e if apis_e else "无")
    print("高频过滤: ", "前{}".format(isprime) if isprime else "否")

    # 再处理账户名, 密码
    url_login_info = getpath("login_info.npy")

    if login_name and login_password:
        with open(url_login_info, "wb") as f:
            pickle_dump([login_name, login_password], f)
    else:
        try:
            with open(url_login_info, "rb") as f:
                login_name, login_password = pickle_load(f)
        except:
            print("首次使用，请设置登录信息：-n 用户名 -p 密码！")
            return

    print("分析时间段: {} ~ {}...".format(time_start, time_end))
    print("基准时间段: {} ~ {}...".format(base_start, base_end))
    if min_freq != 0.0:
        print("平均每分钟调用次数小于{:.2f}的接口直接过滤掉, 不参与后续分析...".format(min_freq))

    print("**********************************************************************************************************")

    # 登录获取授权码
    def login(login_name, login_password, base_url) -> str:
        login_url = base_url + "/imms/userLogin.do"
        params = {
            "REQ_HEAD": {"TRAN_PROCESS": "", "TRAN_ID": ""},
            "REQ_BODY": {
                "flag": "login",
                "logSegment": "OA",
                'loginName': login_name,
                "loginPassword": login_password,
                'loginState': "0",
                "logIP": "",
                "userAuthSession": "",
            }
        }

        try:
            return json_loads(session.post(login_url, json_dumps(params)).text)['RSP_BODY']['userAuthToken']
        except:
            print("登陆失败！请检查网络设置或重新配置登录信息：-n 用户名 -p 密码！")
            exit(1)

    print("登录中...")
    userAuthSession = login(login_name, login_password, base_url)

    # 查询, 经测验，1个小时勉强顶得住，再长服务器就返回错误了
    def pull(login_name, userAuthSession, base_url, time_start, time_end, dim) -> list:
        pull_url = base_url + "/imms/qryDimStatisInfo.do"
        # 注意这里params是区分类型的，下面的4如果设置为字符型就查不回来数据
        params = {
            "REQ_HEAD": {"TRAN_PROCESS": "", "TRAN_ID": ""},
            "REQ_BODY": {
                "branchCode": "01315999999",
                "loginName": login_name,
                "userAuthSession": userAuthSession,
                "pageSize": "8",
                "currentPage": "1",
                "startTime": time_start,
                "endTime": time_end,
                "firstDimensionsNo": dim,
                "systemId": system_process,
                "timeType": 4,
                "type": "MX",

            }
        }
        try:
            dimStatisInfoVoList = json_loads(session.post(pull_url, json_dumps(params)).text)['RSP_BODY'][
                'dimStatisInfoVoList']
            if not dimStatisInfoVoList:
                raise Exception("dimStatisInfoVoList empty")
            else:
                return dimStatisInfoVoList
        except:
            print("拉取失败！可能服务器不稳定或时间设置有误，请再次尝试！")
            exit(1)

    print("数据拉取中...")
    # time_host = pull(login_name, userAuthSession, base_url, time_start, time_end, "ip")
    time_data = pull(login_name, userAuthSession, base_url, time_start, time_end, "transCode")
    base_data = pull(login_name, userAuthSession, base_url, base_start, base_end, "transCode")
    print("数据拉取成功...")

    # 按secondDimensionsNo将时间段内的数值加总
    def handle_res(res):
        dict_res = defaultdict(list)
        for item in res:
            if item['secondDimensionsNo'] not in dict_res:
                dict_res[item['secondDimensionsNo']].extend([
                    item['secondDimensionsNo'], item['configDesc'], int(item['tradeCount']),
                    int(item['successTradeCount']), int(item['countTime'])
                ])
            else:
                dict_res[item['secondDimensionsNo']][2] += int(item['tradeCount'])
                dict_res[item['secondDimensionsNo']][3] += int(item['successTradeCount'])
                dict_res[item['secondDimensionsNo']][4] += int(item['countTime'])
        for key in dict_res.keys():
            dict_res[key].extend([dict_res[key][3] / dict_res[key][2], dict_res[key][4] / dict_res[key][2]])
        return dict_res

    # dict_time_host, dict_time_data, dict_base_data = handle_res(time_host), handle_res(time_data), handle_res(base_data)
    dict_time_data, dict_base_data = handle_res(time_data), handle_res(base_data)
    # 把原始数据存起来, 避免处理过程中有丢失
    dict_time_data_back = copy.deepcopy(dict_time_data)
    dict_base_data_back = copy.deepcopy(dict_base_data)

    # -s -e -i参数的关系需要好好理一下, -s和-e的关系简单, 先处理
    # 如果api有, 则会排除不要分析的; 如果api没有, 还是未空set
    apis = set([x for x in apis if x not in apis_e])
    if isprime:
        # apis为空的情况, 要么本来就为空, 要么排除apis_e之后为空, 不管怎样样, 这里再排除一次比较保险
        if not apis:
            apis = set(
                [x[0] for x in sorted(dict_time_data.values(), key=lambda item: item[2], reverse=True) if x[0] not in apis_e][:isprime])
        else:
            # apis不为空的情况, 那么前面肯定已经把apis_e排除了, 所以这里不用再and一个not in apis_e条件
            apis = set(
                [x[0] for x in sorted(dict_time_data.values(), key=lambda item: item[2], reverse=True) if x[0] in apis][:isprime])

    sum1 = sum([x[2] for x in dict_time_data.values()]) / argv_l
    sum2 = sum([x[2] for x in dict_base_data.values()]) / argv_l
    print("分析时段全部接口分均交易量: {:.2f}, 对应基准时段分均交易量: {:.2f}, 增加: {:.2%}".format(sum1, sum2, (sum1 - sum2) / sum2))

    if apis:
        # and dict_time_data[x][2]>= argv_l * min_freq是为了加上-f过滤
        # 感觉-s -e -i -f还是写的有点乱, 到底该怎么写, 设置一个apis_filter, 四个参数来一遍? 得到最终的apis_filter之后再统计交易量什么的
        # 初始apis_filter取全量api, 一遍遍筛
        sum1 = sum([dict_time_data[x][2] for x in dict_time_data if x in apis and dict_time_data[x][2]>= argv_l * min_freq]) / argv_l
        sum2 = sum([dict_base_data[x][2] for x in dict_base_data if x in apis and x in dict_time_data and dict_time_data[x][2]>= argv_l * min_freq]) / argv_l

        if sum2 == 0:
            percent = 0 if sum1 == 0 else 1
        else:
            percent = (sum1 - sum2) / sum2

        print("分析时段指定接口分均交易量: {:.2f}, 对应基准时段分均交易量: {:.2f}, 增加: {:.2%}".format(sum1, sum2, percent))

    len_trancode = max([len(x) for x in dict_time_data.keys()]) + 11

    """
    先不和基准比, 单独分析当前时点情况
    """

    def filter_map(dic, index, reverse=False, isapi=True, ismix=True):
        v_dic_filter = list(filter(lambda x: x[2] >= argv_l * min_freq and x[0] not in apis_e
                                             and (not isapi or x[0] in apis if apis else True), dic.values()))
        return sorted(v_dic_filter, key=lambda x: abs(x[index]) if ismix else x[index], reverse=reverse)

    # v_time_host_succ_order, v_time_host_dura_order = filter_map(dict_time_host, 5, isapi=False), filter_map(dict_time_host, 6, True, isapi=False)

    v_time_data_freq_order = filter_map(dict_time_data, 2, True)
    v_time_data_succ_order, v_time_data_dura_order = filter_map(dict_time_data, 5), filter_map(dict_time_data, 6, True)

    print("**********************************************************************************************************")
    """
    # 先处理当前主机情况, 分别按成功率和耗时排序, 打印出前10
    max_index = min(10, len(v_time_host_succ_order))
    print('1. 均成功率最低的{}台主机为: '.format(max_index))
    print("{0:<14}{1:<12}{2:<12}{3:<12}".format("No", "AvFreq", "SuRate", "AvDura"))
    for i in range(max_index):
        print("{0:<14}{1:<12.2f}{2:<12.2%}{3:<12.2f}".format(v_time_host_succ_order[i][0], v_time_host_succ_order[i][2]/argv_l,
                                                          v_time_host_succ_order[i][5], v_time_host_succ_order[i][6]))

    print("***********************************************")
    print('2. 平均耗时最高的{}台主机为: '.format(max_index))
    print("{0:<14}{1:<12}{2:<12}{3:<12}".format("No", "AvFreq", "SuRate", "AvDura"))
    for i in range(max_index):
        print("{0:<14}{1:<12.2f}{2:<12.2%}{3:<12.2f}".format(v_time_host_dura_order[i][0], v_time_host_dura_order[i][2]/argv_l,
                                                          v_time_host_dura_order[i][5], v_time_host_dura_order[i][6]))

    print("***********************************************")
    """
    print("0. 分析时段相对基准时段新增调用: ")
    print(
        "{0:<{width}}{1:<12}{2:<12}{3:<12}{4:12}{5:12}{6:12}{7:<18}".format("TranCode", "Frequency", "Base", "Success", "Base", "Duration", "Base", "Description",
                                                          width=len_trancode))
    for item in v_time_data_freq_order:
        if item[0] in dict_base_data: continue
        base = dict_base_data[item[0]] if item[0] in dict_base_data else []
        res = []
        res.append('*' + item[0] if item[0] in apis else item[0])
        res.append("{:.2f}".format(item[2] / argv_l))
        res.append("{:.2f}".format(base[2] / argv_l) if base else "-")
        res.append("{:.2%}".format(item[5]))
        res.append("{:.2%}".format(base[5]) if base else "-")
        res.append("{:.2f}".format(item[6]))
        res.append("{:.2f}".format(base[6]) if base else "-")
        res.append(item[1])

        print("{0:<{width}}{1:<12}{2:<12}{3:<12}{4:12}{5:12}{6:12}{7:<18}".format(
            res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], width=len_trancode))
    # 再打印成功率为0的, 然后按成功率和耗时排序, 打印出前10
    print("***********************************************")
    print('1. 分析时段调用成功率为零的全部接口为: ')
    print(
        "{0:<{width}}{1:<12}{2:<12}{3:<12}{4:12}{5:12}{6:12}{7:<18}".format("TranCode", "Frequency", "Base", "Success", "Base", "Duration", "Base", "Description",
                                                          width=len_trancode))
    v_time_data_freq_order_zero = sorted([x for x in v_time_data_succ_order if x[5] == 0.0], key=lambda x: x[2],
                                         reverse=True)
    zero_count = 0
    for item in v_time_data_freq_order_zero:
        if item[5] != 0.0: break
        zero_count += 1

        base = dict_base_data[item[0]] if item[0] in dict_base_data else []
        res = []
        res.append('*' + item[0] if item[0] in apis else item[0])
        res.append("{:.2f}".format(item[2] / argv_l))
        res.append("{:.2f}".format(base[2] / argv_l) if base else "-")
        res.append("{:.2%}".format(item[5]))
        res.append("{:.2%}".format(base[5]) if base else "-")
        res.append("{:.2f}".format(item[6]))
        res.append("{:.2f}".format(base[6]) if base else "-")
        res.append(item[1])
        # 这里先生成res因为有些字段可能为数字可能为字符, 如果放在后面统一format会有问题
        # 只能这么先生成字符串格式的待输出内容, 然后后面直接以字符串格式输出

        print("{0:<{width}}{1:<12}{2:<12}{3:<12}{4:12}{5:12}{6:12}{7:<18}".format(
            res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], width=len_trancode))

    # 把成功率为0的过滤掉, 剩下的再取成功率最低的前10和耗时最高的前十
    v_time_data_succ_order_nozero = list(filter(lambda x: x[5] != 0, v_time_data_succ_order))
    v_time_data_dura_order_nozero = list(filter(lambda x: x[5] != 0, v_time_data_dura_order))
    max_index = min(max_print, len(v_time_data_succ_order_nozero))

    print("***********************************************")
    print('2. 分析时段调用成功率最低的{}个接口为(除零外): '.format(max_index))
    print(
        "{0:<{width}}{1:<12}{2:<12}{3:<12}{4:12}{5:12}{6:12}{7:<18}".format("TranCode", "Frequency", "Base", "Success", "Base", "Duration", "Base", "Description",
                                                          width=len_trancode))
    for i in range(max_index):
        item = v_time_data_succ_order_nozero[i]
        base = dict_base_data[item[0]] if item[0] in dict_base_data else []

        res = []
        res.append('*' + item[0] if item[0] in apis else item[0])
        res.append("{:.2f}".format(item[2] / argv_l))
        res.append("{:.2f}".format(base[2] / argv_l) if base else "-")
        res.append("{:.2%}".format(item[5]))
        res.append("{:.2%}".format(base[5]) if base else "-")
        res.append("{:.2f}".format(item[6]))
        res.append("{:.2f}".format(base[6]) if base else "-")
        res.append(item[1])

        print("{0:<{width}}{1:<12}{2:<12}{3:<12}{4:12}{5:12}{6:12}{7:<18}".format(
            res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], width=len_trancode))


    max_index = min(max_print, len(v_time_data_dura_order))
    print("***********************************************")
    print('3. 分析时段平均耗时最高的{}个接口为(包括成功率为零的): '.format(max_index))  #　耗时这里就不把成功率为０的过滤了吧
    print(
        "{0:<{width}}{1:<12}{2:<12}{3:<12}{4:12}{5:12}{6:12}{7:<18}".format("TranCode", "Frequency", "Base", "Success", "Base", "Duration", "Base", "Description",
                                                          width=len_trancode))
    for i in range(max_index):
        item = v_time_data_dura_order[i]
        base = dict_base_data[item[0]] if item[0] in dict_base_data else []

        res = []
        res.append('*' + item[0] if item[0] in apis else item[0])
        res.append("{:.2f}".format(item[2] / argv_l))
        res.append("{:.2f}".format(base[2] / argv_l) if base else "-")
        res.append("{:.2%}".format(item[5]))
        res.append("{:.2%}".format(base[5]) if base else "-")
        res.append("{:.2f}".format(item[6]))
        res.append("{:.2f}".format(base[6]) if base else "-")
        res.append(item[1])

        print("{0:<{width}}{1:<12}{2:<12}{3:<12}{4:12}{5:12}{6:12}{7:<18}".format(
            res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], width=len_trancode))


    """
    和基准比, 单独分析当前时点情况
    """
    # print(dict_time_data['TR0398'])
    # print(dict_base_data['TR0398'])
    keys = list(dict_time_data.keys())
    for k in keys:
        if k not in dict_base_data:
            # 新增调用的接口, 不参与比较
            dict_time_data.pop(k)
        else:
            item1 = dict_time_data[k]
            item2 = dict_base_data[k]
            # 5是成功率, 6是平均耗时
            if item2[2] < argv_l * min_freq_old or item2[6] == 0:  # base调用量为0的(6.12改成小于阈值), 成功率0的, 耗时0的不在当下考虑
                dict_time_data.pop(k)
                continue
            # 成功率为0的还是不过滤了, 特殊处理下就行了
            v = (item1[5] - item2[5]) / item2[5] if item2[5] else (1.0 if item1[5] else 0.0)
            item1.extend([item2[2], item1[2] - item2[2], (item1[2] - item2[2]) / item2[2],
                          item2[5], item1[5] - item2[5], v,
                          item2[6], item1[6] - item2[6], (item1[6] - item2[6]) / item2[6]])
            # 非新增的, 7老调用次数, 8调用次数量差, 9比差; 10老成功率, 11成功率量差, 12比差; 13老耗时, 14耗时量差, 15比差
    if not isworse and not isbetter:
        v_cmp_freq_abs = filter_map(dict_time_data, 8, True)
        v_cmp_freq_rel = filter_map(dict_time_data, 9, True)
        v_cmp_succ_abs = filter_map(dict_time_data, 11, True)
        v_cmp_succ_rel = filter_map(dict_time_data, 12, True)
        v_cmp_dur_abs = filter_map(dict_time_data, 14, True)
        v_cmp_dur_rel = filter_map(dict_time_data, 15, True)
    elif isworse:
        v_cmp_freq_abs = filter_map(dict_time_data, 8, True, ismix=False)
        v_cmp_freq_rel = filter_map(dict_time_data, 9, True, ismix=False)
        v_cmp_succ_abs = filter_map(dict_time_data, 11, False, ismix=False)
        v_cmp_succ_rel = filter_map(dict_time_data, 12, False, ismix=False)
        v_cmp_dur_abs = filter_map(dict_time_data, 14, True, ismix=False)
        v_cmp_dur_rel = filter_map(dict_time_data, 15, True, ismix=False)
    else:
        v_cmp_freq_abs = filter_map(dict_time_data, 8, False, ismix=False)
        v_cmp_freq_rel = filter_map(dict_time_data, 9, False, ismix=False)
        v_cmp_succ_abs = filter_map(dict_time_data, 11, True, ismix=False)
        v_cmp_succ_rel = filter_map(dict_time_data, 12, True, ismix=False)
        v_cmp_dur_abs = filter_map(dict_time_data, 14, False, ismix=False)
        v_cmp_dur_rel = filter_map(dict_time_data, 15, False, ismix=False)

    max_index = min(max_print, len(v_cmp_freq_abs))

    def printf(notes, l):
        print('{}的{}个接口为: '.format(notes, max_index))
        print("{:<{width}}{:<12}{:<12}{:<18}{:<12}{:<12}{:<18}{:<12}{:<12}{:<18}".format(
            "TranCode", "Frequency", "Base", "CHANGE", "Success", "Base", "CHANGE", "Duration", 'Base', 'CHANGE',
            width=len_trancode))
        for i in range(max_index):
            item = l[i]
            print("{:<{width}}{:<12.2f}{:<12.2f}{:<18.2%}{:<12.2f}{:<12.2f}{:<18.2%}{:<12.2f}{:<12.2f}{:<18.2%}".format(
                '*' + item[0] if item[0] in apis else item[0], item[2] / argv_l, item[7] / argv_l, item[9],
                                                               100 * item[5], 100 * item[10],
                item[11], item[6], item[13], item[15], width=len_trancode))

    print("**********************************************************************************************************")
    # printf('4. 交易量变化(量差)最大', v_cmp_freq_abs)
    printf('4. 相对基准时段交易量变化最大', v_cmp_freq_rel)
    print("***********************************************")

    printf('5. 相对基准时段成功率变化最大', v_cmp_succ_abs)
    print("***********************************************")

    # printf('5. 成功率变化(比差)最大', v_cmp_succ_rel)
    # printf('8. 平均耗时变化(量差)最大', v_cmp_dur_abs)
    printf('6. 相对基准时段平均耗时变化最大', v_cmp_dur_rel)

    # 由于对比列表里没打印中文描述, 不方便, 开一个线程去查
    class PrintDes(Thread):
        def __init__(self):
            Thread.__init__(self)

        def run(self):
            spaces = "                                                "
            while True:
                print(
                    "**********************************************************************************************************")
                trancode = input("输入接口编号查询接口中文描述, 输入q退出: ").upper().strip()
                if trancode == 'Q':
                    exit(0)
                elif trancode == "":
                    continue
                else:
                    finded = False
                    for key in dict_time_data_back:
                        if key.upper() == trancode:
                            finded = True
                            print(spaces + "接口描述: " + dict_time_data_back[key][1])
                    for key, value in h5_api_all.items():
                        if trancode in value['api']:
                            finded = True
                            print(spaces + "可能调用: " + key + ": " + value['des'])

                    if not finded:
                        print(spaces + "未查询到接口相关信息, 请检查输入!")

    thread = PrintDes()
    thread.setDaemon(False)
    thread.start()


if __name__ == '__main__':
    main()
