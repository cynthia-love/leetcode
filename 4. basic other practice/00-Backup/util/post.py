# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    post请求
"""
from re import search, match
from requests import Session
from datetime import datetime
from json import dumps as json_dumps, loads as json_loads


class CQPost:
    def __init__(self):
        self.session = Session()
        self.base_url = "http://xxx.xxx.xxx.xxx"
        self.login_url = self.base_url + "/cqweb/cqlogin.cq?action=DoLogin"
        self.pull_url = self.base_url + "/cqweb/cqqueryresults.cq"
        self.cqUid = None

    def login(self, username, password):

        params = {
            "loginId": username,
            "password": password,
            "repository": "生产系统变更管理平台",
            "tzOffset": "GMT+8:00",
        }

        try:
            # cq平台的登陆比较特殊, 返回内容无法解析成json
            res = self.session.post(self.login_url, params).text
            self.cqUid = search(r"cqUid:'(.*)'", res).group(1)

        except:
            print("服务器内存不足或登录信息有误, 请重试或重新配置登录信息: -n 用户名 -p 密码！")
            exit(1)

    def pullCQ(self):

        if not self.cqUid:
            print("请先登录获取授权!")
            exit(1)

        params = {
            "action": "ExecuteQuery",
            "resourceId": "cq.repo.cq-query:78051013@生产系统变更管理平台/变更",
            "format": "JSON",
            "startIndex": 1,
            "rowCount": 1 << 31 - 1,
            "refresh": "true",
            "cquid": self.cqUid,
        }
        try:
            res = self.session.post(self.pull_url, params).text
            return json_loads(res)
        except:
            print("拉取CQ单失败！请再次尝试！")
            exit(1)

    def pullDefect(self):

        if not self.cqUid:
            print("请先登录获取授权!")
            exit(1)

        params = {
            "action": "ExecuteQuery",
            "resourceId": "cq.repo.cq-query:78051026@生产系统变更管理平台/变更",
            "format": "JSON",
            "startIndex": 1,
            "rowCount": 1 << 31 - 1,
            "refresh": "true",
            "cquid": self.cqUid
        }
        try:
            res = self.session.post(self.pull_url, params).text
            return json_loads(res)
        except:
            print("拉取CQ单失败！请再次尝试！")
            exit(1)

    def pullCQYear(self, year=None):

        if not self.cqUid:
            print("请先登录获取授权!")
            exit(1)

        if not match(r"^[0-9]{4}$", year):
            print("无效的时间输入!")
            exit(1)

        start_time = year+"-01-01"
        end_time = year+"-12-31"

        params = {
            "action": "ExecuteQuery",
            "resourceId": "cq.repo.cq-query:78051007@生产系统变更管理平台/变更",
            "format": "JSON",
            "startIndex": 1,
            "rowCount": 1 << 31 - 1,
            "refresh": "true",
            "cquid": self.cqUid,
            "data": json_dumps([
                {
                    "fieldPath": "计划更新UAT日期",
                    "op": 9,
                    "valueList": [start_time, end_time],
                    "fieldType": "DATE_TIME",
                    "prompt": "Enter: 计划更新UAT日期",
                    "displayName": "计划更新UAT日期",
                    "choiceListInfo": "null"
                }
            ])
        }
        try:
            res = self.session.post(self.pull_url, params).text
            return json_loads(res)
        except:
            print("拉取CQ单失败！请再次尝试！")
            exit(1)

    def pullDefectYear(self, year=None):

        if not self.cqUid:
            print("请先登录获取授权!")
            exit(1)

        if not match(r"^[0-9]{4}$", year):
            print("无效的时间输入!")
            exit(1)

        start_time = year+"-01-01"
        end_time = year+"-12-31"

        params = {
            "action": "ExecuteQuery",
            "resourceId": "cq.repo.cq-query:78051014@生产系统变更管理平台/变更",
            "format": "JSON",
            "startIndex": 1,
            "rowCount": 1 << 31 - 1,
            "refresh": "true",
            "cquid": self.cqUid,
            "data": json_dumps([
                {
                    "fieldPath": "计划更新UAT日期",
                    "op": 9,
                    "valueList": [start_time, end_time],
                    "fieldType": "DATE_TIME",
                    "prompt": "Enter: 计划更新UAT日期",
                    "displayName": "计划更新UAT日期",
                    "choiceListInfo": "null"
                }
            ])
        }
        try:
            res = self.session.post(self.pull_url, params).text
            return json_loads(res)
        except:
            print("拉取CQ单失败！请再次尝试！")
            exit(1)
