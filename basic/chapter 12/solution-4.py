# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    属性访问
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
print(getattr(c, "x", -1))
# 方法4, 通过property函数间接访问
print(c.p)

print("************************")
class C2:
    """
    def __getattribute__(self, item):
        print("访问属性时先执行")
        raise AttributeError
        # 如果自己写了getattribute, 那么这里得自己抛异常, 才有可能在属性不存在时触发getattr函数
        # 感觉自己写了这个就没必要再写getattr了, 因为要抛异常总得先判断出来属性存在不存在
    """
    def __getattr__(self, item):
        print("getattrbute抛出AttributeError时执行")
        return -1

    def __setattr__(self, key, value):
        print("设置属性时执行")
        # 这个函数比较特殊, 但凡属性赋值都会触发
        # self.x = 1  # 不能这么写, 会死循环, 这里面的代码不能触发自己
        # 办法1, 借用基类的赋值, 不会触发子类的setattr; 没继承的基类是object
        # super().__setattr__("x", 1)
        # 办法2, 借用__dict__, 用key/value赋值不会触发setattr
        self.__dict__["m"] = 2
        # 注意用这种写法, 那上面的__getattribute__如果自己写, 别忘了返回dict
        # self.__dict__也会触发__getattribute__

    def __delattr__(self, item):
        print("删除属性时执行")

c2 = C2()
print(c2.x)
c2.y = 3