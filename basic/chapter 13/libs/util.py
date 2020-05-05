# -*- coding: utf-8 -*-

# Author: Cynthia

x = 1
def f():
    print("helloworld_子目录")

class C:
    @classmethod
    def cm(cls):
        print("cm_子目录")

    def f(self):
        print("cf_子目录")


# __name__属性自己执行时时__main__, 作为模块导入才是模块名
if __name__ == "__main__":
    print("作为主代码运行而非模块导入")
    f()  # 这里的f(), 只有单独运行该文件(比如用于单元测试)时才会执行

