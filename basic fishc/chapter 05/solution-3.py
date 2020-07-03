# -*- coding: utf-8 -*-
# Author: Cynhia

"""
    字符串str
    之所以要和list, tuple放到一起讲, 是因为list, tuple里的很多方法str也支持
    更确切地讲, str更类似于tuple, 其内容不可改变
"""

a = "I love fishc.com"
print(a)
print(a[0])
print(a[1:3])
print(a[1:8:2])
print(a[::-1])
b = a[:5]+"****"+a[5:]
print(b)

# 内置方法, 都是返回一个新的, 而不是在原字符串上改
# 即相比list, str更接近于tuple
c = "aAAAAAAA BBB"
print(c.capitalize())  # 注意是直接返回一个新的字符串, 大小写互换?
print(c.casefold())  # 全部转换为小写
print(c.center(18, "*"))  # 居中, 参数2指定填充字符; 当width小于等于字符串长度时无变化
# 注意中文的时候会有问题, 会补过多的填充字符, 直接把一个中文字符按长度2算好像也不行
print(c.count("A", 0, 3))  # start和end参数可不指定
print(c.encode("utf-8"))  # 用指定的编码格式对字符串进行编码
print(c.endswith("A BBB", 0, 13))  # start end可不指定
print(c.expandtabs(tabsize=4))  # 把\t转换为空格, 意义不大, replace也可以实现
print(c.find("A B", 0, 13))  # 找到了返回索引, 找不到返回-1
print(c.index("A B", 0, 13))  # 找到了返回索引, 找不到抛出异常
print(c.isalnum())  # 是否仅由字母和数字组成; 空字符串认为是False
print(c.isalpha())  # 是否仅由字母组成
print(c.isdecimal())  # 是否仅包含十进制数字
print(c.isdigit(), c.isnumeric())  # 是否仅包含数字
print(c.islower(), c.isupper())  # 是否全是小写字母
print(c.isspace())  # 是否仅包含空格
print("Hello World".istitle())  # 标题字符串指每个单词首字母大写
print(c.join("*****"))  # 注意不要理解反了, 是前面的join后面的, *.join(ABC)变成A*B*C
print(c.ljust(20))  # 左对齐, 不够的补0
print(c.lower(), c.upper())  # 全部转换为小写
print(c.lstrip())  # 去掉左边的所有空格
print(c.partition("A B"))  # 用sub去分割字符串, 返回三元组, 前面的子串, sub, 后面的子串
print(c.partition("C"))  # 没找到子串, 还是返回三元组, 原串, "", ""; partition相当于把find和切片操作合并成一步了
print(c.replace(" ", "*", 3))  # count表示替换不超过count次, 可不指定
print(c.rfind("B"))
print(c.rindex("B"))
print(c.rjust(30))  # 左边用空格补齐
print(c.zfill(30))  # 左边用0补齐
print(c.rpartition("A B"))  # 从右边找到第一个sub去切分
print(c.rstrip("B"))  # strip除了可以去掉收尾空格, 也可以指定字符串去掉指定字符
print("a b c d e f g".split(" ", 3))  # 3表示最多切分3次; ['a', 'b', 'c', 'd e f g']
print("""
aaa
bbb
ccc""".splitlines())  # 按\n去切分['', 'aaa', 'bbb', 'ccc']
print(c.startswith("aA", 0, 8))
print(c.strip())
print(c.swapcase(), c.capitalize())  # capitalize有问题
print(c.title())
print(c.translate(str.maketrans("ab", "ba")))  # 多个单字符替换用replace会很麻烦, 用translate映射比较方便
# 同一分隔符多次拼接, 用+很麻烦, 灵活使用join
print("I" + " " + "like" + " " + "China")
print(" ".join(["I", "like", "China"]))


# 格式化
# 两种方法, 一种类似c里的%f, %c啥的, 不好用; 推荐用format, format支持按位置索引和按变量名索引
d = "{0}第一个插入位置{1}第二个插入位置{2}第三个插入位置".format("a", "b", "c")
print(d)
e = "{x}第一个变量{y}第二个变量{z}第三个变量".format(y="haha", x="heihei", z="hehe")
print(e)
f = "{0}加入格式控制{1:.2e}加入格式控制".format(3.1, 3.1)
print(f)  # 3.1加入格式控制3.10e+00加入格式控制


# 部分转义字符
print("\'")  # 外层是双引号这里加\也是没问题的
print("\"")
print("aaa\tbbb\nccc")
print("aaa\\bbb")
print("\x32")  # 等价于"2"


