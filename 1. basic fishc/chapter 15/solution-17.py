# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Tags用法，给某些内容而不是位置做标记
    Text里修改样式，绑定事件等不能直接根据位置，需要根据这个位置的内容对象
    注意，SEL_FIRST, SEL_LAST是Mark， 而SEL是Tag
"""
"""
    先演示修改样式
"""

from tkinter import *
root = Tk()
# **************************************************************************************************************

text = Text(root, width=30, height=10)
text.pack()

text.insert(END, "I love FishC.com发达的发掘的咖啡机艾迪康缴费拉戴假发来得及法拉第街坊邻居打发")

# 先演示原生的tag，SEL
# 注意SEL的tag_config是动态的，即当tag变化后，后面的设置会自动在tag对应的新内容上生效
# 比如这里设置背景和字体颜色， 重新选中内容，样式会在新的内容上生效
# 由于SEL的后生效特性，其优先级较低，如果有其他tag设置了样式，那么SEL的样式会被覆盖
text.tag_config(SEL, background='yellow', foreground='blue')

# 还可以手动插入tag， 手动插入的tag则是一次性的， 插入后就建立的对象绑定关系
# tag_add有多个位置参数时，前两个识别为区间，其他的识别为特定位置
text.tag_add('tag1', '1.7', '1.12', '1.14')
text.tag_config('tag1', background='black')
text.insert('1.7', '新新新新新')  # 这里insert之后，后面的tag_config改的还是原1.7-1.12和1.14位置的内容
text.tag_config('tag1', background='grey')
# 如果想要样式在新插入的内容上重置，可以插入后在tag_add, tag_config一次，或者插入时直接指定tag名，表示重新绑定
text.insert('1.7', "newnewnewnewnew", ('tag1',)) # 注意，不会对原1.7-1.12和1.14位置的内容样式产生影响

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

# ********************************************************************************************************************
root.mainloop()

