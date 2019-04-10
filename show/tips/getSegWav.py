# -*- coding: utf-8 -*-
'''
20181228: 从参考文本 中的时间段，截取 音频并保存。

'''
import sys
import os
import shutil
import codecs
import re
import numpy as np
import wave
import subprocess


def py_grep(srcTxt, tarStr):
    strcmd = 'grep ' + tarStr + ' ' + srcTxt
    # aa = subprocess.check_output(strcmd,shell=True)
    try:
        aa = subprocess.check_output(strcmd, shell=True)
    # print('aa= '+ str(aa))
    except Exception:
        aa = ''
    return aa


def py_wc(srcTxt):
    strcmd = 'wc -l ' + srcTxt
    aa = subprocess.check_output(strcmd, shell=True)
    num, name = aa.split()
    # print('aa= '+ str(aa))
    return int(num)


# from scipy.io import wavfile
def read_wave_data(file_path):
    # open a wave file, and return a Wave_read object
    f = wave.open(file_path, "rb")
    # read the wave's format infomation,and return a tuple
    params = f.getparams()
    # get the info
    nchannels, sampwidth, framerate, nframes = params[:4]
    # Reads and returns nframes of audio, as a string of bytes.
    str_data = f.readframes(nframes)
    # close the stream
    f.close()
    # turn the wave's data to array
    wave_data = np.fromstring(str_data, dtype=np.short)
    # for the data is stereo,and format is LRLRLR...
    # shape the array to n*2(-1 means fit the y coordinate)
    # wave_data.shape = -1, 2
    # transpose the data
    # wave_data = wave_data.T
    # calculate the time bar
    # time = np.arange(0, nframes) * (1.0/framerate)
    return wave_data, framerate


def wavSave(Xs, fullname, Fs):
    # 20180203_ for python2 
    # 默认保存16bit，采样率16k;单通道数据。
    # 设置参数
    params = (1, 2, Fs, 0, 'NONE', 'not compressed')
    # 保存文件
    wname = fullname  # sys.path[0]+'/musicAddsN.wav'
    wf = wave.open(wname, 'wb')
    # 设置参数
    wf.setparams(params)
    # 设置波形文件 .tostring()将array转换为data
    wave_data = Xs.astype(np.short)
    wf.writeframesraw(wave_data.tostring())
    wf.close()
    # print(fullname+'  wav saved.')
    return 0


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


def getStEt(line1, frameRate):
    tiStr, conStr = line1.split('     ')
    ss = tiStr.split('_')
    st = float(ss[0])
    et = float(ss[1])

    stR = st / (frameRate + 0.0)
    etR = et / (frameRate + 0.0)

    tiStr_R = str(round(stR, 2)) + '_' + str(round(etR, 2))

    return stR, etR, tiStr_R, conStr


if __name__ == "__main__":
    # s1: check paras;
    print(sys.argv[0])
    if len(sys.argv) != 6:
        print(len(sys.argv))
        print('usage: ' + sys.argv[0] + 'srcWav srcTxt dstWavDir frameRate fTime')
        sys.exit()
    srcWav = sys.argv[1]
    srcTxt = sys.argv[2]
    dstWavDir = sys.argv[3]
    frameRate = int(sys.argv[4])
    fTime = float(sys.argv[5])
    foldPrepare(dstWavDir)
    # foldPrepare(dstFile)
    # s2: travese file through dir; get file list ; make parent dir and file list;
    # fileList = traveseFileFmt(srcDir,'.txt')

    f1 = codecs.open(srcTxt, 'r+', 'utf-8')
    xxx, Fs = read_wave_data(srcWav)
    NN = len(xxx)
    print(xxx)
    print(len(xxx))
    print(Fs)
    # sys.exit()
    N = py_wc(srcTxt)
    ii = 0
    while True:
        line1 = f1.readline()
        if not line1:
            break
        else:
            ii = ii + 1
            st, et, tiStr, conStr = getStEt(line1, frameRate)
            segName = os.path.join(dstWavDir, tiStr + '.wav')
            sind = max(int(st * Fs - fTime * Fs), 0)
            eind = min(int(et * Fs), NN - 1)
            Xs = xxx[sind:eind]
            # print(Xs)
            wavSave(Xs, segName, Fs)
            print(" >>> %d / %d" % (ii, N))

    f1.close()
# python3 python3 clu_txt_im.py /home/user01/ASR/4-预处理-分析程序/Data-asr/py-score-V4/txt_prepare/chengYu-ok 3.txt
