# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改Vector的__mul__, 使得其同时支持v*k, v*v
    注意进行运行时类型检查
"""

"""
    这里演示一下装饰器
    包括函数装饰器, 和类装饰器
"""

# 1. 先看一下前面提到的装饰器模式

class A:
    def __init__(self):
        self.x = 100

class KeyDecorator:
    def __init__(self, obj):
        self._obj = obj

    def __getitem__(self, item):
        return self._obj.__dict__.get(item)

    def __getattr__(self, item):
        return getattr(self._obj, item)

a = A()
key_decorator = KeyDecorator(a)
print(a.x, key_decorator.x, key_decorator['x'])

# 2. 上面那种方式也不是不行, 但不够简洁, 且不能用@xxx语法糖
# 下面演示更加规范的装饰器模式, 所谓装饰器, 即增强函数或类的功能, 附魔
# 几个概念: 原函数, 实际执行的函数
def decorator(func):

    def wrapper(*args, **kwargs):
        print("原函数执行前进行这里操作")
        f = func(*args, **kwargs)  # 执行原函数, 并拿到返回值; 参数原封不动传进去
        print("原函数执行后进行这里操作")
        return f  # 这里还可以对原函数的返回值进行装饰

    return wrapper  # 注意这里, 装饰函数返回的是装饰后的函数

@decorator
def f(x):
    print("进入function f, 看看能不能拿到参数", x)
    return "return of function f"

print(f(888))

# 3. 进阶用法, 装饰器本身带参数(注意不是传给原函数的参数)
# 其实没那么难理解, 思想可以类比工厂模式, 感觉意义不大

def decoratorFactory(type):
    def decorator1(func):
        def wrapper(*args, **kwargs):
            print("something before 111")
            f = func(*args, **kwargs)
            print("something after 111")
            return f

        return wrapper

    def decorator2(func):
        def wrapper(*args, **kwargs):
            print("something before 222")
            f = func(*args, **kwargs)
            print("something after 222")
            return f

        return wrapper

    return decorator1 if type == "1" else decorator2

@decoratorFactory("1")
def f():
    print("function f 111")
f()
@decoratorFactory("2")
def f():
    print("function f 222")
f()

# 4. 进阶用法, 用类装饰函数, 思路大同小异, 无非是利用对象的__call__可执行性
# 治理系统自动帮忙retur了__call__
class Decorator:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print("class decorator before")
        res = self._func(*args, **kwargs)
        print("class decorator after")
        return res

@Decorator
def f():
    print("function f")
f()

# 注意, 用类装饰函数还有一种方式, 即仅利用其__call__方法(其实例callable)
class Decorator:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("hahhahahaha start")
            func()
            print("hahahhahaha end")
        return wrapper

@Decorator()
def f():
    print("hahahhahahah f")
f()
# 5. 进阶用法, 用函数装饰类, 本质上是装饰__new_方法
def decorator(cls):
    def wrapper(*args, **kwargs):
        print("function decorate class before")
        res = cls(*args, **kwargs)

        # 给类装饰__getitem__方法
        def f(self, item):
            return self.__dict__.get(item)

        setattr(cls, "__getitem__", f)

        print("function decorate class after")
        return res
    return wrapper

@decorator
class C:
    def __new__(cls, *args, **kwargs):
        print("new...")
        return super().__new__(cls)

    def __init__(self, a):
        self.a = a

c = C(100)
print(c['a'])

# 6. 用类装饰类, 其实没啥用, 不过有时候需要存储点东西, 比如单例
class singleton:
    def __init__(self, cls):
        self._instance = {}
        self._cls = cls

    # 注意这里, 只是给目标类添加方法, 不需要带入自身类信息, 要声明为静态函数
    @staticmethod
    def __getitem__(self, item):
        return self.__dict__.get(item)

    def __call__(self, *args, **kwargs):
        print(type(self))
        print("class decorate class before")
        if self._cls.__name__ in self._instance:
            res = self._instance[self._cls.__name__]
            # 注意这种单例写法与之前的直接需改类自身__new__实现的单例写法的不同
            # 直接修改__new__自身, 哪怕是从缓存里取的类, return完还是会去执行__init__
            # 而这里对__new__进行装饰, 上面这个逻辑直接就不去执行__new__了, 自然就不会去触发__init__
            # 所以这种写法, 声明一个新instance, 不光是单例, 数据成员值也不会改变
            # 要么手动去执行__init__, 注意首参数是res
            # self._cls.__init__(res, *args, **kwargs)
        else:
            if not hasattr(self._cls, "__getitem__"):
                setattr(self._cls, "__getitem__", singleton.__getitem__)
            res = self._cls(*args, **kwargs)
            self._instance[self._cls.__name__] = res

        print("class decorate class after")
        return res

@singleton
class C:
    def __init__(self, x):
        print("yes")
        self.x = x

c = C(88)
print(c['x'])
c2 = C(99)
print(c2['x'])
print(id(c), id(c2))

# 经过上面的学习, 参数校验就知道怎么做了, 用函数去校验函数就行
from typing import Sequence

# 试了下, 好像没办法写到类里面去
def check(func):
    def wrapper(self, other):
        if isinstance(other, (int, float)) or isinstance(other, Vector):
            return func(self, other)
        else:
            raise TypeError

    return wrapper

class Vector:
    def __init__(self, l):
        self._l = l

    def __len__(self):
        return len(self._l)

    def __getitem__(self, item):
        return self._l[item]

    @check
    def __mul__(self, other):
        # ...这个例子用decorator好像意义不大
        if isinstance(other, Vector):
            return sum(self[i]*other[i] for i in range(len(self)))
        else:
            return Vector([x*other for x in self])

v1 = Vector([1, 2, 3, 4])
v2 = Vector([1, 2, 3, 4])
v3 = v1*3
v4 = v1*v2
print([x for x in v3], v4)