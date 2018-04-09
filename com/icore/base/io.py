# -*- coding: utf-8 -*-
# @Time    : 2017/11/23
# @Author  : LIYUAN134
# @File    : io.py
# @Commment:
#

import os
import json


def eachFile():
    filepath = 'C:\Personal\Job\语音识别\数据切分\out'
    filepath = filepath.decode('utf8')
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        print allDir
        # child = os.path.join('%s%s' % (filepath, allDir))
        # print child
        # print child.decode('utf8')  # .decode('gbk')是解决中文显示乱码问题


def loaddemo():
    msg = open('BaiduMap_cityCenter.txt', 'r').read().decode('utf8')
    print msg

    # for ii in msg:
    #     print ii
    json_str = json.dumps(msg)
    print len(json_str)
    # print json_str
    result = json.loads(json_str)
    # municipalities = result['municipalities']
    # other = result["other"]
    #
    # print other
    # print len(result)

    # for ii in result:
    #     print ii


def demo_overide():
    """
        防止覆盖文件
    """
    import os
    if not os.path.exists('somefile'):
        with open('somefile', 'wt') as f:
            f.write('Hello\n')
    else:
        print('File already exists!')


def demo_read():
    # python逐行读取文件内容的三种方法
    # 方法一：
    # f = open("foo.txt")  # 返回一个文件对象
    # line = f.readline()  # 调用文件的 readline()方法
    # while line:
    #     print line,  # 后面跟 ',' 将忽略换行符
    #     # print(line, end = '')　     # 在 Python 3 中使用
    #     line = f.readline()
    # f.close()

    # 方法二：
    for line in open("foo.txt"):
        print line,

        # 方法三：
        # f = open("c:\\1.txt", "r")
        #
        # lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
        #
        # for line in lines
        #
        #     print line


def unique(arr):
    arr1 = list(set(arr))
    arr1.sort(key=arr.index)
    return arr1


def text_distinct():
    """
        文本去重
    """
    file1 = open(u'in.txt', 'a+')
    file_out = open(u'out.txt', 'w+')
    lines = file1.readlines()
    file1.close()
    try:
        # for line in lines:
        #     line = re.sub('\s', '', line)
        #     print len(line),line
        for i in range(0, len(lines) - 1):
            lines[i] = lines[i][:-1]
        text_dealed = unique(lines)
        print len(text_dealed)

        for i in range(0, len(text_dealed) - 1):
            text_dealed[i] = text_dealed[i] + '\n'

        file_out.writelines(text_dealed)

    finally:
        # file1.close()
        file_out.close()


if __name__ == '__main__':
    demo_overide()

# eachFile()
# loaddemo()

# if __name__ == '__main__':
#     # os.chdir('C:/Personal')
#     # print os.getcwd()
#     fd = os.open('C:/Personal/test', os.O_RDWR)
#     # os.fchdir(fd)
#     # print os.getcwd()
