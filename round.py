# -*- coding: utf-8 -*-

# 题目描述

# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
# 输入描述:

# 输入一个正浮点数值

# 输出描述:

# 输出该数值的近似整数值

floatnum = float(input())
intmum = int(floatnum)

result = intmum

if (floatnum - intmum) * 10 >= 5:
    result += 1

print(result) 