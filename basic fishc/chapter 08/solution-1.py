# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    永久存储
"""

"""
    文件
"""

f1 = open("data/data.txt", "r")
print(f1.read(7))  # 按照指定长度以字符串形式读入, 不指定大小则读入全部; abcde\nf
f1.close()
f2 = open("data/data.txt", "w")  # w, 以写入的方式打开, 没有新建有覆盖
f2.write("hahahha")
f2.close()
f3 = open("data/data.txt", "a")  # a, 以追加的方式打开, 没有新建有追加
f3.write("worldworld")
f3.close()
f4 = open("data/data.byte", "wb")  # 二进制写打开, 没有新建有覆盖
f4.write("bytestr".encode("utf-8"))
f4.close()
f5 = open("data/data.byte", "ab")  # 二进制追加打开, 没有新建有追加
f5.write("byteadd".encode("utf-8"))
f5.close()
f6 = open("data/data.byte", "rb")  # 二进制读打开
print(f6.read(5))  # 二进制读的时候一般会指定长度
f6.close()

# 此外, 还有一种+, 与r, w, a结合使用, 一般不要这么用, 读写在一块文件指针需要自己控制
# 给r添加写能力, 文件不存在报错; 存在不清空; 初始指针在文件首
with open("data/data.txt", "r+") as f:
    print(f.read())  # 读, 指针到文件尾
    f.write("fugai")  # 尾部写入
    print(f.read())  # 尾部读, 会读出来空

# 给w添加读能力, 文件不存在新建; 存在清空; 初始指针在文件首
with open("data/data.txt", "w+") as f:
    print(f.read())
    f.write("haha")
    f.seek(0, 0)  # 参数1表示移动多少个字节, 参数2表示参考位置, 参数2取值: 0起始, 1当前, 2末尾
    print(f.read())  # 由于有写操作, 需要手动操作指针到文件首才能读出来内容

# 给a添加读能力, 文件不存在新建; 存在不清空; 初始指针在文件尾
with open("data/data.txt", "a+") as f:
    print(f.read())
    f.write("aa")
    f.seek(0, 0)
    print(f.read())


# 其他方法
# with open("data2.txt", "w") as f:
#     f.writelines(["aaa", "bbbb", "cccc"])  # 注意writelines不会自动添加换行
with open("data/data2.txt", "r") as f:
    print(f.readlines())  # 注意readlines也不会自动去掉\n, ['aaabbbbcccc\n', 'aaaaaaaaaaa']

with open("data/data2.txt", "r") as f:
    print([f.readline(), f.readline(), f.readline()])
    # readline遇到\n结束, 但也不会自动去掉\n, ['dfadfadf\n', 'adfadfdf\n', 'adfj']

with open("data/data2.txt", "r") as f:
    for line in f: print(line)  # f本身也是个可迭代对象, 可直接遍历


# 一个小练习题, 处理三段对话后分别按说话人保存成6个文件

def saveFile(boy, girl, count):
    with open("data/boy_"+str(count)+".txt", "w") as f:
        f.writelines(boy)
    with open("data/girl_"+str(count)+".txt", "w") as f:
        f.writelines(girl)

def splitFile(filename):
    # count表示当前读的第几段
    boy, girl, count = [], [], 1
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("Jim"):
                name, spoken = line.split(":", 1)
                boy.append(spoken)
            elif line.startswith("Lucy"):
                name, spoken = line.split(":", 1)
                girl.append(spoken)
            else:
                saveFile(boy, girl, count)
                count += 1
                boy.clear()
                girl.clear()
        saveFile(boy, girl, count)  # 注意, 最后一行是Jim, 循环退出后还得存一次; count是前加, 所以这里不用+1

splitFile("data/record.txt")
