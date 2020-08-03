# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    描述符
    描述符, 是将某种特殊类型的类实例指派给另一个类的属性

    大概总结了下, 如果说Mixin像是方法组件化, 可以动态给类混入功能特性
    那么描述符就是变量组件化, 将一类具有同样特点的变量封装起来
    比如某些变量, 存100, 取得时候就会减少10

    一般情况下, 用property就够了
    除非你写这个东西是真的是给其他人用的
"""
class Descriptor:
    # 这么记, __get__是变量组件用的, 对外
    # __getattribute__是类自己用的, 对内
    def __get__(self, instance, owner):
        # self为描述符自身实例, instance为这个描述符拥有类的实例, owner为描述符拥有类
        print("get", instance, owner)
        return self.m-10  # 这里变量名无所谓, 反正对外隐藏
        # 像是这里的取值时减10就是一种特殊性质
        # 如果特殊性质很多, 每个类自己写会很麻烦
        # 不如封装成组件

    def __set__(self, instance, value):
        print("set", instance, value)
        self.m = value

    # 注意这里是delete不是del, del是析构函数
    def __delete__(self, instance):
        print("del")
        pass

class C:
    x = Descriptor()  # 和前面的property几乎一样, 只不过property的三个函数要自己传进去
    # 如果C自己写变量x的特殊行为也可以, 但是不如封装好了直接拿过来方便

c = C()
c.x = 100
print(c.x)  # get <__main__.C object at 0x10c440150> <class '__main__.C'>
# C.x = 200  注意这里不能这么写, 虽然x前没加self, 但是其实是实例属性而不是类属性
# print(c.x) 如果这里写了C.x, 会将原x覆盖的(写在类里的实例属性, 如果类里加了个同名属性, 原来的就没了)


# 实例, 封装两个温度数据类
class Celsius:
    def __set__(self, instance, value):
        # 虽然instance指向调用类实例, 但不建议过多交互
        # 并不知道instance里给变量起什么名字
        self.cel = float(value)

    def __get__(self, instance, owner):
        return self.cel

class Fahrenheit:
    # 琢磨下Fahrenheit为什么这么写, 只能单向去不能双向, 双向会陷入死循环
    def __set__(self, instance, value):
        # 注意这里不能写成instance.cel.cel, 不然没法触发Celsius的__set__
        instance.cel = (float(value)-32)/1.8

    def __get__(self, instance, owner):
        return instance.cel*1.8+32

    # 这里相当于用到了CT的实例里的cel
    # 不建议这么干, Descriptor封装应该具有通用性

class CT:
    cel = Celsius()
    fah = Fahrenheit()

ct = CT()
ct.cel = 100
print(ct.cel, ct.fah)
ct.fah = 200
print(ct.cel, ct.fah)


# ***************************************************************
# 自己去写一个property类
# 与descriptor相比, property类更抽象了一步, 连__set__, __get__, __delete__都得外部写完传进去
# 但是不建议这么写, 因为默认传入的self参数就不是property类自己的了, 而是C的
class propertym:
    def __init__(self, getm, setm, delm):
        self.getm = getm
        self.setm = setm
        self.delm = delm

    def __set__(self, instance, value):
        # 这里调用, 系统无法自动给setX传实例的self, 所以调用需要显式传
        self.setm(instance, value)

    def __get__(self, instance, owner):
        return self.getm(instance)

    def __delete__(self, instance):
        self.delm(instance)

class C:
    def __init__(self):
        self._x = 1
    def getX(self):
        return self._x
    def setX(self, value):
        self._x = value
    def delX(self):
        del self._x

    x = propertym(getX, setX, delX)

c = C()
c.x = 10
print(c.x)

# ***************************************************************
# 还可以更进一步, 直接用property函数, 都不用独立类了, 强烈推荐
# 注意一点, init里的是self._x, 而后面声明的变量是x, 这样可以实现init里初始化
# 如果init里直接写self.x会报错
class C:
    def __init__(self):
        self._x = None

    def _getX(self):
        return self._x+1000

    def _setX(self, value):
        self._x = value

    x = property(_getX, _setX)

c = C()
c.x = 1
print(c.x)
