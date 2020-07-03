# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    Mixin, 一种特殊的继承
    (后面还有个Descriptor的概念, Mixin更像是功能组件, Descriptor更像是变量组件)

    这里的父类不是各种有意义的独立概念, 而是功能组件, 一个组件只实现一种功能
    一般的继承里, 父类鱼, 子类金鱼, 实际上子类是父类的一种
    而这里的继承, 父类是通用材料, 比如我要打造一把吸血剑, 传统的继承方式是剑(父类)->吸血剑(子类)
    而Mixin是把吸血特性摘出来, 吸血(父类组件)->子类(剑), 这么干的好处是更通用
    比如可以轻松实现吸血、破防、上毒->剑; 或者把子类剑换了, 给刀附魔, 吸血->子类(刀)

    由于要实现通用性特定类无关, Mixin经常会用到各种各样的类隐藏属性动态去获取各种东西

    比如dict, 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__里的

　　对象的__dict__中存储了一些self.xxx的一些东西; 多继承里, 每个类一个__dict__, 对象一套__dict__

"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p = Person("小陈", 18, "男")
print(p.name)
# print(p.grade), 'Person' object has no attribute 'grade'

# 写一个功能组件类, 当用户试图获取一个不存在的属性时
class KeyError:
    def __getattr__(self, name):
        print("不存在的实例属性!!!")

class Person2(KeyError):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p2 = Person2("小李", 20, "女")
print(p2.name)
print(p2.grade)  # 这里不会抛出错误, 而是会走到__getattr__函数

# 有时候, 给类加特性组件不能重新写一遍类, 可以再声明个子类, 将他们混合起来
class Person3(Person, KeyError):  # 将一个基类和一对特性组件基类混合到一起得到一个新类
    pass  # 子类无需特殊处理时, 不用再写一个init往父类传构造函数参数

p3 = Person3("小王", 30, "男")  # 上面子类没写init, 也没有调父类构造函数传参, 这里会直接套用父类构造函数
print(p3.grade)


# 特别地, 讲一下__dict__
# 类一个, 实例一个; 存在继承时, 每个父类一个, 子类一个, 实例一个
class C:
    cv = 1
    @classmethod
    def cm(cls):
        print("cm")
    @staticmethod
    def sm():
        pass

    def __init__(self):
        self.iv = -1

    def f(self):
        pass

c = C()
print(C.__dict__)
"""
{
    '__module__': '__main__', 
    'cv': 1, 
    'cm': <classmethod object at 0x10faaf110>, 
    'sm': <staticmethod object at 0x10faaf150>, 
    '__init__': <function C.__init__ at 0x10fa65050>, 
    'f': <function C.f at 0x10faace60>, 
    '__dict__': <attribute '__dict__' of 'C' objects>, 
    '__weakref__': <attribute '__weakref__' of 'C' objects>, 
    '__doc__': None}
"""
print(C.__dict__)
"""
{
    '__module__': '__main__', 
    'cv': 1, 
    'cm': <classmethod object at 0x10901efd0>, 
    'sm': <staticmethod object at 0x10901ef50>, 
    '__init__': <function C.__init__ at 0x108fd8050>, 
    'f': <function C.f at 0x10901fe60>, 
    '__dict__': <attribute '__dict__' of 'C' objects>, 
    '__weakref__': <attribute '__weakref__' of 'C' objects>, 
    '__doc__': None}


"""
print(c.__dict__)
"""
    {'iv': -1}
"""
c.cm()  # 这里是能访问到的

# 小测验, 给Person类Mixin根据key值访问实例变量
class KeyRefer:
    def __getitem__(self, key):
        # return self.__dict__[key]
        return self.__dict__.get(key)

class Person3(Person, KeyRefer):
    pass

p3 = Person3("Jim", 20, "男")
print(p3.name)
print(p3['name'])