# -*- coding: utf-8 -*-
# used for audio file(.wav) silience cut at head and tail.
# wt 20180126
# USAGE: 将srcTxt的内容 分条读取  写入 dstDir 文件夹中。
#    python3 p3_1ToNTxt.py txt_p1.txt txtSplitAll_p3
# 20180207:
#   优化 “×/”的替换。


import sys
import os
import shutil
import codecs
import re
from util.file_check_util import *


# give file's full path name ,chek the fold exist,if not,make it.
def foldPrepare(fullfilename0):
    fullfilename = fullfilename0
    # if fullfilename0 have '.' ，then treat it a file.
    if fullfilename.find('.') > 0:
        fullfilename, f = os.path.split(fullfilename)
    # then fullfilename is dir
    try:
        os.makedirs(fullfilename)
    except:
        pass  # print('mkdir failed.')


def strrepWT(string, orIs, tarS):
    strinfo = re.compile(orIs)
    strDst = strinfo.sub(tarS, string)
    return strDst


def traveseFileFmt2(file_dir, frmStr, fileList):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == frmStr:
                fileList.append(os.path.join(root, file))
    fileList.sort()
    return fileList


def traveseFileSpec(file_dir, fileName, fileList):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.split(file)[1] == fileName:
                fileList.append(os.path.join(root, file))
    fileList.sort()
    return fileList

def start():
    # s1: check paras;
    # print(sys.argv[0])
    # if len(sys.argv) != 3:
    #     print(len(sys.argv))
    #     print('usage:'+sys.argv[0]+' srcTxt dstDir')
    #     sys.exit()
    # srcTxt = sys.argv[1]
    # dstDir = sys.argv[2]
    srcTxt = \
        u'C:\\Data\\2.0数据采集\\09.语料\\4-type-b0p0\\data_xiaoI_8k-R-51-werResB0p0-dir\\' \
        'transcript-ok\\script.txt'
    dstDir = u'C:\\Data\\output'
    foldPrepare(dstDir)
    f0 = codecs.open(srcTxt, 'r+', 'utf-8')
    while True:
        line1 = f0.readline()
        if not line1:
            break
        else:
            # print(line1)
            _int = line1.find("	")
            finame = line1[:_int]
            lineNew = line1[_int:]
            '''
            str11 = finame[0:2]
            print("str11= "+str11)
            if str11=="*/":
                print("** str11= str11= ")
                finame = finame[2:]
                line1 = line1[2:]
            '''
            finame = strrepWT(finame, "-*/", "-")

            # print(finame)
            finame = finame + ".txt"
            fullname = os.path.join(dstDir, finame)
            f1 = codecs.open(fullname, 'w+', 'utf-8')
            f1.write(lineNew)
        f1.close()
    f0.close()
    # python3 python3 clu_txt_im.py /home/user01/ASR/4-预处理-分析程序/Data-asr/py-score-V4/txt_prepare/chengYu-ok 3.txt


def start_cp_files():
    path_source = \
        u'C:\\Data\\2.0数据采集\\09.语料\\4-type-b0p0\\data_xiaoI_8k-R-51-werResB0p0-dir\\' \
        'wav-ok'
    path_target = 'C:\\Data\\output'
    copy_files(path_source, path_target)


if __name__ == "__main__":
    start()
    # start_cp_files()