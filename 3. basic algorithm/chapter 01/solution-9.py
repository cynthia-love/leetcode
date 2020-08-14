# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    更清晰直接的新语法
"""

"""条件表达式"""
f = lambda x: x if x >= 0 else -x  # xx if condition else yy, 比用if...else代码块更简洁
print(f(-1))

"""解析语法"""  # [xx for value in iterable if condition], map+filter的结合体
l = [-1, -2, 3, 8, 11]
print([x*x for x in l if x > 0])
print([x*x if x > 10 else x for x in l if x > 0])
# 注意这句话前面的是条件表达式, 作用是条件map; 后面的是条件筛选, 作用是filter
f1 = lambda n: [x**2 for x in range(1, n+1)]  # 1~n的平方列表
print(f1(8))  # [1, 4, 9, 16, 25, 36, 49, 64]
f2 = lambda n: [x for x in range(1, n+1) if n % x == 0]  # 因子列表
print(f2(16))
f3 = lambda n: {x for x in range(1, n+1) if n % x == 0}  # 集合解析
print(f3(16))
f4 = lambda n: {x: x for x in range(1, n+1) if n % x == 0}  # 字典解析
print(f4(16))
f5 = lambda n: (x for x in range(1, n+1) if n % x == 0)  # 生成器generator解析
print(f5(16))

# 生成器解析有时候有妙用, 这里的数是一个一个给sum函数的, 而不是先生成一个完整的list给sum去算
# 这种懒惰计算可以很大程度上节省内存占用; 注意不光generator是懒惰计算, 所有的iterator都是懒惰计算
# for循环只是在不是迭代器的时候自动转成迭代器, 而且生成器本身就是迭代器, 所以这里并不会破坏
# range(1, n+1)本身的懒惰计算
f6 = lambda n: sum(x*x for x in range(1, n+1))
print(f6(16))

"""序列类型的打包和解包"""  # 这里指的并不是*, **, 那属于手动解包
x = 1, 2, 3  # 这里虽然没有(), 但右边会被识别为(1, 2, 3), 称为元组的自动打包, 也常用于return 1, 2这种场景
def f():
    return 11, 88

a, b, c = range(3)  # 将序列类型自动解包, 赋给左边的多个变量, 也常用于for k, v in d.items():
d = {"a": 1, "b": 2, "c": 8}
for k, v in d.items():  # d.items()格式为[("a", 1), ("b", 2), ("c", 8)]
    print(k, v)

a, b = 1, 2  # 自动打包和自动解包结合, 右边先打包(1, 2), 再解包分别赋给a, b
a, b = b + 8, a + 12  # 注意, 右边先整个打包, 所以这里是(10, 13), 利用这种机制交换值就不用中间变量了
print(a, b)



