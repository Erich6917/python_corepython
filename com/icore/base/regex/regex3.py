# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 
# @Author  : LIYUAN134
# @File    : regex3.py
# @Commment: 
#


def demo1():
    import re

    text = "Weather now : Mildly-sunny34 Weather tomorrow : Cloudy"

    # Capture one-or-more characters of non-whitespace after the initial match
    match = re.search(r'Weather now : (\S+)', text)

    if match:
        weather = match.group(1)
        print('weather: {}'.format(weather))


if __name__ == '__main__':
    demo1()
