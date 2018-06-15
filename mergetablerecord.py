# -*- coding: utf-8 -*-

# 题目描述

# 数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
# 输入描述:

# 先输入键值对的个数
# 然后输入成对的index和value值，以空格隔开

# 输出描述:

# 输出合并后的键值对（多行）

num = int(input())
table = dict()

for i in range(num):
    k, v = map(int, input().split())
    table[k] = table.setdefault(k, 0) + v

for k in sorted(table):
    print(k, table[k])
    
