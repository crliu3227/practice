# !-*-coding:utf-8-*-
# 题目描述
# 开发一个坐标计算工具，A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
# 从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

# 输入：
# 合法坐标为A(或者D或者W或者S)+数字（两位以内）
# 坐标之间以;分隔。
# 非法坐标点需要进行丢弃。如AA10;A1A;$%$;YAD;等。
# 下面是一个简单的例子如：
# A10;S20;W10;D30;X;A1A;B10A11;;A10;

# 处理过程：
# 起点（0,0）
# +A10=（-10,0）
# +S20=(-10,-20)
# +W10=(-10,-10)
# +D30=(20,-10)
# +x=无效
# +A1A=无效
# +B10A11=无效
# +一个空不影响
# +A10=(10,-10)
# 结果（10，-10）

# 输入描述:
# 一行字符串
# 输出描述:
# 最终坐标，以,分隔
# 示例1
# 输入
# A10;S20;W10;D30;X;A1A;B10A11;;A10;
# 输出
# 10,-10

import re


class cordinate(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move(self, direction):
        if direction[0] == 'A':
            self._x -= int(direction[1:])
        elif direction[0] == 'D':
            self._x += int(direction[1:])
        elif direction[0] == 'W':
            self._y += int(direction[1:])
        elif direction[0] == 'S':
            self._y -= int(direction[1:])
        else:
            raise ValueError("invalid direction")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y


def main():
    # '^'match begining, '$' match end
    cordinateStandard = re.compile('^[ADWS][0-9]{1,2}$')
    cordinateInput = str(input()).split(';')
    directions = list(filter(lambda x: re.match(cordinateStandard, x), cordinateInput))

    myCordinate = cordinate()

    for d in directions:
        myCordinate.move(d)

    print('{0},{1}'.format(myCordinate.x, myCordinate.y))


if __name__ == '__main__':
    main()

