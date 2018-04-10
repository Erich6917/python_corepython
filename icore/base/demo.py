# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 
# @Author  : LIYUAN134
# @File    : demo.py
# @Commment: 
#
import re


def start():
    # run_go()
    # ss = '(123)去掉了吗？（456）'
    # test(ss)
    # s = "abc(hello)casdf"
    # sss = re.findall(r'[^()]+', s)[1]
    # print sss
    # pattern = r'/(.*?)/'
    # pattern = '(?<= \()'
    # pattern = '\（[^）]*\）'

    pattern = u'(\([^)]+\))|(（[^）]+）)'  # 写法1
    pattern = u'[(（][^)）]*[)）]'  # 写法1 变形
    pattern = u'\(.*?\)'  # 写法2 仅支持 英文
    pattern = u'\(.*?\)|(\（.*?\）)'  # 写法2.2 不支持混写
    pattern = u'[(（].*?[)）]'  # 写法2.1 支持中英混写，即中文左括号和英文右括号

    # c = re.sub(pattern, ' ', u'（啊实打实的 ）阿萨德阿萨德阿萨德玩的阿萨德(123311)asd()')
    c = re.sub(pattern, ' ', '(啊实打实的 ）阿萨德阿萨德阿萨德玩的阿萨德(123311)asd')
    print c


if __name__ == '__main__':
    start()
