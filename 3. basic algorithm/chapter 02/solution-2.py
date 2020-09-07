# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    软件开发的三个阶段: 设计->实现->测试和调试
"""

"""
    对于面向对象编程, 设计是软件开发过程中最重要的阶段, 在这一阶段要确定怎么把程序的工作拆分成
    各个部分(类), 每个类要存储哪些数据, 支持哪些方法, 以及不同的类之间怎么交互
    一些小技巧: 把工作按角色分开, 比如描述授课, 那就存在老师角色, 学生角色, 这些角色形成类, 每种
    角色的特性形成类种的属性, 职责(做什么)形成类中的方法; 角色的划分要足够独立, 不能有穿插, 比如
    一个人不能既是老师, 又是学生
"""

"""
    一般采用UML图来表达程序的组织, 比如最常用的类图
    
               CreditCard
    
            _bank: str
            _account: str
            _balance: int
    
            getAccount(): str
            getBalance(): int
            
    除了单个类, 类与类之间还有关系
    1. dependency, 带箭头的虚线. 比如类A的方法的参数中用到了类B, 那就说A依赖于B, A虚线箭头指向B
    2. association, 比dependency稍强一些的关系, 一般是类A属性中直接用到B, 即没有B直接A都不能new, 
    比如同学之间可能存在依赖, 而老师学生之间则是关联, UML图中表示为带箭头的实线
    3. composition, 其实也是一种关联, 只不过关系更强, 比如人包括头, 躯干, 四肢, 且这种关联关系
    需要在一开始的构造函数里就明确, uml途中表示为实心菱形箭头线(感觉用带箭头实线也行)
    4. implements, 实现接口, 虚线空心三角形箭头
    5. extends, 继承父类, 实线空心三角形箭头(python里没implements, 所以都是实线空心三角箭头)
    
    --->, 一>,   , --△, 一△
    
    最常用: 1参数里依赖, 带箭头虚线, 2构造函数里依赖, 带箭头实线, 3继承, 空心三角箭头实线
"""

"""
    命名规范
    类, XxxYyy
    常量, MAX_SIZE
    变量, list_len
    函数, getSum, 或者get_sum也行
    内部属性, _balance
"""

"""
    文档, 出现在模块, 类, 函数中的第一个字符串认为是docstring
    
    以函数doc为例, 第一行写简要介绍, 然后空一行
    中间介绍参数和返回值
"""

def f(x: int) -> str:
    """The summary of the function

    :param x: an int that serves as the age of the student

    :return: the description of the student
    """

    pass

help(f)


"""
    测试, 最好每行代码都能执行到, 再不济类的每个方法都能执行一次
    两种测试, top-down和bottom-up
    如果组件A依赖于组件B, 那么认为A高于B
    1. 自上而下, 需要用到桩函数(stub)代替底层组件(挡板?)
    2. 自下而上, 通常称为单元测试, 即先测那些不依赖于其他类的类
    
    测试有几种方式, 如果是模块测试, 可以直接在里面写
    if __name__ == '__main__':
        xxxxx
    
    要么可以用unittest模块
"""