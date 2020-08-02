# -*- coding: utf-8 -*-
# Author: Cynthia
# 四个attr函数和property一定要记好

"""
    和类相关的内置函数
"""
class C1:
    x = 1

    def __init__(self):
        self.y = 10

class C2:
    pass

class C3(C1, C2):
    pass

c = C3()

print(issubclass(C3, C1))  # True
print(issubclass(C1, (C2, object)))  # 参数2可以是元组, 有一个是就返回True

print(isinstance(c, C3))  # True
print(isinstance(c, C1))  # True, 是子类的实例, 一定也是父类的实例; 同样, 参数2可以是个元组


print(hasattr(C1, "x"))
print(hasattr(c, "x"))  # 这俩输出都是True

print(getattr(c, "x", 10))  # 第三个值表示如果不存在时的默认值; 没有且没给默认则抛AttributeError
print(getattr(c, "y"))  # 实例变量用实例名可访问, 类变量也可用实例名访问; 类名却只能访问类变量

setattr(C2, "m", 100)
print(C2.__dict__)
# 这里要注意!!!c.x能访问到, 但c.m不能, 类实例化之后再修改类不会对已经实例化的实例有影响

setattr(c, "n", 200)
print(c.__dict__)  # 这里的set属性, 既可以给类set, 也可以给实例set

# delattr(C2, "n")  # 这里会报错, 因为用类名访问不到实例变量
delattr(C2, "m")  # m删除的时候得用类名


# property
# 作用就是把属性__size做了一层封装
# 如果c.size赋值取值, 那赋什么取什么
# 但是用property封装后, 赋值100可以取200
class C:
    def __init__(self):
        self.__size = 0
    def setSize(self, value):
        self.__size = value
    def getSize(self):
        return self.__size+100
    def delSize(self):
        del self.__size
    x = property(getSize, setSize, delSize)

c = C()
print(c.x)
c.x = 100
print(c.x)
print(c.getSize())  # 等价于直接这么调
