# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    继承
    比较一下函数-子函数, 类-实例, 父类-子类中的各种访问/覆盖关系
    (觉得乱那就尽量不要搞同名的变量/函数)
"""
# 0. 书上的例子
import random

class Fish:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        self.x += 1
        print("我移动到了({},{})".format(self.x, self.y))

class Goldfish(Fish):
    pass
    # 金鱼和鱼一模一样， 纯粹为了区分单独声明了个类， 无新变量、函数
    # 子类不声明init时， 系统会自动调父类的init

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self), 这么调称为调用未绑定的父类方法， 可以但不推荐
        super().__init__()  # 建议这么干
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃了")
            self.hungry = False
        else:
            print("饱了")

fish = Fish()
fish.move()

goldFish = Goldfish()
goldFish.move()
goldFish.move()

shark = Shark()
shark.move()
shark.move()
shark.eat()
shark.eat()


# 1. 全局变量-函数变量; 同名覆盖, 外部仍存在, 无法访问
p1v1, p1v2, p1v3 = 1, 2, 3
def p1f():
    print(p1v1)  # 函数内部可直接访问全局变量
    p1v2 = -2  # 函数内部声明同名变量, 会自动降级为局部变量, 之后没有任何办法再访问到外部同名变量
    print(p1v2)
    global p1v3  # global参数声明后, 函数内部可直接修改全局变量
    p1v3 = -3
    print(p1v3)
p1f()
print(p1v1, p1v2, p1v3)  # 1, -2, -3 VS 1 2 -3, 发现只有v3被改变了

# 2. 类变量-实例变量; 无同名, 类名、self都能访问外部; 同名覆盖, 外部仍存在, 类名访问外, self访问内
class P2Class:
    p2c1 = 1
    p2c2 = 2

    def __init__(self):
        print(P2Class.p2c1, self.p2c1)  # 类内部, 可通过类名, self去访问类变量, (1, 1)
        self.p2c2 = -2
        print(P2Class.p2c2, self.p2c2)  # 实例声明同名变量, 自动降级为实例变量; 但仍可通过类名去访问原类变量, (2, -2)


p2o1 = P2Class()

# 3. 类函数-静态函数-实例函数; 无同名, 类名、self都能访问外部; 同名覆盖, 外部彻底没了, 只能self访问内
# 记住这一点, 实例变量只会降级, 实例函数直接覆盖
class P3Class:
    @classmethod
    def p3cm1(cls):
        print("类函数1")
    @classmethod
    def p3cm2(cls):
        print("类函数2")
    @staticmethod
    def p3sm1():
        print("静态函数1")  # 静态函数较之类函数, 不会自动传入类参数, 无法访问类, 其实就是写在类里的最一般函数
    @staticmethod
    def p3sm2():
        print("静态函数2")

    def p3cm2(self):
        print("实例函数-覆盖类函数2")

    def p3sm2(self):
        print("实例函数-覆盖静态函数2")

    def f(self):
        P3Class.p3cm1()
        self.p3cm1()  # 同类变量, 类内部可通过类名, self去访问类函数
        # P3Class.p3cm2()  # 类函数的覆盖是彻底覆盖, 原类函数将不可再用
        self.p3cm2()
        # P3Class.p3sm2()  # 静态函数行为同类函数
        self.p3sm2()

p3o1 = P3Class()
p3o1.f()

# 4. 父类-子类之类变量; 无同名, 父类名、super()、子类名都能访问; 同名覆盖, 外部仍存在,
# 父类名、super()访问外, 子类名访问内; 注意这里的super(), 只有定义类的时候P4Child(P4Parent)
# 才能直接用super()访问, 否则得用父类名访问
class P4Parent:
    p4p1 = 1
    p4p2 = 2
    p4p3 = 3

class P4Child(P4Parent):
    p4p2 = -2
    def pf(self):
        print(P4Parent.p4p1, super().p4p1, P4Child.p4p1)  # 1, 1, 1, super()指代父class, self指代本instance, 一个是类一个是实例
        print(P4Parent.p4p2, super().p4p2, P4Child.p4p2)  # 2, 2, -2

p4o1 = P4Child()
p4o1.pf()

# 5. 父类-子类之实例变量, 这个比较简单, self指向同一个对象, 所以从头到尾都是一套变量
# 即子类里的self.p5v1访问到的直接是父类里的self.p5v1
class P5Parent:
    def __init__(self):
        self.p5v1 = 1
        self.p5v2 = 2
    def pf(self):
        print(self.p5v1, self.p5v2)

class P5Child(P5Parent):
    def __init__(self):
        super().__init__()
        self.p5v1 = -1
        self.p5v3 = -3
    def pf(self):
        print(self.p5v1, self.p5v2, self.p5v3)  # -1 2 -3

p5o1 = P5Child()
p5o1.pf()

# 6. 父类-子类之类/静态函数, 无同名, 父类名、super()、子类名都能访问外部; 同名覆盖, 外部仍存在, 父类名, super()访问外子类名访问内
class P6Parent:
    @classmethod
    def cm1p(cls):
        print("父类函数1")

    @classmethod
    def cm2p(cls):
        print("父类函数2")
    @staticmethod
    def sm1p():
        print("父静态函数1")
    @staticmethod
    def sm2p():
        print("父静态函数2")
class P6Child(P6Parent):
    @classmethod
    def cm2p(cls):
        print("子同名类函数2")
    @staticmethod
    def sm2p():
        print("子同名静态函数2")
    def f(self):
        P6Child.cm1p()
        P6Parent.cm1p()
        super().cm1p()  # 无同名, 这仨都能访问到外部类/静态函数
        P6Child.cm2p()  # 子
        P6Parent.cm2p()  # 父
        super().cm2p()  # 父

p6o1 = P6Child()
p6o1.f()

# 7. 父类-子类之实例函数, 同实例变量, self对象唯一, 从头到尾都是一套函数, 同名覆盖, 外部不存在
class P7Parent:
    def f1p(self):
        print("父实例函数1")
    def f2p(self):
        print("父实例函数2")
class P7Child(P7Parent):
    def f2p(self):
        print("子覆盖实例函数2")
    def f(self):
        self.f1p()
        self.f2p()
p7o1 = P7Child()
p7o1.f()

# 总结, 类函数-实例函数因为在一个命名空间, 会彻底覆盖, 原函数不再能访问
# 父类和子类之间的实例变量, 实例函数因为共享self, 也会彻底覆盖, 原不能再访问
