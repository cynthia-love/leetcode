# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    单元测试模块unittest
"""
"""
    学习unittest模块, 单元测试(不要再pycharm里直接运行, 右键open in terminal后命令行执行)
    TestCase, 测试用例
    TestSuite, 测试集合
    TestLoader, 加载测试用例(一般用不到)
    TextTestRunner, HTMLTestRunner(要单独下, html-testRunner)等, 执行用例

    HTMLTestRunner需要单独安装, 且由于其配置文件里的jquery路径有问题(谷歌的访问不了)会导致
    结果报告中view详情按钮点不了, 需要将其(查找src)替换成
    http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js
"""

"""
    一个class继承unittest.TestCase, 就是一个测试用例, 里面每有一个test打头的方法,
    在load的时候就会生成一个TestCase
"""

def add(a, b):
    return a+b

def minus(a, b):
    return a-b

import unittest

class TestCase(unittest.TestCase):
    """test case"""
    # 更准确地说, 这里不是一个测试用例, 而是一堆, 每有一个test_xxx方法就代表一个测试用例
    # 父类里构造函数需要传入方法名, TestCase("test_minus"), 即每个方法创建一个实例

    @classmethod
    def setUpClass(cls) -> None:
        print("只执行一次, 用于初始化环境, 对应的方法setUp(self), 每个测试案例前执行一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("只执行一次, 用于清理环境, 对应的方法tearDown(self), 每个测试案例后执行一次")

    def test_add(self):
        """这里最好加上注释, 便于后续定位用例"""
        # 这里3, 1, 2什么的直接写死了, 实际环境下应该外面传, 传不同的值得到不同的测试案例
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """由于成功失败是以用例为单位的, 不建议一个用例里面加太多assert"""
        self.assertEqual(1, minus(3, 1))

if __name__ == '__main__':

    # unittest.main(verbosity=2)  # 设置verbosity说是可以修改打印信息的详细程度
    # 简单的测试直接unittest.main()就行了, 但有时候需要控制测试用例的顺序或者有很多测试用例系列
    suite = unittest.TestSuite()
    test1 = TestCase("test_add")
    test2 = TestCase("test_minus")
    test3 = TestCase("test_add")  # 实际运用时, 会外传参数, 不会有重复用例

    suite.addTest(test1)
    suite.addTest(test2)
    suite.addTest(test3)

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # 除了命令行打印, 还可以输出到文件
    """
    with open("data/unittest.txt", "w") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
    """
    from HtmlTestRunner import HTMLTestRunner

    runner = HTMLTestRunner(verbosity=2)
    runner.run(suite)

    # HTMLTestRunner也可以配置stream, 其行为同默认TestRunner
    # 不过不配置也不影响.html格式的报告生成
