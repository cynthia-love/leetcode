# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    画类图

    基类object
    1. Goat扩展object, 增加实例变量_tail和方法milk(), jump()
    2. Pig类扩展object, 增加实例变量_nose和方法eat(food)和wallow()
    3. Horse类扩展object, 增加实例变量_height和_color以及方法run()和jump()
    4. Racer类扩展了Horse类, 增加了方法race()
    5. Equestrain类扩展了Horse类, 增加了实例变量_weight以及方法trot()与is_trained()

"""

"""
    最常用关系线段: 1参数里依赖, 带箭头虚线, 2构造函数里依赖, 带箭头实线, 3继承, 空心三角箭头实线
    见 data/UML-Class.jpeg 
"""