# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import sys
import socket
import threading
from tkinter import *
from tkinter.ttk import *  # ttk比tk更好看, 同名组件优先用ttk的
from tkinter.messagebox import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.geometry("+600+300")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class LoginFrame:
    def __init__(self, parent, f1, f2):
        # 自定义组件里的东西最好用一个frame包起来, 便于统一操作
        self._frame = Frame(parent)

        Label(self._frame, text="Host: ").grid(row=1, column=1, columnspan=2)
        self._host = Entry(self._frame)
        self._host.grid(row=1, column=3, columnspan=3)

        Label(self._frame, text="ID: ").grid(row=2, column=1, columnspan=2)
        self._id = Entry(self._frame)
        self._id.grid(row=2, column=3, columnspan=3)

        Button(self._frame, text="退出", command=f1).grid(row=3, column=2, columnspan=2, pady=15)
        Button(self._frame, text="登陆", command=f2).grid(row=3, column=4, columnspan=1, pady=15)

    def grid(self, *args, **kwargs):
        self._frame.grid(*args, **kwargs)

    def pack(self, *args, **kwargs):
        self._frame.pack(*args, **kwargs)

    def grid_forget(self):
        self._frame.grid_forget()

    def pack_forget(self):
        self._frame.pack_forget()

    def get_host(self):
        # host, port = self._host.get().split(':')
        # return host, int(port)
        return socket.gethostname(), 8088

    def get_id(self):
        return self._id.get()

class ChatFrame:
    def __init__(self, parent):
        self._frame = Frame(parent)
        self._text = ScrolledText(self._frame, state=DISABLED, width=50, height=20)
        self._text.pack()

        self._target = Entry(self._frame, width=5)
        self._target.pack(side=LEFT)

        self._message = Entry(self._frame, width=25)
        self._message.pack(side=LEFT)

        Button(self._frame, text='发送', command=self.send_message).pack(side=RIGHT)

    def send_message(self):
        target = self._target.get()
        message = self._message.get()
        self.add_content("->"+target+": "+message+'\n')
        client.send((target+":"+message).encode('utf-8'))

    def clear_content(self):
        # DISABLED状态不光用户不能编辑, delete, insert也无效...
        self._text.configure(state=NORMAL)
        self._text.delete(1.0, END)
        self._text.configure(state=DISABLED)

    def get_content(self):
        return self._text.get(1.0, END)

    def add_content(self, value):
        self._text.configure(state=NORMAL)
        self._text.insert(END, value)
        self._text.configure(state=DISABLED)

    def pack(self, *args, **kwargs):
        self._frame.pack(*args, **kwargs)

    def pack_forget(self):
        self._frame.pack_forget()

class RecvThread(threading.Thread):
    def __init__(self, f):
        threading.Thread.__init__(self)
        self._f = f

    def run(self) -> None:
        self._f()

def f1():
    root.quit()

# 函数体里面的变量可以先写后声明, 比如这里的login_frame
# 除了这么写, 还可以给个self参数, 子组件类调方法的时候把自身self传进去
def f2():
    host, port = login_frame.get_host()

    try:
        client.connect((host, port))
    except OSError:
        showerror("提示", "\n连接失败, 请检查服务器地址!")
        return

    client.send(login_frame.get_id().encode('utf-8'))

    def f():
        while True:
            data = client.recv(1024)
            if data:
                origin, message = data.decode("utf-8").split(':')
                chat_frame.add_content(origin+": "+message+'\n')
            else:
                showerror("提示", "\n服务器断开连接, 点击退出!")
                sys.exit()

    thread = RecvThread(f)
    thread.setDaemon(True)
    thread.start()

    login_frame.pack_forget()

    chat_frame = ChatFrame(root)
    chat_frame.pack()

login_frame = LoginFrame(root, f1, f2)

login_frame.pack()
login_frame.pack_forget()

chat_frame = ChatFrame(root)
chat_frame.pack()

root.mainloop()

