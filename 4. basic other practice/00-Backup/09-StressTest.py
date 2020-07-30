# -*- coding: utf-8 -*-

# Author: Cynthia

"""

"""
from json import loads as json_loads, dumps as json_dumps
from threading import Thread
from requests import Session
from time import sleep
from datetime import datetime
def main():

    session = Session()

    url_login = "http://xxx.xxx.xxx.xxx:xxxx/MOBS4-UAT/MOBS.MOBS-LOGIN.V-1.0/MB0000.do"

    url_ps0001 = "http://xxx.xxx.xxx.xxx:xxxx/MOBS4-UAT/MOBS.MOBS-APP.V-1.0/PS0001.do"
    url_sl0000 = "http://xxx.xxx.xxx.xxx:xxxx/MOBS4-UAT/MOBS.MOBS-APP.V-1.0/SL0000.do"

    class APIThread(Thread):
        def __init__(self, url):
            Thread.__init__(self)
            self.url = url

        def run(self) -> None:
            print(self.name+"开始执行")
            params = {
                "sltCity":"上海",
                "brachNo":"01310999999"
            }

            try:
                # 注意这里没有用json.dumps，和后台服务器的要求有关系
                # 如果从fiddler里看到是JSON形式的，得dumps；如果是a=xx&b=xx&c=xx的，不要dumps
                session.post(self.url, data=params)
                print(self.name+"接口调用成功")
            except:
                print("调用失败")
                exit(1)

    thread_list = []
    for i in range(100):
        thread_list.append(APIThread(url_sl0000))

    print(datetime.now())
    for i in range(100):
        thread_list[i].start()
    print(datetime.now())
    print("主程序退出")


if __name__ == "__main__":
    main()