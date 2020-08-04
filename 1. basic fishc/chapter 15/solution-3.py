# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Label组件详解
    可文字, gif图片, 或两者结合
"""

from tkinter import *

class App:

    def __init__(self, parent):

        # txt = "您所下载的影片含有未成年人限制内容, 请满18岁后再点击观看!"
        # label1 = Label(parent, text=txt)
        # label1.pack(side=LEFT)

        """
        首先, Label组件只支持.gif格式的图片
        其次, 这里的img不能是临时变量, 比如把self.img改成img图片就渲染不出来了, 很奇怪
        而且把PhotoImage写到label2里也不行...奇了怪了, 好像只能像下面这么写
        而上面的text可以看到, txt前并没加self也能正常显示...
        """
        # self.img = PhotoImage(file='img/demo.gif')
        # label2 = Label(parent, image=self.img)
        # label2.pack(side=RIGHT)

        """
        text和image可以混合到一起
        """
        self.img3 = PhotoImage(file='img/cute.gif')
        # justify换行后左对齐, padx文字右移一点, fg文本颜色, compound混合模式, 不指定文字出不来
        label3 = Label(parent, text="带换行的图片文字混合演示\n这里是第二行", bg='yellow', font=("楷体", 12),
                       justify=LEFT, padx=10, image=self.img3, compound=CENTER)  # CENTER表示混到图片中间
        label3.pack(side=TOP, expand=YES, anchor=E, padx=100, fill=X)

root = Tk()
root.geometry("500x500+100+100")
app = App(root)

root.mainloop()

"""
    pack布局详解
    1. side有四个取值, top, left, bottom, right
    2. 以side=top为例, 父组件400x400, 子组件20x20
    那么: 
    (1) 容器可用空间, 前辈还没占用的空间
    (2) 子组件原始空间, 即20x20
    (3) 组件独占空间, 这里side=top, 那么独占空间为上方400x20
    即side=top/bottom时, 组件占据整行, 后辈组件只能依次排在它的下面/上面
    side=left/right时, 组件占据整列, 后辈组件只能依次排在它的右面/左面
    (4) 组件可扩展空间, 即容器里的剩余空间
    side=top/bottom时, 组件独占整行, 并可纵向向下/上扩展
    side=left/right时, 独占整列, 并可横向向右/向左扩展
    expand=yes才会启用这部分空间, 默认不启用
    3. anchor共9个方向, 默认center, 结合padx, pady, 可将组件安排在指定位置
    只指定anchor时, padx和pady认为是0; 注意是先anchor, 再根据pad偏移
    比如anchor=E, padx=100, 是先放到最右边, 再往左移动100
    (1) expand为no时, anchor只能让子组件在组件独占空间里移动
    即N, S, CENTER美有效果, 只有S和W能让组件在左还是在右
    (2) expand为yes时, 组件占据全部空间, anchor9个位置都有效
    
    4. fill, 其实和前面的不是一回事, 前面的控制子组件占据的总空间
    fill控制子组件原始空间是否扩展至占据总空间, 有四个值, none, BOTH, X, Y
    注意, fill影响的是2.(2), 但也只是影响空间, 并不会整个组件拉伸(这里存疑, 比如Listbox就是拉伸的)
    设想几种情况:
    (1) side=TOP, fill=Y, 因为expand为NO, 占据总空间只有2.(3)独占空间
    而默认就是占一整行的, 所以这里fill=Y没有效果
    (2) side=TOP, fill=X, expand为NO, 这里会将子组件原始空间扩展至整行独占空间
    (3) side=TOP, expand=YES, anchor=E, padx=100, fill=X
    side=TOP+expand=YES, 会占据整个空间, 如果没有其他后辈组件, 这里的side是TOP
    还是LEFT, RIGHT, BOTTOM, 只要有expand=YES, 结果是一样的
    这里占用整个空间后, 靠右边中间位置, 注意padx不计算占用空间, 所有这里的
    fill=X 不会填充一整行, 不光右边会留100 padx, 左边也会留100 padx
    
    5. 如果有后辈组件, 原则如下:
    (1) 后辈组件不会进入前辈组件的2.(3)独占空间, 无论side怎么设置
    (2) 可扩展空间2.(4)是可以被后辈组件的独占空间压缩的
    (3) 但是后辈组件的可扩展空间不会侵占前辈的可扩展空间, 和(2)对比理解下
    若扩展空间有重叠, 前辈享用扩展空间
    (4) 空间优先级别: 界面空间>前辈独占空间>后辈独占空间>前辈扩展空间>后辈扩展空间
"""