# -*-encoding-utf8-*-

# 题目描述

# •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
# 输入描述:

# 连续输入字符串(输入2次,每个字符串长度小于100)

# 输出描述:

# 输出到长度为8的新字符串数组

import sys

stringlist = []

for i in range(2):
    stringlist.append(sys.stdin.readline().strip())

for item in stringlist:
    if item == "":
        print(item)
        continue
    n = len(item) // 8
    m = len(item) % 8
    for num in range(n):
        print(item[8*num:8*num+7])
    if m != 0:
        print('{:0<8}'.format(item[-m:]))