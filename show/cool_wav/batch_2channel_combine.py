# -*- coding: utf-8 -*-
#! bin/python3
'''
usage: 

    python batch_2channel_combine.py   srcDir   tarDir

function :
    用于批处理 srcDir 中的wav, 
    如果 wav是双通道，并且量通道内容一样，则保留一个通道，存入 tarDir,原始双通道 保留在 srcDir中。 
    如果 wav是单通道，则移动到 tarDir, 
    如果 wav是双通道，并且 通道内容不一样，则移动到 tarDir。 

'''

# 
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin
from numpy import pi
from numpy import log10
import os, sys
import soundfile
import librosa
import librosa.display
import shutil
import codecs
import re


# from matplotlib.pyplot import specgram
# ********************************* add noise ************************************

# ********************************* wavSave + read --end  ************************************
# ********************************* tool  ************************************
# calsulate the nearest exp of 2. : 100-> 7;1000->10;
def nextpow2(x):
    if (x == 0):
        y = 0;
    else:
        y = np.ceil(math.log2(x))
    return y


# ********************************* filter --end  ************************************
# ********************************* main  ************************************
def enframe(x, win, inc):
    inc = int(inc)
    '''print("inc = ")
    print(inc)'''
    # window or win length
    wlenMark = 0;
    # python2 use bellow
    # if str(type(win))=="<type 'numpy.ndarray'>": # win is an array of win.;
    # python3 use bellow
    if str(type(win)) == "<class 'numpy.ndarray'>":
        wlen = len(win)
    else:
        wlen = win
        wlenMark = 1
    # inc judge
    if inc <= 0:
        print('*************************************************************')
        print('***** wrong in : ******* enframe(x,win,inc):' + 'inc =0,must >0')
        print('*************************************************************')
        return
    # splice to frame
    N = len(x)
    # log(inc,99)
    frmNum = int(np.floor((N - (wlen - inc)) / inc))
    # print("frmNum1 = "+ str(frmNum))
    frmNum = int(np.floor((N - (wlen - inc)) / inc) + 1)
    # print("frmNum2 = "+ str(frmNum))
    pad0num = frmNum * inc + wlen - inc - N
    # pad 0
    padArr = np.zeros(pad0num)
    # print("padArr= "+ str(padArr))

    x = np.append(x, padArr)
    N = len(x)
    shiftN = np.arange(0, frmNum * inc + 1, inc);
    xFrame = np.zeros([wlen, frmNum])
    frmSE = np.zeros([frmNum, 2])
    if wlenMark == 1:  # rectangle window
        for i in np.arange(0, frmNum):
            xFrame[:, i] = x[shiftN[i]:shiftN[i] + wlen]
            frmSE[i, :] = [shiftN[i], shiftN[i] + wlen - 1]
    else:
        for i in np.arange(0, frmNum):
            xFrame[:, i] = x[shiftN[i]:shiftN[i] + wlen] * win;
            frmSE[i, :] = [shiftN[i], shiftN[i] + wlen - 1]
    return xFrame, frmNum, frmSE, wlen, padArr


def get_fft_spectrum(data, Fs):
    # Pxx, freqs, bins, im = plt.specgram(data, int(Fs * 0.02), Fs, Fs - int(0.01 * Fs))
    wlen = np.hamming(int(0.02 * Fs))
    nFFT = len(wlen)
    featNum = int(nFFT / 2)
    inc = int(0.01 * Fs)
    Y1, nFrm, frmSE, nwlen, padArr = enframe(data, wlen, inc)  #
    xSpectrum = np.zeros((nFrm, featNum))
    for i2 in np.arange(0, nFrm):  # i2 in np.arange(0,1):#for
        xFrm = Y1[:, i2]
        Sp = abs(np.fft.fft(xFrm, nFFT))  # 使用fft函数对余弦波信号进行傅里叶变换。
        Sp = Sp[0:featNum]
        xSpectrum[i2, :] = Sp
    return xSpectrum


def traveseFileFmt2(file_dir, frmStr):
    fileList = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == frmStr:
                fileList.append(os.path.join(root, file))
    fileList.sort()
    return fileList


def strrepWT(string, orIs, tarS):
    strinfo = re.compile(orIs)
    strDst = strinfo.sub(tarS, string)
    return strDst


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


if __name__ == "__main__":
    print(sys.argv[0])
    if len(sys.argv) != 3:
        print(len(sys.argv))
        print('usage: voice-process.py  file_dir tarDir')
        sys.exit()
    file_dir = sys.argv[1]
    tarDir = sys.argv[2]
    fileList = traveseFileFmt2(file_dir, '.wav')
    f = codecs.open(os.path.join(file_dir, 'channel_MSG.txt'), 'w+', 'utf-8')

    N = len(fileList)
    for ii in range(0, N):
        tarFile = fileList[ii]  # 150228-p3.wav'
        # tarFile = 'car-n.wav'
        # file get*****************************************************
        X, Fs = soundfile.read(tarFile)
        if len(X.shape) <= 1:
            print('--->%d/%d   %s  :has 1 channel. jump it !' % (ii, N, tarFile))
            newName = strrepWT(tarFile, file_dir, tarDir)
            shutil.move(tarFile, newName)
            f.write(str(ii) + '\t chnnel Num = 1, ----- \t' + tarFile + '\n')
            # sys.exit()
            continue
        # X = X[:3*Fs,:]
        mm = np.max(X) + 0.0
        X = X / mm

        X0 = X[:, 0]
        X1 = X[:, 1]
        X2 = X1 - X0

        print('--->     energy:')
        # print(sum(X0*X0))
        # print(sum(X1 * X1))
        # print(sum(X2 * X2))
        energyRadio = sum(X2 * X2) / min((sum(X1 * X1) + 0.0), (sum(X0 * X0) + 0.0))
        print(energyRadio)

        if energyRadio < 0.1:
            print('--->%d/%d   %s  :has 2 same channel. reWrite it !' % (ii, N, tarFile))
            newName = strrepWT(tarFile, file_dir, tarDir)
            foldPrepare(newName)
            # os.remove(tarFile)
            soundfile.write(newName, mm * X0, Fs)
            f.write(str(ii) + '\t chnnel Num = 2, same \t' + tarFile + '\n')
        else:
            print('--->%d/%d   %s  :has 2 different channel. keep it !' % (ii, N, tarFile))
            newName = strrepWT(tarFile, file_dir, tarDir)
            shutil.move(tarFile, newName)
            f.write(str(ii) + '\t chnnel Num = 2, differ \t' + tarFile + '\n')
        if 0:
            xSpectrum0 = get_fft_spectrum(X0, Fs)
            xSpectrum1 = get_fft_spectrum(X1, Fs)
            xSpectrum2 = get_fft_spectrum(X2, Fs)

            N = len(X0)
            t = np.linspace(0, N, N) / (Fs + 0.0)
            plt.figure()
            plt.subplot(231)
            plt.plot(t, X0)
            plt.subplot(232)
            plt.plot(t, X1)

            plt.subplot(234)
            librosa.display.specshow(xSpectrum0, x_axis='time')
            plt.subplot(235)
            librosa.display.specshow(xSpectrum1, x_axis='time')
            plt.subplot(233)
            plt.plot(t, X2)

            plt.subplot(236)
            librosa.display.specshow(xSpectrum2, x_axis='time')

            plt.show()
    f.close()

    print(' end ok !')
