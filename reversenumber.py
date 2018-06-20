# -*- coding: utf-8 -*-

# 题目描述

# 描述：

# 输入一个整数，将这个整数以字符串的形式逆序输出

# 程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001

# 输入描述:

# 输入一个int整数

# 输出描述:

# 将这个整数以字符串的形式逆序输出

from functools import reduce


def main():
    inputnumber = input()

    outputnumber = list(reversed(inputnumber))

    print(reduce(lambda a, b: a + b, outputnumber))


if __name__ == '__main__':
    main()