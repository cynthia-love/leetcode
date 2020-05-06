# -*- coding: utf-8 -*-

# Author: Cynthia

"""
     Numpy库基础知识
"""
"""
    NumPy, n维数组和矩阵容器, 比Python自身的嵌套列表高效, 辅以部分基础的数学计算, 比如傅里叶变换
    SciPy, 基于Numpy的科学计算包, 封装了一些高阶抽象和物理模型, 比如信号处理等
    Pandas, 基于Numpy的数据处理包, 提供了大量能使我们快速便捷地处理数据的函数和方法
    Matplotlib, Python中最著名的绘图系统
    Sklearn, 建立在上述四个之上的机器学习工具包, 聚类分类回归等等
"""
import numpy as np


def main():

    # *****************************************************************************
    # n维数组对象 ndarray, 只能存储同类型元素的多维数组
    # np.array(object, dtype = None, copy = True, order = None)
    l1, l2 = [1, 2, 3, 4], [[1, 2], [3, 4]]
    a1, a2 = np.array(l1, dtype=float), np.array(l2, dtype=int)
    print(l1)
    print(a1)
    print(l2)
    print(a2)
    # 注意, 虽然ndarray只支持单一数据类型, 但是可以自定义复杂数据类型
    dt = np.array([('lucy', [13, 15]), ('jim', [14, 18]), ('lucas', [18, 20])],
                  dtype=[('name', str, 16), ('info', int, (2,))])
    print(dt.dtype)
    print(dt, dt[0]['name'], dt[0]['info'])

    # *****************************************************************************
    # ndarray的属性
    l3 = [[5, 6], [7, 8], [9, 10]]
    a3 = np.array(l3)
    print(l3[1][1], a3[1][1], a3[1, 1])  # ndarray多维索引支持[][]和[m, n]两种写法
    print(a3.ndim)  # 维度为2
    print(a3.shape)  # (2, 2)
    print(a3.size)  # 元素的总个数
    """
    每个维度称为一个轴, numpy里大量的操作需要指定轴axis=0, 1, 2...
    axis=0表示在第0维上变化, axis=1表示在第1维上变化(可以理解为固定其他索引, 变化某一维度索引)
    """
    print(np.mean(a3, axis=0))  # [6 7]
    print(np.mean(a3, axis=1))  # [5.5 7.5]

    a4 = np.reshape(a3, newshape=(2, 3), order='C')  # 按行顺序置为1维再重构
    a5 = np.reshape(a3, newshape=(2, 3), order='F')  # 按列顺序置为1维再重构
    print(a3)
    print(a4)
    print(a5)

    # *****************************************************************************
    # 创建数组
    a6 = np.empty((3, 3), dtype=float)
    print(a6)  # 会打印随机值
    a7 = np.zeros((3, 3), dtype=np.float)
    print(a7)
    a8 = np.ones((3, 3))
    print(a8)
    # numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象
    # numpy.frombuffer(buffer, dtype=float, count=-1, offset=0), -1表示读入所有数据
    l9 = b'HelloWorld'
    a9 = np.frombuffer(l9, dtype='S1', count=-1, offset=0)  # dtype设置为S2试试
    print(a9)
    l10 = iter([3, 8, 11, 2])
    a10 = np.fromiter(l10, dtype=float)
    print(a10)
    # 知道起始和终止以及步长
    a11 = np.arange(2, 20, 2, dtype=float)
    print(a11)
    # 知道起始和终止以及份数, 等差
    a12 = np.linspace(2, 20, 30, endpoint=True)
    print(a12)
    # 知道起始和终止以及份数, 等比
    a13 = np.logspace(2, 20, 10, endpoint=False)
    print(a13)

    # *****************************************************************************
    # 切片和索引
    l14 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a14 = np.array(l14)
    print(l14[1:5:2])
    print(a14[1:5:2])
    print(l14[1:])
    print(a14[1:])
    l15 = [[1, 2], [3, 4], [5, 6]]
    a15 = np.array(l15)
    # 二维数组的切片, 只有ndarray支持, python自带list支持不了
    print(a15[:, 1])
    print(a15[:, 0:])
    print(a15[:, [0]])
    # 数组索引, 有几个维度就有几个数组, 每个数组对应位置拼成一个索引
    print(a15[(0, 0, 2, 2), (0, 1, 0, 1)])
    # 注意和下面这个做比较, 括起来就变成二维了
    print(a15[([0, 0], [2, 2]), ([0, 1], [0, 1])])
    # 注意, 数组索引, 如果给的是一个数组而不是多个, 就不用拼了
    print(a15[[-1, -2]])
    # 条件索引
    print([x for y in a15 for x in y if x >= 3])  # 这什么神仙写法
    print(a15[a15 >= 3])  # 注意这里直接比的数组, 而不是元素

    # *****************************************************************************
    # 广播
    # 如果两个数组 a 和 b 形状相同, 则加减乘除是对应元素计算; 否则, 会触发广播机制
    a16 = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    a17 = np.array([
        [1, 1, 1],
        [1, 1, 1]
    ])
    a18 = np.array([2, 2, 2])
    a19 = np.array([3, 3]).reshape((2, 1))
    print(a16+a17)
    print(a16+a18)  # 第一维广播
    print(a16+a19)  # 第二维广播

    # *****************************************************************************
    # 迭代数组

if __name__ == '__main__':
    main()
