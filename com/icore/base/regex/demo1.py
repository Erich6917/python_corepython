# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 
# @Author  : LIYUAN134
# @File    : demo1.py
# @Commment: 
#

import re


def ssss():
    p = r'[^a-zA-Z0-9\' ]+'
    sms = "what's your name !'s'@#$#$%$%%^&^&***"
    # p= "/\p{P}/&&!/-|'/"
    c = re.sub(p, '', sms)
    print '1:', c
    print '2:', re.sub('(?<![a-zA-Z])\'', '', c)



if __name__ == '__main__':
    ssss()

