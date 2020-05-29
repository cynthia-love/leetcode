# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Tags用法
    一般用于修改文本的样式，以及将Text中的内容与键盘、鼠标等绑定事件
    据观察，没有直接的可指定元素索引位置的设置样式函数
"""

from tkinter import *

root = Tk()

text = Text(root, width=30, height=10)

text.pack()

text.insert(END, "I love FishC.com发达的发掘的咖啡机艾迪康缴费拉戴假发来得及法拉第街坊邻居打发")

# 注意SEL的tag_config是动态的，即当tag变化后，后面的设置会自动在tag对应的新内容上生效
# 比如这里设置背景和字体颜色， 重新选中内容，样式会在新的内容上生效
text.tag_config(SEL, background='yellow', foreground='blue')

# 还可以手动插入tag， 手动插入的tag则是一次性的， 把这几个位置对应内容删了， 新的内容背景不会变黑
# tag_add有多个位置参数时，前两个识别为区间，其他的识别为特定位置
text.tag_add('tag1', '1.7', '1.12', '1.14')
text.tag_config('tag1', background='black')
text.tag_config('tag1', background='grey')
# 此外， tag后覆盖前，这里生效的背景是grey
# 但注意，选中后不糊变成黄， 点了按钮也不会变红， SEL的行为比较特殊， 设置在前， 选中在后， 选中这一行为不会覆盖其他设置
# SEL只在自己内部遵守后覆盖前规则


# 其他可设置的东西
# font控制字体
text.tag_config(SEL, font="微软雅黑")
# borderwidth和relief共同作用控制边框宽度和样式
text.tag_config(SEL, borderwidth=1, relief=SUNKEN)
# justify指定对其方式， tag覆盖的范围里必须有行首字符
text.tag_config(SEL, justify=RIGHT)

# 首行缩进， 其他行缩进， tag要指向整个文本框
text.tag_config(SEL, lmargin1=20, lmargin2=10)

# 相对于基线的偏移量， 基线指每行的下方的线
text.tag_config(SEL, offset=10)

# 画一条删除线
text.tag_config(SEL, overstrike=True)

# 右侧缩进
text.tag_config(SEL, rmargin=100)

# 行上方间距（段前）， 自动换行行间间距， 行下方间距（段后）
text.tag_config(SEL, spacing1=10, spacing2=20, spacing3=30)

# TAB键对应几个字符
text.tag_config(SEL, tabs='5c')

# 加下划线
text.tag_config(SEL, underline=True)

# 是否自动换行， NONE, CHAR, WORD
text.tag_config(SEL, wrap=NONE)

def f():
    print(text.get(SEL_FIRST, SEL_LAST))
    text.tag_config(SEL, background='red', foreground='blue')
    # insert可以有第三个参数， tag， 表示直接把tag配置拿过来用到插入的内容上， 和原tag的位置信息无半毛钱关系
    # 这里可以指定多个tag， 用text.tag_lower("tag1")和tag_raise去设定优先级
    text.insert(INSERT, "这里是新的内容新的内容新的内容", ("tag1",))

# 注意SEL是一个tag， 对应选中的内容；SEL_FIRST, SEL_LAST是俩索引，对应位置
button = Button(root, text="点我", command=f)
button.pack()



root.mainloop()

