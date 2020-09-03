# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    面向对象中的命名空间

    类空间, 包括所有直接在类定义体内的声明(一个类的所有实例所共享的成员或没有引用任何特定实例的成员)
    实例空间, 即使使用了继承, 每个对象仍有单一的实例命名空间

    o.xxx名称解析顺序:
    1. 在实例命名空间中搜索
    2. 在该实例所属的类的命名空间搜索
    3. 在所属类的父类的命名空间搜索
    4. 一直往上找, 最后找不到, 抛出AttributeError
"""

class A:
    def __init__(self):
        self.x = 1

    classvar = 1

    def classf(self):
        pass

    class B:
        def ccf(self):
            pass

class C(A):
    def __init__(self):
        self.y = 1
        super().__init__()

    classCvar = 1

    def classCf(self):
        pass

a = A()
c = C()

print(A.__dict__.keys())  # 实例成员函数也是在类空间里的, 因为是所有实例共享
# '__module__', 'classvar', 'classf', 'B', '__dict__', '__weakref__', '__doc__'
print(C.__dict__.keys())
# '__module__', 'classCvar', 'classCf', '__doc__'
print(a.__dict__.keys())  # 'x'
print(c.__dict__.keys())  # 'y', 'x'


# 嵌套类的使用
class LinkedList:

    class Node:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.head

    def add(self, value):
        node = self.Node(value)
        self.tail.next = node
        self.tail = self.tail.next

    def show(self):
        current = self.head
        while current != self.tail:
            current = current.next
            print(current.value)

ll = LinkedList()
ll.add(3)
ll.add(4)
ll.add(5)
ll.show()


# slots声明, 给用descriptor代替__dict__
# 1. 可以提升属性访问速度
# 正常情况下, o.x -> o.__dict__ -> o.__dict__['x']->结果
# slots情况下: o.x -> descriptor直接get->结果
# 比正常情况下少了o.__dict__['x']这步, 一个哈希函数的速度消耗
# 2. 减少内存消耗
# __dict__是一个哈希表, 哈希以空间换时间, 当字典使用量超过2/3时
# python会根据情况进行2-4倍的扩容, 所以取消__dict__的使用可以大幅减少空间消耗
class Slots:
    # 一旦这么声明了, 那后面self就不能访问其它变量名了
    __slots__ = ['name', 'age']

    def __init__(self):
        self.name = 'Jim'
        self.age = 18

s = Slots()  # 'Slots' object has no attribute '__dict__'
print(s.name)
