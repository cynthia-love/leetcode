# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    模拟一个聊天室, 支持多人同时在线
    注意, 收信息要启一个线程
"""

import socket
import weakref
import threading

# 创建socket对象
# 第一个参数为套接字家族, 可以是AF_UNIX或者AF_INET
# 前者本机通信首选, AF_INET则用于跨机器之间的通信
# 第二个参数可以是SOCK_STREAM(面向连接)和SOCK_DGRAM(非连接)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定主机名和端口号
host, port = socket.gethostname(), 8093
server.bind((host, port))

# 设置最大连接数, 超过后排队
server.listen(10)
print("server start!")
print("==============================")

class RecvThread(threading.Thread):
    # ip和socket映射用weakref存, 可以自动清理
    ip2cs = weakref.WeakValueDictionary()

    def __init__(self, cs, ca):
        threading.Thread.__init__(self)
        self._cs = cs
        self._ca = ca

    def run(self) -> None:
        while True:
            data = self._cs.recv(1024)
            if data:
                # print(data.decode('utf-8'))
                # self._cs.send("host: message received".encode('utf-8'))
                data = data.decode('utf-8')
                # 要求客户端发送信息格式ip:port|message
                target, message = data.split("|")
                if target in RecvThread.ip2cs:
                    RecvThread.ip2cs[target].send(message.encode("utf-8"))
                else:
                    print("illegal client target")
            else:
                print("{}:{} disconnected".format(self._ca[0], self._ca[1]))
                self._cs.close()
                break

while True:
    # 建立客户端连接, cs为客户端socket, ca为客户端(ip, port)
    # 服务端可以通过client_socket给客户端发信息以及关闭连接
    cs, ca = server.accept()
    print("connected from {}:{}".format(ca[0], ca[1]))

    RecvThread.ip2cs["{}:{}".format(ca[0], ca[1])] = cs

    thread = RecvThread(cs, ca)
    thread.setDaemon(True)
    thread.start()