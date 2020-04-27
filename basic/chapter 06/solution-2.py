# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    灵活即强大
"""

# 注释, 即help命令打印的东西
def f1(name):
    """
    打印名字
    f1(name: str)
    """
    # 这个位置的注释称为函数文档字符串
    print(name)
f1("Haha")
help(f1)

# 形参实参
def f(name, age=16): # 这里的age称为默认参数, 调用函数时如果不传参则使用默认值
    print(name, age)
f("Jim")  # 这里name称为形参, 只代表一个位置, 变量名, 而Jim是实参,是一个具体的值
f(name="Jim")  # 传实参时可以指定变量名, 参数多的时候这么传参可以避免位置错乱

# 收集参数, 函数调用时不确定会传入多少个参数时用这个
def f2(*params):
    print(params)
f2(1, 2, 4, "hahah")
# 其实也可以这么写
def f3(params):
    print(params)
f3((1, 2, 4, "hahah"))  # 本来,是tuple的标志, 但是函数传参比较特殊, 不会直接解析成一个元组
# 前面加*就是告诉函数, 把传入的参数整个打包成一个元组赋给params
# 还有一种特殊情况, 收集参数后面还有其他参数
def f4(*params, extra=8):
    print(params)
    print(extra)
f4(1, 2, 3, [8, 8], extra=100)  # 此时给额外参数传参时就得指定变量名了
# *不仅可以打包, 还可以在传参时解包list
def f5(a, b, c):
    print(a, b, c)
f5(*[1, 2, 3])

# 收集参数除了*, 还可以用**, 表示打包成字典形式
def f6(**params):
    print(params)
f6(a=1, b=2, c=3)  # 打包成字典模式, 传参的时候就得指定变量名了
def f7(a, b, c):
    print(a, b, c)
f7(**{"b": 1, "a": 2, "c": 3})  # 同样, **也可以在传参时解包dict

