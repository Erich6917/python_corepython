# -*- coding: utf-8 -*-
'''
20181022: used for caldulate time ; ok

'''
import sys
import os
import shutil
import codecs
import re
import librosa


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


# wrong -2018016-not ok ;
def traveseFileFmt3(srcDir, frmStr, fileList):  # srcDir = /wav
    # print('start  traveseFileFmt ********** ')
    for file1 in os.listdir(srcDir):  # file1 = wav/dev,test,train
        srcDir = os.path.join(srcDir, file1)
        if os.path.isdir(srcDir):
            fileList = traveseFileFmt2(srcDir, frmStr, fileList)
            # listdir(srcDir,frmStr,fileList)
        else:
            if srcDir[-4:] == frmStr:
                fileList.append(srcDir)
                print(srcDir + '\n')
                # rint('end  traveseFileFmt ********** ')
    fileList.sort()
    return fileList


'''def traveseFileFmt2(srcDir,frmStr): # srcDir = /wav
    print('start   traveseFileFmt ********** ')     
    fileList = []
    print('srcDir= ')
    print(srcDir)
    temS= srcDir[-1]
    if ~(temS=='/'):
        srcDir = srcDir+'/'
    for file1 in os.listdir(srcDir):           # file1 = wav/dev,test,train
        srcDir2 = srcDir+file1  # srcdir2 = wav/dev,test,train
        temS= srcDir2[-1]
        #print(srcDir4)
        if srcDir2[-4:]==frmStr:
            fileList.append(srcDir2)
    print('end  traveseFileFmt ********** ')                            
    return fileList   
'''


def traveseFileFmt2(file_dir, frmStr, fileList):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == frmStr:
                fileList.append(os.path.join(root, file))
    fileList.sort()
    return fileList


def removeALL(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file0 in files:
            os.remove(os.path.join(root, file0))
    os.rmdir(file_dir)


# 从spk+id的 文件名中分割除 spk 和 utt-ID
def spkIDsplit(instr):
    liSTR = re.findall(r'\d+', instr)
    ID = liSTR[-1]
    num = len(ID)
    spkIDstr = instr[:-num]
    return spkIDstr, ID


def getTimeLenSec(file0):
    y, sr = librosa.load(file0, sr=None)
    timeLen = librosa.get_duration(y, sr)

    return timeLen


if __name__ == "__main__":
    # s1: check paras;
    # print(sys.argv[0])
    # if len(sys.argv) != 4:
    #     print(len(sys.argv))
    #     print('usage: ' + sys.argv[0] + 'srcDir dstDir timeLenTxt')
    #     sys.exit()
    #
    # srcDir = sys.argv[1]
    # dstDir = sys.argv[2]
    # timeLenTxt = sys.argv[3]

    srcDir = 'C:\Users\Administrator\Desktop\count\wav'
    dstDir = 'C:\Users\Administrator\Desktop\count\output'
    timeLenTxt = 'aa.txt'

    foldPrepare(dstDir)
    # foldPrepare(dstFile)
    # s2: travese file through dir; get file list ; make parent dir and file list;
    # fileList = traveseFileFmt(srcDir,'.txt')
    fileList = []
    frmStr = '.wav'
    fileList = traveseFileFmt2(srcDir, frmStr, fileList)
    timeAll = 0
    for file0 in fileList:
        newName = strrepWT(file0, srcDir, dstDir)

        # newName = strrepWT(newName,'.wav','.txt')
        #
        timeLen = getTimeLenSec(file0)
        timeAll = timeAll + timeLen
        #
        # i = i+1
        foldPrepare(newName)
        print(file0)
        print(newName)
        f1 = codecs.open(newName[:-4] + '-Sec.txt', 'w+', 'utf-8')
        timeLenStr = str(timeLen) + ' sec'
        f1.write(timeLenStr)
        f1.close()

    f1 = codecs.open(timeLenTxt, 'w+', 'utf-8')
    f1.write(srcDir + '\n')
    timeLenStr = 'all time long = ' + str(timeAll) + ' sec' + ' = ' + str(timeAll / 3600.0) + ' hours'
    f1.write(timeLenStr)
    f1.close()
# python3 python3 clu_txt_im.py /home/user01/ASR/4-预处理-分析程序/Data-asr/py-score-V4/txt_prepare/chengYu-ok 3.txt
