# -*- coding: utf-8 -*-

# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
# 输入描述:

# 输入一个int型整数

# 输出描述:

# 按照从右向左的阅读顺序，返回一个不含重复数字的新的整数


def main():
    numberlist = list(input())

    numberlist.reverse()

    output = []
    for num in numberlist:
        if num in output:
            continue
        output.append(num)

    for out in output:
        print(out, end='')


if __name__ == "__main__":
    main()