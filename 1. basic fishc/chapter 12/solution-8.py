# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    生成器 generator
    1. 生成器其实就是迭代器的一种实现, 但较之__next__更简洁
    2. next每次重新调都是独立的, 需要自己去保存迭代之间的状态关系; 而生成器
    则是一种非阻塞式的状态函数, 不影响主体代码运行, 可以暂时挂起, 并保留局部变量等数据,
    下一次调用函数自动从上一次暂停的地方往下进行
    3. yield不需要一定方在类里, 可以独立为一个普通函数; 当然, 也可以协助简化__iter__(淘汰__next__)

"""

def it():
    yield 1
    yield 2
    yield 3

for x in it():
    print(x)

# 通过实现类的__iter__函数, 可以让类自己也成为可迭代对象
class C:
    def __iter__(self):
        yield 1
        yield 2
        yield 3

c = C()
print(c.__iter__)
# print(c.__next__), 没实现__next__, 这里并没有__next__, 但是仍可迭代
for x in c:
    print(x)  # 1, 2, 3

it = iter(c)
print(next(it))  # 输出1, 即即使没实现__next__, 内置函数next()也是可以生效的