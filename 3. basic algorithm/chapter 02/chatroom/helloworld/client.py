# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""

import socket
import threading

# 创建socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接主机名和端口号
host, port = socket.gethostname(), 9999
client.connect((host, port))

class RecvThread(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self._socket = socket

    def run(self) -> None:
        while True:
            data = self._socket.recv(1024)
            if data:
                print(data.decode('utf-8'))
            else:
                print("host disconnected")
                self._socket.close()
                break
thread = RecvThread(client)
thread.setDaemon(True)
thread.start()

while True:
    data = input("请输入待发送信息: ")
    if data == 'q': break
    client.send(data.encode("utf-8"))
