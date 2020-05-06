# -*- coding: utf-8 -*-

# Author: Cynthia

from re import match
from requests import Session
from base64 import b64encode
from sys import exit, argv, path
from threading import Thread
from collections import defaultdict
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from json import dumps as json_dumps, loads as json_loads
from pickle import dump as pickle_dump, load as pickle_load
from numpy import std, save as numpy_save, load as numpy_load


def main():
    session, base_url = Session(), "http://xxx.xxx.xxx.xxx:8081"

    # 处理用户输入
    print("**********************************************************************************************************")
    print("用法：mobsapi -s 开始时间 -e 结束时间 -t 异常阙值 -n 登录名 -p 登录秘钥")
    print("时间格式：HH:MM（当天）或YYYY-MM-DD HH:MM（指定天），时间跨度建议一小时")
    print("经测试，非当日时间可以任意指定时间跨度，当日只能1~2个小时，多了服务器会报错")
    print("不指定时间，默认最近一个小时；异常阙值缺省为1.30；首次使用请指定登陆信息")
    print("**********************************************************************************************************")

    # 设置时间区间、异常阙值的缺省值
    now, one_hour_ago = datetime.now(), datetime.now() - timedelta(hours=1)
    time_start, time_end, threshold = one_hour_ago.strftime("%Y-%m-%d %H:%M"), now.strftime("%Y-%m-%d %H:%M"), 1.3

    def getpath(filename) -> str:
        if path[0].endswith(".zip"):
            return str.replace(path[0], "base_library.zip", filename)
        else:
            return path[0] + "\\" + filename

    login_name, login_password = None, None
    for i in range(len(argv)):
        if argv[i] == '-s' and argv[i + 1:]:
            if match(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}", argv[i + 1]):
                time_start = argv[i + 1]
            elif match(r"[0-9]{2}:[0-9]{2}", argv[i + 1]):
                time_start = now.strftime("%Y-%m-%d") + " " + argv[i + 1]
            elif match(r"[0-9]{1}:[0-9]{2}", argv[i + 1]):
                time_start = now.strftime("%Y-%m-%d") + " " + "0" + argv[i + 1]
            else:
                print("无效的开始时间！")
                return
        elif argv[i] == '-e' and argv[i + 1:]:
            if match(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}", argv[i + 1]):
                time_end = argv[i + 1]
            elif match(r"[0-9]{2}:[0-9]{2}", argv[i + 1]):
                time_end = now.strftime("%Y-%m-%d") + " " + argv[i + 1]
            elif match(r"[0-9]{1}:[0-9]{2}", argv[i + 1]):
                time_end = now.strftime("%Y-%m-%d") + " " + "0" + argv[i + 1]
            else:
                print("无效的截止时间！")
                return
        elif argv[i] == '-t' and argv[i + 1:]:
            if match(r"[0-9]+.?[0-9]*", argv[i + 1]):
                threshold = float(argv[i + 1])
            else:
                print("无效的异常阙值！")
                return
        elif argv[i] == '-n' and argv[i + 1:]:
            login_name = argv[i + 1]
        elif argv[i] == '-p' and argv[i + 1:]:
            # 智能运维平台的密码做了base64加密
            # 注意, b64encode的参数和输出都是byte类型, 即b'xxx'这种
            # byte和str之间要通过encode, decode转码
            login_password = b64encode(argv[i + 1].encode('utf-8')).decode('utf-8')

    url_login_info = getpath("login_info.npy")

    if login_name and login_password:
        numpy_save(url_login_info, [login_name, login_password])
    else:
        try:
            login_name, login_password = numpy_load(url_login_info)
        except:
            print("首次使用，请设置登录信息：-n 用户名 -p 密码！")
            return

    print("时间区间{0}~{1}，异常阙值{2:.2f}......".format(time_start, time_end, threshold))

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
            # 注意这里上送参数用了json_dumps, 有时候不加
            # 如果从fiddler里看到的是json形式, 得加; 如果是a=xx&b=xx&c=xx, 直接送params
            return json_loads(session.post(login_url, json_dumps(params)).text)['RSP_BODY']['userAuthToken']
        except:
            print("登陆失败！请检查网络设置或重新配置登录信息：-n 用户名 -p 密码！")
            exit(1)

    print("登录中......")
    userAuthSession = login(login_name, login_password, base_url)

    # 查询, 经测验，2个小时勉强顶得住，再长服务器就返回错误了
    def pull(login_name, userAuthSession, base_url, time_start, time_end) -> list:
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
                "firstDimensionsNo": "transCode",
                "secondDimensionsNo": "",
                "systemId": "MOBS",
                "timeType": 4,
                "type": "MX",

            }
        }
        try:
            return json_loads(session.post(pull_url, json_dumps(params)).text)['RSP_BODY']['dimStatisInfoVoList']
        except:
            print("拉取失败！可能时间区间设置过大，请再次尝试！")
            exit(1)

    print("数据拉取中......")
    dimStatisInfoVoList = pull(login_name, userAuthSession, base_url, time_start, time_end)

    if dimStatisInfoVoList:
        print("数据拉取成功......")
    else:
        print("拉取数据有误！可能服务器不稳定，请再次尝试！")
        return

    print("**********************************************************************************************************")

    def process(dimStatisInfoVoList):
        """
        除了从网上拉取，还可以通过pandans包的read_excel从excel里读取
        xls = read_excel(filename, skiprows=4, header=None, skipfooter=1, usecols=[0, 1, 2, 3, 5])
        xls = xls.values.tolist()
        """
        """
        拉取的数据列数很多，分析的时候不需要那么多, 没有到的后面看看还能不能干点别的
        xls = [[x['tradeDate'] + ' ' + x['tradeTime'], x['secondDimensionsNo'], x['configDesc'], int(x['tradeCount']),
                int(x['successTradeCount']), float(x['avgTime']), float(x['successRate']),
                float(x['systemSuccessRate']),
                float(x['tradeSuccessRate'])] for x in dimStatisInfoVoList]
        """
        xls = [[x['tradeDate'] + ' ' + x['tradeTime'], x['secondDimensionsNo'], x['configDesc'],
                int(x['tradeCount']), float(x['avgTime'])] for x in dimStatisInfoVoList]
        # 分别以时间和日期为key值构造两个dict，便于后面使用
        dict_time, dict_api = defaultdict(list), defaultdict(list)
        for item in xls:
            dict_time[item[0]].append(item[1:])
            dict_api[item[1]].append([item[0]] + item[2:])

        # 计算几个统计数据-时间跨度、所有接口的总调用次数、总耗时、总平均耗时
        time_range = len(set([item[0] for item in xls]))
        count_all = sum([item[3] for item in xls])
        duras_all = sum([item[3] * item[4] for item in xls])
        duras_avg_all = duras_all / count_all if count_all > 0 else 0

        # 计算各个时间维度的统计信息，包括本分钟所有接口调用次数、总耗时、平均耗时
        dict_stati_time = defaultdict(list)
        for key, value in dict_time.items():
            count_time = sum([item[2] for item in value])
            duras_time = sum([item[2] * item[3] for item in value])
            duras_avg_time = duras_time / count_time if count_time > 0 else duras_avg_all
            dict_stati_time[key].extend([count_time, duras_time, duras_avg_time])

        # 计算各个接口的统计信息，接口名、总调用次数、总耗时、平均耗时、标准差
        dict_stati_api = defaultdict(list)
        for key, value in dict_api.items():

            count_api = sum([item[2] for item in value])
            duras_api = sum([item[2] * item[3] for item in value])
            duras_avg_api = duras_api / count_api if count_api > 0 else duras_avg_all

            # 对均耗时归一化之后再去算无偏标准差
            duras_l = [item[3] for item in value]
            # 归一化算标准差的时候需要兼容min-max相同的情况，这种一般是极低频接口，直接设置标准差为0
            if max(duras_l) == min(duras_l):
                std_api = 0
            else:
                std_api = std([(x - min(duras_l)) / (max(duras_l) - min(duras_l)) for x in duras_l], ddof=1)

            dict_stati_api[key].extend([value[0][1], count_api, duras_api, duras_avg_api, std_api])

        # 打印按照各个维度排名的前十的接口编号和名字, 注意过滤低频的（至少time_range*60次）
        l_s_api = [item for item in list(dict_stati_api.items()) if item[1][1] >= time_range * 60]
        print("1. 每分钟交易量排名前十的高频接口（平均每秒至少调用一次）分别为：")
        l_s_api.sort(key=lambda x: x[1][1], reverse=True)
        print("{0:<8}{1:<8}{2:<8}{3:<8}{4:<}".format("接口编号", "分均频次", "平均耗时", "波动程度", "接口名称"))
        for i in range(10):
            list_print = [l_s_api[i][0], l_s_api[i][1][1] / time_range, l_s_api[i][1][3], l_s_api[i][1][4],
                          l_s_api[i][1][0]]
            print("{0:<12}{1:<12.0f}{2:<12.2f}{3:<12.2f}{4:<}".format(*list_print))
        print(
            "**********************************************************************************************************")

        print("2. 平均调用耗时排名前十的高频接口（平均每秒至少调用一次）分别为：")
        l_s_api.sort(key=lambda x: x[1][3], reverse=True)
        print("{0:<8}{1:<8}{2:<8}{3:<8}{4:<}".format("接口编号", "分均频次", "平均耗时", "波动程度", "接口名称"))
        for i in range(10):
            list_print = [l_s_api[i][0], l_s_api[i][1][1] / time_range, l_s_api[i][1][3], l_s_api[i][1][4],
                          l_s_api[i][1][0]]
            print("{0:<12}{1:<12.0f}{2:<12.2f}{3:<12.2f}{4:<}".format(*list_print))
        print(
            "**********************************************************************************************************")

        print("3. 平均耗时波动排名前十的高频接口（平均每秒至少调用一次）分别为：")
        l_s_api.sort(key=lambda x: x[1][4], reverse=True)
        print("{0:<8}{1:<8}{2:<8}{3:<8}{4:<}".format("接口编号", "分均频次", "平均耗时", "波动程度", "接口名称"))
        for i in range(10):
            list_print = [l_s_api[i][0], l_s_api[i][1][1] / time_range, l_s_api[i][1][3], l_s_api[i][1][4],
                          l_s_api[i][1][0]]
            print("{0:<12}{1:<12.0f}{2:<12.2f}{3:<12.2f}{4:<}".format(*list_print))
        print(
            "**********************************************************************************************************")

        # 本来想开个子线程或者子进程去画图，但是matplot好像不支持
        # 只能换一种思路， 开子线程去让输入待分析时间点, 在主进程里画图
        class AnalysePeak(Thread):
            def __init__(self, dict_time, dict_stati_api, duras_avg_all):
                Thread.__init__(self)
                self.dic_time = dict_time
                self.dict_stati_api = dict_stati_api
                self.duras_avg_all = duras_avg_all

            def run(self):
                print(
                    "**********************************************************************************************************")

                while True:

                    time = input("请输入待分析时间点YYYY-MM-DD HH:MM：").strip()
                    if time not in self.dic_time:
                        print("无效的时间输入！")
                    else:
                        list_apis = dict_time[time].copy()
                        for item in list_apis:
                            # 计算异常点贡献值，计算公式为max(本时点平均耗时-总平均耗时, 0)*本时点调用次数
                            # 某个特定接口的总平均耗时可能不存在，如果没有，取全局平均耗时duras_avg_all
                            if item[0] in self.dict_stati_api:
                                duras_avg_api = self.dict_stati_api[item[0]][3]
                            else:
                                duras_avg_api = self.duras_avg_all
                            contribute_value = max(0, item[2] * (item[3] - duras_avg_api))
                            item.extend([duras_avg_api, contribute_value])

                        # 算出各个接口的异常贡献后，取和，然后算比例
                        # 注意处理极个别特殊情况，总平均耗时很高，个别低的时点可能所有接口都很快，contribute_value都为0
                        contribute_value_all = sum([item[5] for item in list_apis])
                        for item in list_apis:
                            contribute_percent = item[5] / contribute_value_all if contribute_value_all != 0 else 0
                            item.append(contribute_percent)

                        list_apis.sort(key=lambda x: x[6], reverse=True)
                        print(
                            "**********************************************************************************************************")
                        print("时点{0}的接口耗时异常增加主要由以下接口导致（打印前二十个）：".format(time))
                        head = ["接口编号", "时点频次", "时点均耗", "正常均耗", "贡献量", "贡献度", "接口名称"]
                        print("{0:<8}{1:<8}{2:<8}{3:<8}{4:<9}{5:<9}{6:<}".format(*head))
                        for i in range(20):
                            item = list_apis[i]
                            list_print = [item[0], item[2], item[3], item[4], item[5], item[6], item[1]]
                            print("{0:<12}{1:<12.0f}{2:<12.2f}{3:<12.2f}{4:<12.0f}{5:<12.2%}{6:<}".format(*list_print))
                        print(
                            "**********************************************************************************************************")

        # 这里有个问题， dict_stati_api和duras_avg_all如果取分析的这个时间段的，有可能异常事件很长
        # 每个接口的平均耗时和总平均耗时已经被拉高了，比如某个接口平时平均30ms，分析时段的平均是40，分析时点50, 贡献量算20还是10？
        # 那么把历史的存了吧，但凡在合理范围内的总平均耗时，则把新的dict_stati_api和duras_avg_all存起来下次备用

        # with语句虽然会处理文件读取过程中的异常，但是open异常不会处理，所以外层还得加个try
        # 这里用pickle而不是np，因为np老乱转格式，而pickle存的时候是什么取的时候就是什么
        # 这里获取执行文件所在路径用sys.path， 其它的方法都有问题，不能兼顾脚本、exe、环境变量各种情况

        url_dict_stati_api, url_duras_avg_all = getpath("dict_stati_api.pickle"), getpath("duras_avg_all.pickle")

        try:
            with open(url_dict_stati_api, "rb") as file:
                dict_stati_api_old = pickle_load(file)
            with open(url_duras_avg_all, "rb") as file:
                duras_avg_all_old = pickle_load(file)
        except:
            dict_stati_api_old = dict_stati_api
            duras_avg_all_old = duras_avg_all

        # 比如已存的是60ms，则<=66ms的都认为是正常水平，存起来
        # 另外，过短的不建议存，最好只存时间跨度大于55的
        if time_range >= 55 and duras_avg_all <= duras_avg_all_old * 1.1:
            with open(url_dict_stati_api, "wb") as file:
                pickle_dump(dict_stati_api, file)
            with open(url_duras_avg_all, "wb") as file:
                pickle_dump(duras_avg_all, file)

        threadAP = AnalysePeak(dict_time, dict_stati_api_old, duras_avg_all_old)
        threadAP.setDaemon(True)

        # 这里先不开子线程，后面再输出点东西，在画图前开就行

        # 主进程继续画图，三个参数分别为x，y，标注阙值
        def draw(x, y, threshold, threadAP):

            plt.figure(figsize=(12, 12 * 0.618))
            plt.xlabel("Time")
            plt.ylabel("Average Time-Consuming(ms)")

            plt.plot(y)
            # axis用于定义横坐标、纵坐标刻度范围
            plt.axis([0, len(x), 0, max(y) * 1.1])

            # 横坐标刻度保持24个以内
            step = len(x)//24+1
            range_x, mark_x = range(0, len(x), step), [x[i][11:] for i in range(0, len(x), step)]

            plt.xticks(range_x, mark_x)

            # 对于折线图的上顶点加标注，超过一定阙值, 且是尖点才加
            for i in range(len(x)):
                if y[i] >= threshold and (i == 0 or i == len(x)-1 or (y[i] >= y[i-1] and y[i] >= y[i+1])):
                    plt.annotate(x[i][11:], xy=(i, y[i]), xytext=(-20, 10), textcoords="offset pixels", color="red")

            # 主进程卡住之前先把子线程启动了
            threadAP.start()
            url_img = getpath("figure.png")
            plt.savefig(url_img)
            plt.show()

        l_s_time = list(dict_stati_time.items())

        # 先按照耗时由大到小排序，打印平均耗时最高的5个时间点
        l_s_time.sort(key=lambda x: x[1][2], reverse=True)
        print("4. 平均耗时排名前五的时点为（时段总平均耗时{:.2f}ms），参考平均耗时{:.2f}ms：".format(duras_avg_all, duras_avg_all_old))
        print("{0:<22}{1:<8}".format("时点", "平均耗时"))
        for i in range(5):
            print("{0:<24}{1:<12.2f}".format(l_s_time[i][0], l_s_time[i][1][2]))
        print(
            "**********************************************************************************************************")

        # 画图，更直观地展示接口平均耗时随时点的变化
        l_s_time.sort(key=lambda x: x[0])
        x, y = [x[0] for x in l_s_time], [x[1][2] for x in l_s_time]
        # 先设置阙值，默认1.3，即平均100ms，到了130ms就认为高了
        draw(x, y, duras_avg_all * threshold, threadAP)

    process(dimStatisInfoVoList)


if __name__ == '__main__':
    main()
