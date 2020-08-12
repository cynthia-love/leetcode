# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    控制流程
"""

"""条件语句"""
door_closed = True
door_locked = True

if door_closed:
    if door_locked:
        print("开锁")
    print("开门")
print("其他操作")

x = 100
if x > 100:
    print("aaa")
elif x > 10:
    print("bbb")
else:
    print("ccc")

"""循环语句"""
x = "dkXfjdkaf"
index = 0
while index <= len(x)-1 and x[index] != 'X':
    index += 1
else:
    print("非中途break则执行此部分")
# 测试条件, 符合->执行循环体->测试条件
# 所以这里while的意义是, 如果当前字符不是'X', 那就往后移一位
# 退出条件是当前字符是'X', 或者index移动到了字符串范围外
print(index if index <= len(x)-1 else "不存在")

# 对于list, tuple, str, set, dict, file等可迭代的对象, for比while更适合
s = {1, 2, 3, 4, 5}
sum_s = 0
for each in s:
    sum_s += each

print(sum_s)

# 还可以根据索引遍历
s = [8, 7, 6, 5, 4]
for i in range(len(s)):
    if s[i] == 100:
        print(i)
        break  # break终止整个循环, continue终止当前循环后续代码
else:
    print("未找到")
