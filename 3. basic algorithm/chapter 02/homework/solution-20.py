# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    继承深度过深的劣势
"""

"""
    1. 理解困难, A<-B<-C<-D....O, 那么O到底具有怎样的行为模式, 得一级一级往上找
    2. 修改困难, 类与类之间高耦合, 越往上层级的类, 修改起来越困难
    3. 运行效率低, 初始化时要一层一层往上调__init__, 调用成员函数时, 因为是存在
    类的__dict__里的, 所以也得一层一层往上找
    
"""