# -*- coding: utf-8 -*-

# Author: Cynthia

"""
     正则表达式入门

     注意字符串自带的find什么的是不支持正则匹配的
"""

import re

s = "helloworld"

# 通配符
res = re.search(r".el.", s)
print(res.span(), res.group(), res.group(0))  # (0, 4) hell hell, group()和group(0)返回的都是整个匹配

# 演示一下group用法
res = re.search(r"((el).*or(.*l))", s)
print(res.group(0), res.groups(), res.group(1), res.group(2))
# elloworl ('elloworl', 'el', 'l') elloworl el
# group(0)为整个匹配, groups()为1, 2, 3...的, group(1)为第一个()匹配, group(2)为第二个; 嵌套的按(位置从左往右算
print(res.span(), res.span(0), res.span(1), res.span(2))
# 与group对应的是span, 同样有span(), span(0, 1, 2...); 不过没spans()函数

# \, 可以剥夺特殊字符的特殊能力, 以及赋予普通字符特殊能力
res = re.search(r"\.ha.*", "dfkajdkjfkdjfiej.hadkajdjfk")
print(res.group())  # .hadkajdjfk; 由于匹配不上返回None, 最好判断一下res再用res.group()
res = re.search(r"\S*", "adkfjdkjfkdaf adkjfdkjf adfd")
print(res.group())  # \S赋予S代表非空字符的能力, adkfjdkjfkdaf

# 字符枚举, [], 比如[abc], 表示匹配到单个字符a或b或c都行, 而不是123; 由于都是字符串, 内层不用再加引号
res = re.search(r"[abc]", "hello adfd")
print(res.group())  # a
# 字符枚举支持范围书写方式; 这里表示1, 2, 3, 4, 5和9, 8
res = re.search(r"[1-598]", "dfda123dfjj")
print(res.group())  # 1

# 指定重复次数, {}, 比如{2}
res = re.search(r"[123]{3}", "1292123212")
print(res.group())  # 212
# 重复次数也可以指定范围, 不过是用,隔开, 而不是-; 重复次数好像没有枚举
res = re.search(r"[123]{2,5}", "183239")
print(res.group())  # 这里注意, 32能匹配上, 但不会停, 会一直匹配到323
res = re.search(r"[123]{2,5}?", "183239")  # 后面加?开启非贪婪模式, 输出32
print(res)

# 或; 注意|的优先级最低, 所以123|423表示123或423而不是12323或12423
res = re.search("123|423", "12423")
print(res.group())

# 小测验, 匹配0-255
# 好像没啥好办法, 只能生枚举
"""
    000-009
    010-099
    100-199
    200-249
    250-255
    先不考虑1位2位的情况, 那么第一位为0或1的时候, 后面两位任意, 即[01][0-9][0-9], 考虑不足三位, 则[01]?[0-9]?[0-9]
    第一位为2的时候, 第二位[0-4], 第三位[0-9], 2[0-4][0-9]
    第一位为2, 第二位为5, 第三位[0-5], 25[0-5]
    综合: [01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]
    
    这里会有个小问题, 比如255, 由于或的关系, 匹配到25就结束了, 所以问题不是出在?, ?默认也是贪婪的, 而是出在|上
    当然, 只是判断是不是ip, 这样已经满足要求了; 但是如果要把ip提取出来, 得改一下顺序
    25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]
"""
res = re.search(r"25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]", "255")
print(res.group())
# 进一步, 匹配ip
numbers = "(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])"  # 由于|优先级比.低, 这里得加括号
pattern = "{}.{}.{}.{}".format(numbers, numbers, numbers, numbers)
print(pattern)
res = re.search(pattern, "192.168.1.1")
print(res.group())

# 如果用findall注意下, findall会把带()的拆成子组
res = re.findall(pattern, "192.168.1.1")
print(res)  # [('192', '168', '1', '1')]
# 想得到完整的匹配串, 又不想用finditer, 可以在最外层包一层括号
res = re.findall("({})".format(pattern), "192.168.1.1")
print(res)  # [('192.168.1.1', '192', '168', '1', '1')]

