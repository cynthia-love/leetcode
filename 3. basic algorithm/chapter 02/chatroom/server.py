# -*- coding: utf-8 -*-
# Author: Cynthia
"""
    服务端不需要界面
    主线程接受来自客户端的连接, 最大10
    支线程接受来自客户端的信息, 信息格式ID:message
    首次连接成功后要单独把ID发过来
"""

import socket
import weakref
import threading

# AF_INET用于跨机器通信; SOCK_STREAM表示面向连接
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host, port = socket.gethostname(), 8088
server.bind((host, port))

server.listen(10)  # 最大连接数10
print("server start!")
print("==============================")

class RecvThread(threading.Thread):

    id2cs = weakref.WeakValueDictionary()

    def __init__(self, id, cs, ca):
        # 这里不能用super()
        threading.Thread.__init__(self)
        self._id = id  # 用户id
        self._cs = cs  # 当前socket
        self._ca = ca  # 用户ip,端口

    def run(self):
        while True:
            data = self._cs.recv(1024)
            if not data:
                print("{}:{} disconnected".format(self._ca[0], self._ca[1]))
                self._cs.close()
                break
            data = data.decode('utf-8')
            if ":" not in data: continue  # 不合法的信息直接丢失
            target, message = data.split(":")
            if target not in RecvThread.id2cs: continue  # 无效的目标用户则信息直接丢失
            RecvThread.id2cs[target].send((self._id+":"+message).encode('utf-8'))

while True:
    cs, ca = server.accept()
    print("connected from {}:{}".format(ca[0], ca[1]))
    id = cs.recv(1024).decode('utf-8')
    print(id)
    RecvThread.id2cs[id] = cs

    thread = RecvThread(id, cs, ca)
    thread.setDaemon(True)
    thread.start()