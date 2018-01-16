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
