# -*- coding: utf-8 -*-
# Author: bbliu

"""

"""
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
    print("参数说明: -f 频次过滤阈值, 默认不过滤 -f2 基准时段的频次过滤阈值 -l 分析时长, 默认10 -c 分析时段末, 默认上一分钟")
    print("-t 基准时段末, 默认上周 -m 打印条数, 默认20 -s 待分析接口文件, 支持csv和xlsx -e 不分析接口文件 -n 登录名 -p 秘钥")
    print("-worse, 按交易量增加, 成功率降低, 耗时增加排序 -better 按交易量减少, 成功率增加, 耗时降低排序; 默认按变化绝对值排序")
    print("-sys mobs/ecbpin/ecbpout, 指定分析系统, 默认mobs, 不区分大小写")
    print("**********************************************************************************************************")

    login_name, login_password, now = None, None, datetime.now()

    argv_l, argv_c, argv_t, min_freq, max_print, min_freq_old = 10, now, None, 0.0, 20, 0.0

    api_file, apis, api_file_e, apis_e = None, set(), None, set()

    isworse, isbetter = False, False

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
            id = argv[i+1].upper()
            if id in ['MOBS', 'ECBPIN', 'ECBPOUT']:
                system_process = id
            else:
                print("无效的系统编号！")
                return
    print("当前分析系统: {}".format(system_process))
    # 先计算四个时间点, 得到当前时间段, 基准时间段
    if not argv_t: argv_t = argv_c - timedelta(weeks=1)
    time_end, time_start = argv_c - timedelta(minutes=1), argv_c - timedelta(minutes=argv_l)
    base_end, base_start = argv_t - timedelta(minutes=1), argv_t - timedelta(minutes=argv_l)

    time_start, time_end = t2s(time_start), t2s(time_end)
    base_start, base_end = t2s(base_start), t2s(base_end)

    # 再看看需不需要特殊标记本次涉及的接口
    if api_file:
        if api_file.endswith(".csv"):
            apis = set(read_csv(api_file, usecols=[0], header=None, skiprows=[0])[0].values)
        else:
            apis = set(read_excel(api_file, usecols=[0], header=None, skiprows=[0])[0].values)

    print("需要特别分析的接口:", apis if apis else "无")

    if api_file_e:
        apis_e = set(read_excel(api_file_e, usecols=[0], header=None, skiprows=[0])[0].values)

    print("需要排除分析的接口:", apis_e if apis_e else "无")

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
    # print(dict_time_data['TR0398'])
    # print(dict_base_data['TR0398'])

    len_trancode = max([len(x) for x in dict_time_data.keys()])+11

    """
    先不和基准比, 单独分析当前时点情况
    """

    def filter_map(dic, index, reverse=False, isapi=True, ismix = True):
        v_dic_filter = list(filter(lambda x: x[2] >= argv_l * min_freq and x[0] not in apis_e
                                   and (not isapi or x[0] in apis if apis else True), dic.values()))
        return sorted(v_dic_filter, key=lambda x: abs(x[index]) if ismix else x[index], reverse=reverse)

    # v_time_host_succ_order, v_time_host_dura_order = filter_map(dict_time_host, 5, isapi=False), filter_map(dict_time_host, 6, True, isapi=False)
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
    # 再处理当前API情况, 先打印成功率为0的, 然后按成功率和耗时排序, 打印出前10
    print('1. 均成功率为零的接口为: ')
    print("{0:<{width}}{1:<12}{2:<12}{3:<18}{4:<20}".format("TranCode", "Frequency", "Success", "Duration", "Description", width=len_trancode))
    v_time_data_freq_order_zero = sorted([x for x in v_time_data_succ_order if x[5] == 0.0], key=lambda x: x[2],
                                         reverse=True)
    zero_count = 0
    for item in v_time_data_freq_order_zero:
        if item[5] != 0.0: break
        zero_count += 1
        print("{0:<{width}}{1:<12.2f}{2:<12.2%}{3:<18.2f}{4:<20}".format(
            '*'+item[0] if item[0] in apis else item[0], item[2]/argv_l, item[5], item[6], item[1], width=len_trancode))

    # 把成功率为0的过滤掉, 剩下的再取成功率最低的前10和耗时最高的前十
    v_time_data_succ_order_nozero = list(filter(lambda x: x[5] != 0, v_time_data_succ_order))
    v_time_data_dura_order_nozero = list(filter(lambda x: x[5] != 0, v_time_data_dura_order))
    max_index = min(max_print, len(v_time_data_succ_order_nozero))

    print("***********************************************")
    print('2. 均成功率最低的{}个接口为: '.format(max_index))
    print("{0:<{width}}{1:<12}{2:<12}{3:<18}{4:<20}".format("TranCode", "Frequency", "Success", "Duration", "Description", width=len_trancode))
    for i in range(max_index):
        item = v_time_data_succ_order_nozero[i]
        print("{0:<{width}}{1:<12.2f}{2:<12.2%}{3:<18.2f}{4:<20}".format(
            '*'+item[0] if item[0] in apis else item[0], item[2]/argv_l, item[5], item[6], item[1], width=len_trancode))

    print("***********************************************")
    print('3. 平均耗时最高的{}个接口为: '.format(max_index))
    print("{0:<{width}}{1:<12}{2:<12}{3:<18}{4:<20}".format("TranCode", "Frequency", "Success", "Duration", "Description", width=len_trancode))
    for i in range(max_index):
        item = v_time_data_dura_order_nozero[i]
        print("{0:<{width}}{1:<12.2f}{2:<12.2%}{3:<18.2f}{4:<20}".format(
            '*'+item[0] if item[0] in apis else item[0], item[2]/argv_l, item[5], item[6], item[1],width=len_trancode))

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
        print("***********************************************")
        print('{}的{}个接口为: '.format(notes, max_index))
        print("{:<{width}}{:<12}{:<12}{:<18}{:<12}{:<12}{:<18}{:<12}{:<12}{:<18}".format(
            "TranCode", "Frequency", "Base", "CHANGE", "Success", "Base", "CHANGE", "Duration", 'Base', 'CHANGE', width=len_trancode))
        for i in range(max_index):
            item = l[i]
            print("{:<{width}}{:<12.2f}{:<12.2f}{:<18.2%}{:<12.2f}{:<12.2f}{:<18.2%}{:<12.2f}{:<12.2f}{:<18.2%}".format(
                '*'+item[0] if item[0] in apis else item[0], item[2]/argv_l, item[7]/argv_l, item[9], 100*item[5], 100*item[10],
                item[12], item[6], item[13], item[15], width=len_trancode))

    # printf('4. 交易量变化(量差)最大', v_cmp_freq_abs)
    printf('4. 交易量变化(比差)最大', v_cmp_freq_rel)
    # printf('6. 成功率变化(量差)最大', v_cmp_succ_abs)
    printf('5. 成功率变化(比差)最大', v_cmp_succ_rel)
    # printf('8. 平均耗时变化(量差)最大', v_cmp_dur_abs)
    printf('6. 平均耗时变化(比差)最大', v_cmp_dur_rel)


    # 由于对比列表里没打印中文描述, 不方便, 开一个线程去查
    class PrintDes(Thread):
        def __init__(self):
            Thread.__init__(self)

        def run(self):
            spaces = "                                                "
            while True:
                print("**********************************************************************************************************")
                trancode = input("输入接口编号查询接口中文描述, 输入q退出: ").upper().strip()
                if trancode == 'Q':
                    exit(0)
                else:
                    finded = False
                    for key in dict_time_data:
                        if key.upper() == trancode:
                            finded = True
                            print(spaces + dict_time_data[key][1])
                    if not finded:
                        print(spaces+"未查询到输入的接口编号, 请重新输入!")


    thread = PrintDes()
    thread.setDaemon(False)
    thread.start()


if __name__ == '__main__':
    main()
