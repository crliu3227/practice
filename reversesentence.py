# -*- coding: utf-8 -*-

# 题目描述

# 将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
# 所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
 
# 输入描述:

# 将一个英文语句以单词为单位逆序排放。

# 输出描述:

# 得到逆序的句子


def main():
    sentencelist = input().split()

    sentencelist.reverse()

    for word in sentencelist:
        print(word, end=" ")


if __name__ == '__main__':
    main()
