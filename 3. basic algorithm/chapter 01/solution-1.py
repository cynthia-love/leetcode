# -*- coding: utf-8 -*-
# Author: Cynthia
"""
    第1章, Python入门

"""
"""
    第一个示例程序, 输入成绩等级输出绩点
"""
print('Welcome to the GPA calculator')
print('Please enter all your letter grades, one per line')
print('Enter a blank line to designate the end')

s2f = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
    'C+': 2.33, 'C': 2.0, 'D+': 1.33, 'D': 1.0, 'F': 0.0
}

list_gpa = []

while True:
    pin = input()
    if pin == '':
        break
    elif pin not in s2f:
        print('Unknown grade {} being ignored'.format(pin))
    else:
        list_gpa.append(s2f[pin])

if list_gpa:
    print("Your GPA is {:.2f}".format(sum(list_gpa)/len(list_gpa)))
