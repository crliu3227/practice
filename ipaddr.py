# 题目描述
# 请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类.

# 所有的IP地址划分为 A,B,C,D,E五类
# A类地址1.0.0.0~126.255.255.255;
# B类地址128.0.0.0~191.255.255.255;
# C类地址192.0.0.0~223.255.255.255;
# D类地址224.0.0.0~239.255.255.255;
# E类地址240.0.0.0~255.255.255.255

# 私网IP范围是:
# 10.0.0.0～10.255.255.255
# 172.16.0.0～172.31.255.255
# 192.168.0.0～192.168.255.255

# 子网掩码为前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
# 本题暂时默认以0开头的IP地址是合法的，比如0.1.1.2，是合法地址

# 输入描述:
# 多行字符串。每行一个IP地址和掩码，用~隔开。
# 输出描述:
# 统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开.

import re


# 判断IP是否合法
# params：ipaddr string pattern is '10.10.10.10'
# return: True ipaddr is valid
def validIP(ipaddr):
    r = re.compile('([0-9]{1,3}.){3}[0-9]{1}')

    if re.match(r, ipaddr):
        for i in map(int, ipaddr.split('.')):
            if i > 255 or i < 0:
                return False
    else:
        return False
    return True


# 判断Mask是否合法
# params：mask string pattern is '255.255.255.0'
# return: True mask is valid
def validMask(mask):
    if not validIP(mask):
        return False

    binstr = ""
    for b in map(bin, map(int, mask.split('.'))):
        binstr += str(b).lstrip('0').lstrip('b').rjust(8, '0')

    flag = 0
    for s in binstr:
        if s == '0':
            flag = 1
        if flag == 1 and s != '0':
            return False

    return True


# 根据ip以及mask得到网络
# param: ip, mask string pattern 192.168.1.1
# return: network 2进制链表 [11000000, 10101000, 0, 0]
def getNetwork(ip, mask):
    iplist = ip.split('.')
    masklist = mask.split('.')

    network = []
    for n in range(len(iplist)):
        network.append(int(iplist[n]) & int(masklist[n]))

    return network


def isNetEqual(net1, net2):
    if(len(net1) != len(net2)):
        return False

    for i in range(len(net1)):
        if(net1[i] != net2[i]):
            return False

    return True


def isPrivate(ip, mask):
    privateNet = []
    privateNet.append(getNetwork('10.0.0.0', '255.0.0.0'))
    privateNet.append(getNetwork('192.16.0.0', '255.240.0.0'))
    privateNet.append(getNetwork('192.168.0.0', '255.255.0.0'))

    currNet = getNetwork(ip, mask)

    for net in privateNet:
        if isNetEqual(net, currNet):
            return True

    return False


def main():
    wrongIPNum = 0
    wrongMaskNum = 0
    ANum = 0
    BNum = 0
    CNum = 0
    DNum = 0
    ENum = 0
    privateNum = 0

    s = input().split()
    for ss in s:
        inputstr = str(ss).split('~')

        if not validIP(inputstr[0]):
            wrongIPNum += 1
            continue

        if not validMask(inputstr[1]):
            wrongMaskNum += 1
            continue

        binip = ""
        for b in map(bin, map(int, inputstr[0].split('.'))):
            binip += str(b).lstrip('0').lstrip('b').rjust(8, '0')

        if binip[0] == "0":
            ANum += 1
        elif binip[0:2] == "10":
            BNum += 1
        elif binip[0:3] == "110":
            CNum += 1
        elif binip[0:4] == "1110":
            DNum += 1
        elif binip[0:5] == "11110":
            ENum += 1

        if isPrivate(inputstr[0], inputstr[1]):
            privateNum += 1

    print(ANum, BNum, CNum, DNum, ENum, wrongIPNum, wrongMaskNum, privateNum)


if __name__ == '__main__':
    main()