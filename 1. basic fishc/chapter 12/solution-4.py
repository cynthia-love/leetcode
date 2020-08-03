# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    属性访问
    __getattribute__, __getattr__什么的不要轻易用
    除非像是给dict添加.访问符, 给class添加[]访问符等特殊的场景
    一般情况下都是对单个变量增加特殊操作, 用property就够了
    要么就是加点属性不存在时的操作, 也只会用到__getattr__而用不到__getattribute__

    还要注意一点, __setattr_是和__getattribute__同等地位的而不是__getattr__
    但凡是赋值语句, 都会先过__setattr_
"""

class C:
    x = 1

    def __init__(self):
        self.y = 2

    def getY(self):
        return self.y
    def setY(self, v):
        self.y = v
    def delY(self):
        del self.y

    p = property(getY, setY, delY)

c = C()
# 方式1, 点操作符, 支持用实例名获取类属性
print(c.x)
# 方式2, 获取dict后用key值访问, 不支持用实例名获取类属性
print(c.__dict__['y'])
# 方式3, getattr函数, 支持用实例名获取类属性
print(getattr(c, "x", -1))   # -1表示取不到时的返回值
# 方法4, 通过property函数间接访问
print(c.p)

print("************************")

class C:
    def __getattribute__(self, item):
        print("调用__getattribute__")
        try:
            return super().__getattribute__(item)
            # return super().__dict__[item]
            # 不建议这种写法, 因为要的属性不一定是__dict__里的
            # 另外注意, 这里写的是super(), 而不是self, 也不是super
            # 如果写self, self.__dict__也会触发__getattribute__陷入死循环
            # 而super是父类不是父类实例, 也不可取, 实际上super()等价于self?
            # 好像也不是, 完全等价的话应该和self调到的是同一个函数啊...
        except AttributeError:
            # 注意__getattribute__调__getattr__的原理是其抛AttributeError错, 而不是直接调
            # 所以这里如果还想继续触发__getattr__, 那么得手动raise AttributeError
            raise AttributeError

    def __getattr__(self, item):
        print("调用__getattr__")

c = C()
print(c.x, c.__dict__, hasattr(c, 'x'), getattr(c, 'x'))
# 经测验, 上面四种写法都会触发__getattribute__, 其中1, 3, 4还会触发__getattr__
# 那么在__getattribute__内部就不能再用这几种写法获取属性值

print("*********")
class C:
    def __getattribute__(self, item):
        print("访问了__getattribute__")
        try:
            return super().__getattribute__(item)
        except AttributeError:
            raise AttributeError

    def __setattr__(self, key, value):
        print("访问了__setattr__")
        # self.__dict__[key] = value # 这种写法因为有self.__dict__还会去访问__getattribute__
        super().__setattr__(key, value)  # 第一种和这种写法都是可以的, 只要不重复触发自己就行
        # setattr(self, key, value), 这种写法会触发__setattr__导致陷入死循环, 不可取


c = C()
c.x = 100  # 这么写不会去触发__getattribute__
print(c.x)