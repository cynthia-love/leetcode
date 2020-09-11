# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    模拟网络应用程序的一方A, 定期发给另一方B信息
    互联网不断地检查A是否有想发送的信息, 有就发送给B
    B定期检查, 如果有收到包, 那么就阅读并删除包
"""
"""
    用中介者模式模拟
    思路: User对象维护一个发送mq, 一个接收mq
    User1和User2向中介者注册后, 中介者定期去检测
    User1的发送mq有没有内容, 有的话就把内容取出来, 发给User2的接收mq
    
    User2定期检查自己的接收mq, 有内容就取出来打印
"""
import threading
import time
from collections import deque
class User(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self._mq_s = deque()  # 发送消息队列
        self._mq_r = deque()  # 接收消息队列

    def getMQS(self):
        return self._mq_s

    def getMQR(self):
        return self._mq_r

    def sendMessage(self, val):
        self._mq_s.append(val)

    def receiveMessage(self):
        print("{} 接收到信息: {}".format(self.name, self._mq_r.popleft()))

    def run(self):
        while True:
            if self._mq_r:
                self.receiveMessage()

class Mediator(threading.Thread):
    def __init__(self, sender, receiver):
        threading.Thread.__init__(self)
        self._sender = sender
        self._receiver = receiver

    def run(self):
        mq_s = self._sender.getMQS()
        mq_r = self._receiver.getMQR()
        while True:
            if mq_s:
                print("{} 向 {} 发送信息!".format(self._sender.name, self._receiver.name))
                mq_r.append(mq_s.popleft())


user1 = User("Jim")
user2 = User("Lucy")

m = Mediator(user1, user2)

user2.setDaemon(True)
user2.start()

m.setDaemon(True)
m.start()

while True:
    s = input("请输入待发送内容: ")
    user1.sendMessage(s)
    time.sleep(0.1)
