# -*- encding: utf-8 -*-
# Author: bbliu

"""
    指定h5代码根目录, 扫描所有模块接口调用情况

"""

import os
import re
import sys
import json
import copy
import pickle
import pandas as pd
from ftplib import *
from collections import defaultdict


# 取程序运行目录, 可兼容.py和.exe两种情况
# 比如设置了环境变量, 但这里取的还是exe所在的目录
def getpath(filename) -> str:
    if sys.path[0].endswith(".zip"):
        return str.replace(sys.path[0], "base_library.zip", filename)
    else:
        return sys.path[0] + "\\" + filename


def main():
    print("**********************************************************************************************************")
    print("SCAN参数说明: -d h5代码根目录, -s 模块名或子模块名或页面码, -t YYYYMMDD, -n ftp用户名, -p ftp密码")
    print("默认将所有模块结果生成h5_api_all.xlsx放在当前目录, 指定-t同步上传50服务器, 指定-s 解析特定模块接口")
    print("建议远端用回归流, 执行时会自动更新; 首次执行请指定工程目录; 首次上传ftp请提供50服务器的用户名/密码")
    print("例: scan, scan -s life, scan -s NHP0008, scan -s NC0,life\\HP0,credit_card,NHP0001")
    print("不指定参数, 仅生成h5_api_all.xlsx; 指定-s, 额外生成h5_api_part.xlsx和h5_api_imms.xlsx")
    print("文件h5_api_all.xlsx可供imms的-verbose参数读入, 文件h5_api_imms.xlsx供imms的-s参数读入")
    print("**********************************************************************************************************")

    ftp_ip = "182.207.129.50"
    ftp_port = 2001
    file_xlsx = "h5_api_all.xlsx"
    file_part = "h5_api_part.xlsx"
    file_imms = "h5_api_imms.xlsx"

    # 首先是用户输入参数对应的变量
    # 直接这么命名省时好记
    var_d = None  # 指定h5代码根目录
    var_s = None  # 要指定打印的模块名/二级模块名/页面码
    var_t = None  # 投产日期
    var_n = None  # 50服务器用户名
    var_p = None  # 50服务器密码

    for i in range(len(sys.argv)):
        if sys.argv[i] == '-d' and sys.argv[i + 1:]:
            # 这种拼法能兼容前面目录带\和不带\, 最后一个""可以保证末尾添加\
            s = os.path.join(sys.argv[i + 1], "src\\modules", "")
            if os.path.isdir(s):
                var_d = s
            else:
                print("无效的h5代码目录！")
                sys.exit(1)

        elif sys.argv[i] == '-s' and sys.argv[i + 1:]:
            var_s = [os.path.join(x.strip(), "") for x in sys.argv[i+1].split(",")]
        elif sys.argv[i] == '-t' and sys.argv[i + 1]:
            if re.match(r"^[0-9]{8}$", sys.argv[i + 1]):
                var_t = sys.argv[i + 1]
            else:
                print("无效的日期格式!")
                sys.exit(1)
        elif sys.argv[i] == '-n' and sys.argv[i + 1]:
            var_n = sys.argv[i + 1]
        elif sys.argv[i] == '-p' and sys.argv[i + 1]:
            var_p = sys.argv[i + 1]

    # 先判断能否拿到h5代码目录
    file_d = getpath("data_d.pickle")
    if not var_d:
        try:
            with open(file_d, "rb") as f:
                var_d = pickle.load(f)
        except FileNotFoundError:
            print("首次使用，请设置-d h5代码目录!")
            sys.exit(1)
            #　异常退出建议用这个, 而不是return
            # 这样外部调用它的能达到具体退出状态码
    else:
        with open(file_d, "wb") as f:
            pickle.dump(var_d, f)

    # 再判断如果指定了-t参数能否拿到ftp用户名密码
    if var_t:
        file_np = getpath("data_np.pickle")
        if var_n and var_p:
            with open(file_np, "wb") as f:
                pickle.dump([var_n, var_p], f)
        else:
            try:
                with open(file_np, "rb") as f:
                    var_n, var_p = pickle.load(f)
            except FileNotFoundError:
                print("首次上传FTP请提供-n 账号 -p 密码!")
                sys.exit(1)

    print("模块所在目录为: {}".format(var_d[:-1]))
    print("模块名特别指定: {}".format(", ".join([x[:-1] for x in var_s]) if var_s else "未指定, 仅生成全部模块统计结果"))
    print("**********************************************************************************************************")
    print("更新代码...")
    # 直接这么执行会阻塞主程序, 跟直接运行git一样; 不想阻塞好像也有办法, start?
    r = os.system("git -C {} pull".format(var_d))  # git -C指定更新的目录
    if r != 0:
        print("更新失败, 请检查网络或git配置!")
        sys.exit(1)
    print("更新完成...")
    print("**********************************************************************************************************")
    # 　下面初始化后续处理需要用到的变量
    dict_base = defaultdict(set)  # 所有包含.vue文件的目录, 格式{路径: {接口1, 接口2}}
    dict_des = defaultdict(str)  # 所有confi.json里提取出来的, {页面码: 中文描述}

    # 第一遍扫描, 只处理叶节点那些路径下有.vue文件的, 把他们的接口扫描出来; 遇到confi.json也扫描
    print("扫描文件...", end="", flush=True)  # 指定end的时候有时候不会及时打印, 加上flush=True
    # 注意第一个root会是根目录, 后面注意过滤掉
    work_all = None  # work_all存储最外层的子目录, 用于判断程序处理进度
    # 正则比较复杂, 先编译了
    pattern = r'(["\']|API.SERVICE.API_)([A-Z0-9]{10}|[A-Z0-9]{8}|[A-Z0-9]{6})\b["\']?'  # 三元表达式的写法毕竟少, 这种情况就不考虑8位和10位的了
    pattern1 = re.compile(r'\b["\']?(rpc|prdCod|sendRequest|longTimeRpc|processCode|tranCode|transCode|targetCode|specifyKeyProcessCode|transProcessCode)_?[0-9]?'
                          r'["\']?[\n\t ]*?[(:=][\n\t ]*?'+pattern)
    pattern2 = re.compile(r'\?[\n\t ]*?'+pattern+r'[\n\t ]*?:[\n\t ]*?'+pattern)
    for root, dirs, files in os.walk(var_d):
        root = os.path.join(root, "")  # 如果有\不会重复添加, 没有会添加, 加\是为了处理C:\aaa\bbb\wr, C:\aaa\bbbwraaa这种情况
        # 第一个扫描的会是根目录, 所以不会出现work_all未声明先访问的情况
        if root == var_d: work_all = [os.path.join(root, x, "") for x in dirs]
        else:
            if root in work_all:
                index = work_all.index(root)+1
                # 每10%打印一次进度, 最后一次打印100%
                if index % int(len(work_all)/10) == 0 or index == len(work_all):
                    print("{:.0%}...".format(index/len(work_all)), end="", flush=True)

        for file in files:
            if file.endswith(".vue"):
                file_vue = os.path.join(root, file)
                try:
                    with open(file_vue, "r", encoding="utf-8") as f:
                        s = ""
                        # 去掉注释行, 包括//和/**/两种
                        isremark = False
                        for line in f.readlines():

                            if line.strip().startswith("//"):
                                continue

                            if line.strip().startswith("/*") and '*/' in line:
                                continue

                            if line.strip().startswith("/*"):
                                isremark = True
                                continue

                            if '*/' in line:
                                isremark = False
                                continue

                            if isremark: continue  # 注意这一句得放下面, 不能放上面, 否则就到不了*/了

                            s += line

                        target1 = re.findall(pattern1, s)
                        target2 = re.findall(pattern2, s)

                except UnicodeDecodeError:
                    # 个别文件不是utf-8编码
                    with open(file_vue, "r", encoding="gb2312") as f:
                        s = ""
                        # 去掉注释行
                        isremark = False
                        for line in f.readlines():

                            if line.strip().startswith("//"):
                                continue

                            if line.strip().startswith("/*") and '*/' in line:
                                continue

                            if line.strip().startswith("/*"):
                                isremark = True
                                continue

                            if '*/' in line:
                                isremark = False
                                continue

                            if isremark: continue  # 注意这一句得放下面, 不能放上面, 否则就到不了*/了

                            s += line

                        target1 = re.findall(pattern1, s)
                        target2 = re.findall(pattern2, s)

                # 这里空的也写, 是为了保证所有目录下有.vue文件的目录都进到dict_base里, 不管有没有扫描出来接口
                # 从而保证路径和vue文件是一一对应的, 后面才好加总
                target1 = set([x[2] for x in target1])
                target2 = set([x[1] for x in target2]+[x[3] for x in target2])
                dict_base[root] = dict_base[root] | target1 | target2
            elif file == "conf.json":
                file_json = os.path.join(root, file)

                try:
                    with open(file_json, "r", encoding="utf-8") as f:
                        s = f.read()
                        # 对于utf-8格式的, 有些文件带bom, 需要去掉
                        if s.startswith(u"\ufeff"):
                            s = s.encode("utf-8")[3:].decode("utf-8")
                        data = json.loads(s)
                except UnicodeDecodeError:
                    with open(file_json, "r", encoding="gb2312") as f:
                        data = json.load(f)

                for item in data:
                    for each in data[item]:
                        dict_des[each] = data[item][each]['title']

    print("")

    print("解析接口...", end="", flush=True)
    dict_all = defaultdict(set)  # 不仅包括叶目录, 也包括一级, 二级目录, 根据dict_base构建, 没vue的一二级目录不会统计进去
    dict_structure = dict()  # 最终包含.vue文件的一二三级目录结构, {life:{WW1:{TWW9A01, TWW9A02}, WW2:{TWW2122}}}
    # 如果路径在dict_base里(其目录底下就有.vue)或者是其父目录, 加总
    """
    考虑一种特殊情况:
    C://aa/bb/index.vue
    C://aa/bb/cc/index.vue
    第二遍扫描到C://aa/的时候, 会把这俩都加起来
    扫描到C://aa/bb/的时候, 也是都加起来
    扫描到C://aa/bb/cc/的时候, 直接把C://aa/bb/cc/index.vue的统计结果拿过来
    可以看出, 目前的逻辑是能满足这种特殊情况的
    """

    for root, dirs, files in os.walk(var_d):

        root = os.path.join(root, "")

        #画进度条
        if root == var_d: work_all = [os.path.join(root, x, "") for x in dirs]
        else:
            if root in work_all:
                index = work_all.index(root)+1
                if index % int(len(work_all)/10) == 0 or index == len(work_all):
                    print("{:.0%}...".format(index/len(work_all)), end="", flush=True)

        # 只有带有vue的目录的上级目录对我们才有意义

        for each in dict_base:
            # root末尾都加了\, C:\xxx\xx\xxx\, 所以直接用in判断是可以的
            if root in each:
                # 这里dict_all的key值把绝对路径的前半部分给去了, 末尾的\还得留着
                key = root.replace(var_d, "")
                dict_all[key] |= dict_base[each]  # dict_base里的肯定都有.vue, 所以这里直接加总一点问题没有

                if key.count("\\") == 3:  # 3级目录的时候采取构建dict_structure, life\HP0\NHP0008\
                    l = key.split("\\")
                    if l[0] not in dict_structure:
                        dict_structure[l[0]] = defaultdict(set)
                    # 这里最后一级用set因为存在这种情况: life\HP0\NHP0008\, life\HP0\NHP0008\component\
                    dict_structure[l[0]][l[1]].add(l[2])
    print("")
    print("总接口数: {}".format(len(dict_all[""])))
    print("**********************************************************************************************************")

    # 注意dict_structure和dict_lines的key值因为是split出来的, 不带\
    # dict_structure结构：　{life:{WW1:{TWW9A01, TWW9A02, component}, WW2:{TWW2122}}}
    # dict_lines结构: {life:{WW1:5, WW2:1}}
    dict_lines = dict()
    for item in dict_structure:
        for each in dict_structure[item]:
            if item not in dict_lines:
                dict_lines[item] = defaultdict(int)
            dict_lines[item][each] += len(dict_structure[item][each])
            # 其实这里用=就行, [item][each]不可能重复的
            # 另外, dict_lines不是必须算, 只是为了后面汇总一级模块高度方便

    def generateXlsx(path, dict_structure, dict_lines):
        with pd.ExcelWriter(path) as writer:

            df, workbook = pd.DataFrame(), writer.book
            # 这里好像必须得有设置个空df然后to_excel这一步
            df.to_excel(writer, index=False, header=False, sheet_name="接口统计")
            worksheet = writer.sheets['接口统计']

            # 第二个参数是宽度
            worksheet.set_column("A:G", None, workbook.add_format({
                "text_wrap": True,
                'align': 'left',
                'valign': 'vcenter',
            }))
            worksheet.set_column("A:A", 25)
            worksheet.set_column("B:B", 40)
            worksheet.set_column("C:C", 10)
            worksheet.set_column("D:D", 40)
            worksheet.set_column("E:E", 10)
            worksheet.set_column("F:F", 30)
            worksheet.set_column("G:G", 40)
            # 直接set_column或set_row是全部设置格式, 而写的时候加格式则是有内容的才有格式
            # 比如这里write_row, 并不会一整行都加上格式, 如果用set_row则是一整行
            worksheet.write_row(0, 0, ['模块名', '接口调用', '二级模块', '接口调用', "页面码", "页面描述", "接口调用"],
                                workbook.add_format({"bold": True, "border": 1, "bg_color": "#00CD66"}))

            index = 1  # 注意数字编号是从0开始的, 但字母编号是从1开始的

            # 构建excel直接用dict_structure就好
            for each in dict_structure:

                # 先处理第一第二列
                lines = sum(dict_lines[each].values())
                key = os.path.join(each, "")
                if lines == 1:
                    # write用的是数字索引...
                    worksheet.write(index, 0, each)
                    worksheet.write(index, 1, ", ".join(dict_all[key]))
                else:
                    # merge_range, 跨行写
                    worksheet.merge_range("A{}:A{}".format(index + 1, index + 1 + lines - 1), each)
                    worksheet.merge_range("B{}:B{}".format(index + 1, index + 1 + lines - 1), ", ".join(dict_all[key]))

                # 再处理第三第四列, 第二层要设置i2, 而第一层用index就行
                i2 = index
                # 二级模块排个序
                list_2 = sorted(dict_structure[each].keys())
                for each2 in list_2:
                    lines2 = dict_lines[each][each2]
                    key = os.path.join(each, each2, "")
                    if lines2 == 1:
                        # write用的是数字索引...
                        worksheet.write(i2, 2, each2)
                        worksheet.write(i2, 3, ", ".join(dict_all[key]))
                    else:
                        # merge_range, 跨行写
                        worksheet.merge_range("C{}:C{}".format(i2 + 1, i2 + 1 + lines2 - 1), each2)
                        worksheet.merge_range("D{}:D{}".format(i2 + 1, i2 + 1 + lines2 - 1), ", ".join(dict_all[key]))

                    i3 = i2  # 处理第五六七列, 注意这里初始值不是index, 不是i, 而应该是i2
                    # 页面码排个序
                    list_3 = sorted(list(dict_structure[each][each2]))
                    for each3 in list_3:
                        key = os.path.join(each, each2, each3, "")
                        worksheet.write(i3, 4, each3)
                        worksheet.write(i3, 5, dict_des[each3])
                        worksheet.write(i3, 6, ", ".join(dict_all[key]))
                        i3 += 1

                    # 注意i2的变更要放后面
                    i2 += lines2

                index += lines

            writer.save()

    generateXlsx(file_xlsx, dict_structure, dict_lines)
    print("全部模块接口文件已生成: {}".format(os.path.join(os.getcwd(), file_xlsx))) # os.getcwd获取当前工作目录
    print("**********************************************************************************************************")

    # 拿到dict_structure, 生成dict_lines之间, 如果指定了-s, 需要重构dict_structure
    if var_s:

        # 遍历dict_structure的时候需要删东西, 所以深拷贝一个出来作为索引
        dict_copy = copy.deepcopy(dict_structure)
        for each in dict_copy:
            m = os.path.join(each, "") in var_s

            if not m:

                # 如果上一级不在var_s里, 其保留不保留就依赖于子分支了
                for each2 in dict_copy[each]:
                    # 由于输入支持life\NH0这种, 所以这里不能简单这么判断, 得加or
                    m2 = os.path.join(each2, "") in var_s or os.path.join(each, each2, "") in var_s

                    if not m2:
                        for each3 in dict_copy[each][each2]:

                            # 三级模块支持只指定三级模块, 和和前面俩模块拼接, 种类比较多
                            m3 = os.path.join(each3, "") in var_s or os.path.join(each, each2, each3, "") in var_s\
                            or os.path.join(each, each3, "") in var_s or os.path.join(each2, each3, "") in var_s

                            if not m3:
                                dict_structure[each][each2].remove(each3)
                            else:
                                # 3级在的时候, m和m2都要改
                                m2, m = True, True

                        # 如果遍历完第三级并没有把m2改过来, 这时候删对应二级模块
                        if not m2:
                            dict_structure[each].pop(each2)

                    else:
                        # 如果2级在里面, 修改m, 告诉第一层循环, 不要删除该模块
                        m = True

                # 如果遍历完子分支并没有把m改过来, 这时候删
                if not m:
                    dict_structure.pop(each)

        # 指定-s的情况, 处理完dict_structure, 再重新计算一次dict_lines
        dict_lines = dict()
        for item in dict_structure:
            for each in dict_structure[item]:
                if item not in dict_lines:
                    dict_lines[item] = defaultdict(int)
                dict_lines[item][each] += len(dict_structure[item][each])

        generateXlsx(file_part, dict_structure, dict_lines)
        print("指定模块接口文件已生成: {}".format(os.path.join(os.getcwd(), file_part)))
        print("**********************************************************************************************************")

    # 如果指定了-s, 打印
    if var_s:
        set_imms = set()
        # 这里不能用前面处理好的dict_structure, 因为对于life这种, dict_structure里是其全量子分支, 而我们需要打印总的
        for each in var_s:
            for item in dict_all:
                # 先假定不匹配
                matched = False

                # 一级模块名life\, 直接判断相等
                if item.count("\\") == 1:
                    if item == each:
                        matched = True
                # 二级模块名, life\NH0\, 则要么输入的是完整的life\NH0, 要么输入的是NH0, 即拆分life\NH0\的第二项在输入里面
                elif item.count("\\") == 2:
                    if item == each or item.split("\\")[1] == each:
                        matched = True
                # 三级模块名, life\NH0\NNH0031, 处理方式类似
                elif item.count("\\") == 3:
                    if item == each:
                        matched = True
                    else:
                        l = item.split("\\")
                        if os.path.join(l[2], "") == each or\
                            os.path.join(l[0], l[2], "") == each or\
                            os.path.join(l[1], l[2], "") == each:
                            matched = True

                if matched:

                    # 只要匹配上, 加到全量结果set里去
                    set_imms |= dict_all[item]

                    print(item[:-1]+": ", end="", flush=True)

                    list_item = sorted(list(dict_all[item]))  # 这里需要先转成有序list

                    if list_item:
                        for i in range(len(list_item)):
                            # 每第13个, 需要换行
                            if i % 13 == 0:
                                print("\n    " + list_item[i], end="", flush=True)
                            else:
                                print(list_item[i], end="", flush=True)

                            if i != len(list_item) - 1:
                                print(", ", end="", flush=True)
                        print("\n")
                    else:
                        print("\n    无\n")

        list_imms = sorted(list(set_imms))

        df = pd.DataFrame({"接口编号": list_imms})

        df.to_excel(file_imms,"Sheet1", index=False, header=True)

        print("指定模块IMMS文件已生成: {}".format(os.path.join(os.getcwd(), file_imms)))
        print("**********************************************************************************************************")

    # 如果指定了投产日期, 将生成的文件都上传50, 没-s上传一个, 有上传3个
    if var_t:
        ftp = FTP()
        try:
            print("登录FTP...", end="")
            ftp.connect(ftp_ip, ftp_port)
            ftp.login(var_n, var_p)
            print("登录成功...")
        except:
            print("登录失败, 请检查网络或更新用户名密码!")
            sys.exit(1)

        ftp.cwd("/PRD_INS")
        try:
            ftp.cwd(var_t)
        except error_perm:
            ftp.mkd(var_t)
            ftp.cwd(var_t)

        try:
            ftp.cwd("MOBS")
        except error_perm:
            ftp.mkd("MOBS")
            ftp.cwd("MOBS")

        try:
            ftp.cwd("HTML")
        except error_perm:
            ftp.mkd("HTML")
            ftp.cwd("HTML")

        print("上传全部模块接口文件...", end="")
        # 注意ftp上传的callback是每上传一个block就回调一次
        with open(file_xlsx, "rb") as f:
            ftp.storbinary("STOR {}".format(file_xlsx), fp=f, blocksize=1024)
            print("上传成功, 路径: /PRD_INS/{}/MOBS/HTML/{}".format(var_t, file_xlsx))

        if var_s:
            print("上传指定模块接口文件...", end="")
            with open(file_xlsx, "rb") as f:
                ftp.storbinary("STOR {}".format(file_part), fp=f, blocksize=1024)
                print("上传成功, 路径: /PRD_INS/{}/MOBS/HTML/{}".format(var_t, file_part))

            print("上传指定模块IMMS文件...", end="")
            with open(file_xlsx, "rb") as f:
                ftp.storbinary("STOR {}".format(file_imms), fp=f, blocksize=1024)
                print("上传成功, 路径: /PRD_INS/{}/MOBS/HTML/{}".format(var_t, file_imms))

        ftp.quit()


if __name__ == "__main__":
    main()
