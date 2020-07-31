# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第9章 异常处理
"""

"""
    你不可能总是对的
"""
# 常见的异常

# 不满足条件主动抛出的异常, assert
try:
    assert 9 > 10  # 相当于if else+raise
except AssertionError as e:
    print("AssertionError", e)

# 更通用的主动抛出异常, raise
try:
    if True: raise AssertionError("hahah")  # 也可以不带参数, 直接raise AssertionError
except AssertionError as e:
    print("AssertionError", e, str(e))  # str(e)能获取到 hahah

# 尝试访问未知的对象属性, .访问符
try:
    d = {"a": 1}
    print(d.abc)
except AttributeError as e:
    print("AttributeError", e)  # 'dict' object has no attribute 'abc'

# 尝试访问未知的索引, 序列中涉及索引
try:
    l = [1, 2, 3, 4]
    print(l[10])
except IndexError as e:
    print("IndexError", e)  # list index out of range

# 索引, 对应到字典里就是键, 对应错误KeyError(这里字典得是[]访问方式, 前面的.实际上是类/对象属性访问方式)
try:
    d = {"a":1, "b":2}
    print(d["c"])
except KeyError as e:
    print("KeyError", e)

# 尝试访问一个不存在的变量
# 这种用法应该有发挥空间, 比如有时候特定情况下才给变量赋值
# 那么就可以这么写, 不然就只能在初始先声明变量=None
try:
    print(m)
except NameError as e:
    print("NameError", e)  # 这里好像没办法直接获取"m"

# OSError, 操作系统产生的异常, FileNotFoundError就是一种OSError
try:
    open("xxx.txt", "r")
except OSError as e:
    print("OSError", e)

try:
    open("xxx.txt", "r")
except FileNotFoundError as e:
    print("FileNotFoundError", e)

# 语法错误, SyntaxError, 比较特殊, 无法捕捉

# 不同类型间的无效操作, TypeError
try:
    x = "a" + 1
except TypeError as e:
    print("TypeError", e)  # must be str, not int

# 除数不能为0异常, ZeroDivisionError
try:
    x = 3/0
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)

# 多个except不同处理方式(逐一, 同一次只可能抛出来一种Error, 且前面的except捕获完就没了)
# 注意如果在except里raise, 那么需要再外面再去捕获, 其try except体里后面的except并不能捕获其新抛出的错误
try:
    x = "a"+1
    y = 3/0
except TypeError as e:
    print("bbb1", e)
except ZeroDivisionError as e:
    print("bbb", e)
except Exception as e:
    print("bbb", e)

# 多个except统一处理
try:
    x = "a"+1
    y = 3/0
except(TypeError, ZeroDivisionError) as e:
    print(e)
    # 每次只会遇到一个Error, 所以这里的e, 实际上不是(), 要么是TypeError, 要么是ZeroDivisionError, 2选1的
    # 所以不要用e[0], e[1]这么去访问

# 捕获所有异常
try:
    x = "a"+1
except:  # 这里实际上是省了个Exception
    print("捕获所有异常")


# 个别情况下, 某些代码无论是否捕获到异常都需要执行, 而写两遍又没必要, 用finally
# 此外, 程序顺利执行, 未捕获异常, 用else
# 记住这个结构, 总感觉有很大应用的空间
try:
    print("函数主体")
except:
    print("捕获到异常才执行")
else:
    print("未捕获到异常才执行")
finally:
    print("无论什么情况下都会执行")

# 函数主体, 未捕获到异常, 无论什么情况下都会执行

try:
    print("函数主体")
    x = "a"+1
except:
    print("捕获到异常")
else:
    print("未捕获到异常")
finally:
    print("无论什么情况下都会执行")

# 函数主体, 捕获到异常, 无论什么情况下都会执行

# 想一下应用场景
s = "hello"
try:
    f = open("xxx.txt", "r")
except:
    print("打开失败")
else:
    s = f.read()  # else好像没啥意义啊, 放try里不就行了, 不也相当于没捕获到异常继续执行吗
finally:
    print(s)