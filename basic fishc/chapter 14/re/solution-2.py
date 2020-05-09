# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    一些常见的特殊字符(包括本身就是的特殊字符.~$*+?{}[]\|(); 以及\+普通字符变成的特殊字符, \d, \S等
"""

import re

# .   匹配除换行符外的任何字符
print(re.search(r".", "a"))

# |   表示或者
print(re.search(r"a|b", "b"))

# ^   匹配开始位置
print(re.search(r"^abc", "dabc"))  # None, 相当于match

# $   匹配结束位置
print(re.search(r"abc$", "abcd"))  # None

# \   将特殊字符变成普通字符, 将普通字符变成特殊字符
print(re.search(r"\.", "a.b"))  # .
print(re.search(r"\d", "123"))  # 1

# []   字符枚举, 比较特殊的有-, 出现在中间作为范围从x到x, 其他地方作为普通字符
# ^   出现在首位表示不包含, 其他地方作为普通字符; 除了这两种特殊情况, 其他字符除\外, 在[]里都作为普通字符
print(re.search("[abc]", "xyaz"))  # a
print(re.search("[1-8]", "7"))  # 7
print(re.search("[-8]", "-"))  # -
print(re.search("[\-8]", "-8"))  # -, 这里的\等于没加
print(re.search("[.8]", "."))  # .
print(re.search("[^\da]", "akdfj"))  # 非数字非a, 所以匹配到k
print(re.search("[a^b]", "^"))  # ^


# {m,n}, 注意几个变体{m}恰好, {,n}至多, {m,}至少
print(re.search("a{3}", "bbaaad"))  # aaa
print(re.search("a{3,5}", "bbaaaad"))  # aaaa
print(re.search("a{,5}", "bbaaaaad"))  # 注意这里, 至多5次, 0也符合, 所以空字符""会优先返回
print(re.findall("a{,5}", "bbaaaaad"))  # ['', '', 'aaaaa', '', ''], 有点怪
print(re.search("a{6,}", "bbaaaaaadd"))  # aaaaaa

# *, 匹配0次或多次
print(re.search("ab*", "a"))  # a
print(re.search("ab*", "abbbb"))  # abbbb

# +, 匹配1次或多次
print(re.search("ab+", "ab"))  # ab

# ?, 匹配0次或1次, 注意?默认也是贪婪模式, 往多了匹配
print(re.search("ab?", "ab"))  # ab
print(re.search("a[cdb]?", "ab"))
# ?除了单独用, 还可以和*+?{m,n}这些表示次数的配合用, 表示开启其非贪婪模式
print(re.search("ab*?", "abbbb"))  # a符合条件吗, 符合, 那就不往后匹配了
print(re.search("ab+?", "abbbb"))  # ab符合条件吗, 符合, 那就不往后匹配了
print(re.search("ab??", "abbbb"))  # a符合条件吗, 符合, 那就不往后匹配了
print(re.search("ab{3,5}?", "abbbbbb"))  # abbb就结束匹配, 而不是继续匹配到abbbbb
print(re.search("<.*>", "<aaa><bbb><cccc>"))  # 默认贪婪方式, <aaa><bbb><cccc>
print(re.search("<.*?>", "<aaa><bbb><ccc>"))  # 在表示重复的特殊字符后加?开启非贪婪方式, 匹配到就立刻返回<aaa>

# ()用于确定优先级以及指定子组; 特别地, 子组内容可以以数字引用
res = re.search("(\w*) (\w*) (\w*)", "aa bb ef.gh")
print(res.group(), res.groups())  # aa bb ef ('aa', 'bb', 'ef')


# ***********************************************************************************
# (?...), 类似于[^...], 是一种正则的扩展语法; 感觉意义不大还复杂, re方法里都自带flag, 用那个就行

print(re.search(r"Aa", "adfdjkjaa", re.I))  # aa, re.I, 大小写不敏感, 一般re.I有点用, 其他没啥用
print(re.search(r"aa.*bb", "aa\n\nbb", re.M|re.S))  # re.M, 多行匹配; re.S, 使.也能匹配到\n


# ************************************************************************************
# \, 用于把特殊字符变成普通字符, 把普通字符变成特殊字符
print(re.search(r"(aa)xx\1", "aaxxaabbbaa"))  # aaxxaa
# \1表示引用子组1所匹配的字符串; 注意是所匹配到的字符串, 而不是子组
# 看下面这个, 为什么ip匹配不能写成这样; \1匹配到的是192, 而不是25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]
print(re.search(r"(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])!\1!\1!\1", "192!192!192!192"))
# 所以只能匹配到192!192!192!192, 而匹配不到192!168!1!2这种四个数不同的

# \b, 匹配单词边界, 可以是空字符, ., ()等等
# 有时候搜索一一个子串, 要求这个子串是一个独立单词, 比如想找到单词var, 而不是variable的前三个字符
print(re.search(r"\bFishC\b", "love FishC"))  # FishC
print(re.search(r"\bFishC\b", "loveFishC"))  # None
print(re.search(r"\bFishC\b", "(FishC)"))  # FishC

# \B与\b相反, 匹配到的子串不能是个独立单词
print(re.search(r"fish\B", "fish."))  # None
print(re.search(r"fish\B", "fishing")) # fish
print(re.search(r"\bfish\B", "fishaaa")) # fish, 前有边界后不能有


# \d, 匹配数字
print(re.search(r"\d", "2"))
# \D, 匹配非数字
print(re.search(r"\Daaa", "xaaa"))  # xaaa

# \s, 匹配空白字符
print(re.search("\s", "aa bb"))  # " "
# \S, 匹配非空白字符
print(re.search("\S", "    b"))  # b

# \w, 单词字符, 注意是字符, 不是一整个单词, 一般指[a-zA-Z0-9]
print(re.search("\w", "hello world"))  # h
# \W, 非单词字符
print(re.search("\W", "hello world"))  # " "







