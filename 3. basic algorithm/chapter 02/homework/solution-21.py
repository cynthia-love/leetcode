# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    继承深度过浅的劣势
"""

"""
    继承的优势反过来就是继承过浅的劣势
    1. 子类父类差距较大, 且继承关系不易理解(比如猫和猫科都继承动物, 那层次结构就乱了)
    2. 代码复用程度低, 子类创建工作量大(比如猫继承猫科和继承动物)
    3. 由于父类要成为很多子类的基类, 那么其抽象程度必须非常高, 能适合所有子类, 然而抽象
    高到一定程度跟没抽象一样了, 比如动物, 植物, 石头, 水等等都继承自物质
"""