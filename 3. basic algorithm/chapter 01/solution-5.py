# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    函数
    类外面的函数叫函数, 类里面的函数叫方法
"""

"""
    每次调用函数, python会创建一个专用的活动记录来存储于当前调用相关的信息
    这个活动记录包括命名空间, 命名空间包括该函数的参数和在函数体内定义的其他本地标识符
"""

"""参数与返回值"""
def f(l, target):  # 标识符f为函数的名称, l和target为形参, 调用时传的[1, 2, 3]和3为实参
    """
    :param l:
    :param target:
    :return:
    """
    n = 0
    for each in l:
        if each == target:
            n += 1
    print(locals())  # {'l': [1, 2, 3], 'target': 3, 'n': 1, 'each': 3}
    return n
    # 如果没有return语句, 则自动返回None
    # 返回值也类似于赋值, r = n

r = f([1, 2, 3], 3)  # # 参数传递遵循标准赋值语句语法, 比如这里相当于l=[1, 2, 3], target=3
# 注意python里都是引用传参, 是直接给实参取别名, 而不是复制一个新的对象
print(r)
help(f)

def f2(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1  # 根据条件逻辑的不同, 可以有多个return语句

print(f2([8, 6, 1], 6))

def f3(l):
    # l = [8, 9], 注意如果这么写, l降级为局部变量, 后面再append改变的是局部变量而不是外部的实参
    l.append(8)

x = [1, 2, 3]
f3(x)  # 前面说了python是引用传参, 对可变对象的修改会直接反映到原对象上
print(x)

"""参数默认值"""
# 注意如果一个参数有默认值, 那么它后面的参数也得有默认值, 不用特别记, 不这么写会报错的
def f4(var1=None, var2=None):
    if var1:
        return 'a'
    if var2:
        return 'b'
    return 'c'

print(f4(), f4(1), f4(var2=2))

# 可以通过参数默认值实现多态效果, 以range函数为例, 支持range(n), range(m, n), range(m, n, step)
def f5(start, end=None, step=1):
    if not end: return range(0, start)
    else: return range(start, end, step)
print(f5(8), f5(3, 8), f5(3, 8, 2))

"""关键字参数"""
def f6(a, b, c):
    print(a, b, c)
f6(c='c', a='a', b='b')
# 传统的实参赋值形参是根据位置的, 除了位置, 还可以显示地按照形参的名称赋值
# 典型的应用场景比如max(a, b, c...key)函数
def f7(*args, key=None):  # 这种情况下前面参数个数不定, 所以key只能用关键字形式赋值
    if not key: return max(args)
    else: return max(args, key=key)

print(f7(1, 2, 3, 8, 100))
print(f7(1, 38, 9, -1, -2, -900, key=abs))

"""常用内置函数"""
# 输入输出, print, input, open
# 字符编码
print(ord('a'))  # ASCII编码97
print(chr(97))  # 'a'
# 数学运算, divmod是//和%的结合体, pow表示次方, round四舍五入, 可以指定第二个参数表示保留几位小数
print(abs(-1), divmod(10, 3), pow(2, 3), round(3.1), sum([1, 2, 3]), round(3.132, 2))  # 3.13
# 排序
print(max(1, 2,3), max([1,2,3]), min(1, 2), sorted([8, 1, 2], key=lambda x: x, reverse=True))
# 集合/迭代
# reversed返回iterator, 需要强转list
# all, 如果所有元素都是True, 则返回True, 否则返回False
# any, 有一个元素为True, 则返回True, 感觉这俩函数应该有妙用
print(range(10), len([1,2,3]), list(reversed([1, 8, 2])), all([True, 8, []]), any([8, 0]))
print(list(map(lambda x: x+1, [1, 2, 3])))  # map的结果也得强制转换
print(list(map(lambda x, y:x+y, [1, 2, 3], [8, 10])))  # [9, 12], map支持多个list映射, 按最短截断
it = iter([8, 7, 100])
print(next(it), next(it))
# 其它
print(hash("adb"))  # 返回对象的整数散列值, 注意每次会变; md5是hash的一种
print(id("aaa"))  # 返回对象的身份标识整数
print(isinstance("aaa", str))
print(type("aaa"))
