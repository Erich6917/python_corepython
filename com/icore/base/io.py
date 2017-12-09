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


# eachFile()
# loaddemo()

