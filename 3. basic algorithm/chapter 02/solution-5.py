# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    运算符重载和其它魔法方法

    比如a+b, 实际上是调用a的魔法方法 a.__add__(b)
    b的类型不要求和a一样
    此外, 如果a没有__add__, b里有__radd__, 那么会调b.__radd__(a)
"""

# 先演示运算符
class A:
    def __init__(self):
        self.a = 10

    # +, a+b
    def __add__(self, other):
        return 1+other

    # 在右边, b+a
    def __radd__(self, other):
        return other+10

    # 简写, a+=b
    def __iadd__(self, other):

        self.a += other
        return self  # 别忘了这句

    # -
    def __sub__(self, other):
        return self.a-other

    # *
    def __mul__(self, other):
        return 1*other

    # /
    def __truediv__(self, other):
        return 1/other

    # //
    def __floordiv__(self, other):
        return 100 // other

    # %
    def __mod__(self, other):
        return 100 % other

    # **
    def __pow__(self, power, modulo=None):
        return 100**power

    # <<
    def __lshift__(self, other):
        return self.a << other

    # >>
    def __rshift__(self, other):
        return self.a >> other

    # &
    def __and__(self, other):
        return self.a & 3

    # |
    def __or__(self, other):
        return self.a | 3

    # ^
    def __xor__(self, other):
        return self.a ^ 3

    # +a
    def __pos__(self):
        return +self.a

    # -a
    def __neg__(self):
        return -self.a

    # ~a, 按位取反
    def __invert__(self):
        return ~self.a

    # abs
    def __abs__(self):
        return abs(self.a)

    # 比较运算符有妙用
    # 比如个别算法不支持自定义比较函数, 可以在类里把这几个比较魔法方法定义了
    # <
    def __lt__(self, other):
        return self.a < other

    # <=
    def __le__(self, other):
        return self.a <= other

    # >
    def __gt__(self, other):
        return self.a > other

    # >=
    def __ge__(self, other):
        return self.a >= other

    # ==
    def __eq__(self, other):
        return self.a == other

    # !=
    def __ne__(self, other):
        return self.a != other

a = A()
print(a+8)
print(8+a)
a += 1
print(a-8)
print(a*8)
print(a/8)
print(a//2)
print(a % 3)
print(a**2)
print(a << 1)
print(a >> 1)
print(a & 3)
print(a | 3)
print(a ^ 3)
print(+a)
print(-a)
print(~a)
print(abs(a))
print(a < 1)
print(a <= 12)
print(a == 11)
print(a != 11)

# 再演示非运算符
print("=======================")
class B:
    def __init__(self):
        self.x = 1
        self.s = "hello"
        self.d = {
            "k1": 1,
            "k2": 2
        }

    # v in b
    def __contains__(self, item):
        return item in self.s

    # b[k], 像字典那样访问元素
    def __getitem__(self, item):
        return self.d[item]

    # b[k] = v
    def __setitem__(self, key, value):
        self.d[key] = value

    # del b[k]
    def __delitem__(self, key):
        del self.d[key]

    # b(), 注意是实例b, 而非类B(), 后者是实例化
    # __call__和__new__, __init__完全不是一码事
    # __new__是创建对象用的, 返回值是创建后的实例
    # __init__拿到__new__创建的实例, 然后初始化对象属性什么的, 返回None

    def __call__(self, *args, **kwargs):
        print(args, kwargs)

    # len(b)
    def __len__(self):
        return 100

    # hash(b)
    # 哈希, 包括MD5, SHA等, 可以把任意长度的输入通过算列算法变换成固定长度的输出, 即压缩映射
    # 同一输入同一算法输出相同; 不同输入可能会散列成相同的输出, 虽然几率很小
    # 一般用来得到文件的摘要, 可逆
    # 区别于base64, base64主要是用于方便网络传输的, 可解码
    # base64将二进制转化成字符串, 且不会像hash那样固定长度
    def __hash__(self):
        return 10000

    # iter
    def __iter__(self):
        return iter([1, 2, 3])

    # bool, 这个也很重要, 可以直接支持if b这种语法
    def __bool__(self):
        return True

    # float
    def __float__(self):
        return float(self.x)

    # int
    def __int__(self):
        return self.x

    # repr
    def __repr__(self):
        return self.s

    # str
    def __str__(self):
        return self.s

    # reversed
    def __reversed__(self):
        return [4, 3, 2, 1]
b = B()
print("o" in b)
print(b['k1'])
b['k3'] = 4
print(b['k3'])
del b['k1']
print(b.d)
print(callable(b))
b(3, 4, x=8, y=10)  # (3, 4) {'x': 8, 'y': 10}
print(len(b))
print(hash(b))
print(iter(b))
print(bool(b))
print(float(b))
print(repr(b))
print(str(b))
print(reversed(b))

"""
    补充, 有时候即使没定义魔法方法也可能支持一些操作符, 可能是python提供了默认定义, 或者来源于其他定义
    1. bool, 默认情况下除了None对象外的都为True, 定义了__len__的容器类型除外, 长度为0返回False否则True
    2. iter, 如果定义了__len__和__getitem__, 则默认支持iter; 支持了iter, 则默认支持__contains__
    除了通过__len__和__getitem__实现iter, 还可以通过__next__和__iter__实现iter, 或者直接用__iter__
    3. 如果没有实现__eq__, 则===等价于is, 即是同一个对象的不同别名才认为相等
    4. 还要注意, 定义了==, 无法直接得到!=, 定义了>无法直接得到>=; 但是定义了>, 却能支持<
    
"""