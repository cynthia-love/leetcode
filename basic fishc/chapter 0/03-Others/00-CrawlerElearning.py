# -*- coding: utf-8 -*-

# Author: Cynthia
import re
import time
import requests
from requests.cookies import RequestsCookieJar

cookie_jar = RequestsCookieJar()
cookie_jar.set("YII_CSRF_TOKEN", "xxxxx", domain="elearning.bankcomm.com")
cookie_jar.set("regenerateSessionID", "xxxxx", domain="elearning.bankcomm.com")
cookie_jar.set("snspSessId", "xxxxx", domain="elearning.bankcomm.com")
cookie_jar.set("snspUserId", "xxxxx", domain="elearning.bankcomm.com")

url = "http://elearning.bankcomm.com/?r=course/course/view&id={id}"

with open("result.txt", "a") as fout:
    for i in range(300000, 400000, 1):
        time.sleep(0.3)
        res = requests.get(url.format(id=str(i)), cookies=cookie_jar)

        result1 = re.search(u"课程时长&nbsp;:&nbsp;&nbsp;([0-9]+.[0-9]+)", res.text)
        hour = result1.group(1) if result1 else None

        result2 = re.search(r"paragraph-unstudy", res.text)

        print(i, hour, result2)
        if result2 and hour and float(hour) >= 1.5:
            print("写入文件...")
            fout.write(hour+"\t"+url.format(id=str(i))+"\n")
            fout.flush()
