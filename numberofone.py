# -*- coding: utf-8 -*-

# 题目描述
# 输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数.

# 输入描述:
#  输入一个整数（int类型）

# 输出描述:
# 这个数转换成2进制后，输出1的个数


def main():
    binaryInput = bin(int(input()))

    numberofone = str(binaryInput).count("1")

    print(numberofone)
    
if __name__ == '__main__':
    main()