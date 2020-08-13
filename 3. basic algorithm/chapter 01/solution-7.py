# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    异常处理
    如果异常没有在函数体内被捕获, 那么函数的执行会立刻停止, 并且这个异常可能会被传播到调用的上下文
"""
import pickle
import collections

"""常见异常类"""
# Exception, 所有异常类的基类
try:
    x = 1/0
except Exception as e:
    print(e)

# AttributeError, .操作符找不到成员
try:
    x = 1
    print(x.a)
except AttributeError as e:
    print(e)

# KeyError, []操作符找不到键值
try:
    x = {}
    print(x["a"])
except KeyError as e:
    print(e)

# EOFError, "end of file"到达控制台或者文件输入引发错误
try:
    f = open("data/empty.txt", "rb")
    x = pickle.load(f)
except EOFError as e:
    print("end of file")

# IOError, 输入/输出操作失败引发错误
try:
    f = open("data/xxx.txt", "r")
except IOError as e:
    print(e)

# IndexError, 与KeyError对应的一个错误, 索引为数字
try:
    print([1, 2, 3][8])
except IndexError as e:
    print(e)

# KeyboardInterrrupt, ctrl-c 中断程序时引发错误

# NameError, 使用不存在的标识符, 有点像js里的undefined
try:
    print(m)
except NameError as e:
    print(e)

# StopIteration, 下一次遍历的元素不存在时引发错误
try:
    l = iter([1, 2, 3])
    while True:
        print(next(l))
except StopIteration as e:
    print("stopiteration")

# TypeError, 发给函数的参数类型不对
try:
    abs("hello")
except TypeError as e:
    print("TypeError")

# ValueError, 函数参数类型对, 但值不对
try:
    int("2.1")
except ValueError as e:
    print("ValueError")

# ZeroDivisionError
try:
    x = 1/0
except ZeroDivisionError as e:
    print("ZeroDivisionError")

"""手动抛出异常"""
# 以sqrt为例
def f_sqrt(x):
    # 注意, 错误检测也是占用性能的, 不是越多越好
    # 比如这里, 不显式raise错误, 在计算x**0.5的时候一样会抛错
    if not isinstance(x, (int, float)):  # isinstance第二个参数可以是多个; 参数2给定基类也会返回True
        raise TypeError("aa")
    elif x < 0:
        raise ValueError
        # raise的时候可以直接ValueError, 也可以ValueError(message)
        # 加的message后面捕获的时候, 可以用str(e)打印出来
    else:
        return x**0.5

try:
    f_sqrt("1")
except TypeError as e:
    print("TypeError", e)

try:
    f_sqrt(-1)
except ValueError as e:
    print("ValueError", e)

# 再举个sum的例子, 两个版本, 第一个严格错误检测, 第二个简单版本
def f_sum(values):
    if not isinstance(values, collections.Iterable):
        # Iterable包含所有迭代容器类型,list, tuple, set等
        raise TypeError("not an iterable type")
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise ValueError("elements must be numeric")
        total += v
    return total

# 简单版本, 不显式校验错误, 但适当的异常也会由代码自然抛出, 我们更倾向于这种简单实现
def f_sum2(values):
    total = 0
    for v in values:
        total += v
    return total

"""异常捕捉"""
# 异常处理其实有两种思路, 一种是事前许可控制, 一种是事后请求原谅
x, y = 1, 0
if y != 0:
    print(x/y)
else:
    print("zero division")

# 这种属于事前许可控制, 即先判断y是否符合条件, 符合了再去除以

x, y = 1, 0
try:
    print(x/y)
except ZeroDivisionError:
    print('zero division')
# 这种属于事后请求原谅
# try except的好处是, 非特殊情况下高效运行, 不用每次都去执行额外检查语句
# 如果我们判断出现问题的几率较小, 或者无法进行事前校验, 此时用try except事后补救
# 比如打开文件, 无法事前校验, 可以用try except

# 异常捕获的一般格式
try:
    x = int(input("请输入一个整数"))
except (TypeError, ValueError) as e:
    # except后面的Error可以指定多个, 但实际上每次只会捕获一个
    print("输入非法")
except EOFError as e:
    print("EOF Error")
except:  # 最后可以跟一个except不指定错误类型, 用于捡漏, 但一般不建议这么干
    # 因为未知类型, 并不知道该如何处理它, 这里轻易给捕获了, 可能就无法触发程序中断什么的了
    print("其它未知错误")
finally:
    print("无论如何都要经过这里")
