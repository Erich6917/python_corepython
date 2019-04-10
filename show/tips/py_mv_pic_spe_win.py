# -*- coding: utf-8 -*-
'''
20181229:
本程序主要实现三个功能：
    1，调用ffmpeg 实现 输入视频到  音频、视频图像 的转换；（需要制定转换帧率， 音频采样率，通道数目）
    2，对获得的图像进行 裁剪；（需要手动调整裁剪位置）
    3，（外部）调用 ocr 对 裁剪得到的图像进行识别，获得文本；
    4, 根据 第三步的文本，以及第一步的 音频， 获得单段的音频。


'''
import sys
import os
import shutil
import codecs
import re
import numpy as np
import wave
import subprocess
from PIL import Image
import json
from PIL import ImageGrab


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


def getSegWav(srcWav, srcTxt, dstWavDir, frameRate, fTime):
    foldPrepare(dstWavDir)
    f1 = codecs.open(srcTxt, 'r+', 'utf-8')
    xxx, Fs = read_wave_data(srcWav)
    NN = len(xxx)
    # print(xxx)
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
    return 0


def ffmpeg_get_audio(srcWav, tarAudio, Fs, chNum, sTime, eTime):
    foldPrepare(tarAudio)
    pa, ext = os.path.splitext(srcWav)
    if (ext == '.mkv') or (ext == '.rmvb') or (ext == '.mp4'):
        # print()
        # strcmd = 'ffmpeg -i '+file0+" -ar 16000 -ac 1 "+file0[:-4]+'.wav'
        # strcmd =  ffmpeg -ss 300 -i wdyzzbp.mkv -to 600 -ar 16000 -ac 1 wdyzzbp.mkv-300-600-1ch-16k.wav
        strcmd = 'ffmpeg -ss ' + str(sTime) + ' -i ' + srcWav + ' -to ' + str(eTime) + ' -ar ' + str(
            Fs) + ' -ac ' + str(chNum) + ' ' + tarAudio
        #
        subprocess.call(strcmd, shell=True)
        print(' ::: <ffmpeg_get_audio> succeed finished  ~ ~')
    else:
        print(' movie format is not supported !')
    return 0


def ffmpeg_get_jpg(srcWav, dstPicDir, frameRate):
    foldPrepare(dstPicDir)
    pa, Name = os.path.split(srcWav)
    pureName, ext = os.path.splitext(Name)
    if (ext == '.mkv') or (ext == '.rmvb') or (ext == '.mp4') :
        # strcmd = 'ffmpeg -i '+file0+" -ar 16000 -ac 1 "+file0[:-4]+'.wav'
        # strcmd =  ffmpeg -ss 300 -i wdyzzbp.mkv -to 600 -ar 16000 -ac 1 wdyzzbp.mkv-300-600-1ch-16k.wav
        # strcmd = 'ffmpeg -ss 300 -i wdyzzbp.mkv -to 600 -copyts -vf fps=3  /Users/king/Desktop/codec/py_ocr/wdyzzbp-3frt/wdyzzbp_3frt-%d.jpg
        dstPicDirStr = os.path.join(dstPicDir, pureName + '_' + str(frameRate) + 'frt' + '-%d.jpg')
        strcmd = 'ffmpeg -ss ' + str(sTime) + ' -i ' + srcWav + ' -to ' + str(eTime) + ' ' + '-copyts -vf fps=' + str(
            frameRate) + ' ' + dstPicDirStr
        #
        subprocess.call(strcmd, shell=True)
        print(' ::: <ffmpeg_get_jpg> succeed finished  ~ ~')
    else:
        print(' movie format is not supported !')
    return 0


def cut_batch(dstPicDir, dstPicDir_cut,len_to_end):
    # /Users/king/Desktop/codec/py_ocr/wdyzzbp-3frt/ /Users/king/Desktop/codec/py_ocr/wdyzzbp-3frt-cut/
    srcDir = dstPicDir
    cutDir = dstPicDir_cut
    foldPrepare(cutDir)
    '''
    if srcDir[-1:]=='/':
        #noTxtDir = srcDir[:-1]+'-noTxt'
        total_txt = srcDir[:-1]+"_ocr_all.txt"
    else:
        #noTxtDir = srcDir+'-noTxt'
        total_txt = srcDir[:-1]+"_ocr_all.txt"
     '''
    frmStr = '.jpg'
    n = len(frmStr)
    if os.path.splitext(srcDir)[1] == frmStr:
        print(">>>>>> please input a picDir but not a pic <<<<<<<<")
    else:
        # total_txt = os.path.join(pa,dirname+"_ocr_all.txt")
        # foldPrepare(total_txt)
        # f0 = codecs.open(total_txt, 'w+','utf-8')
        fileList = []
        fileList = traveseFileFmt2(srcDir, frmStr, fileList)

        cnt = 0
        N = len(fileList)

        for pic in fileList:
            pa, dirname = os.path.split(pic)
            image = Image.open(pic)
            # 截取目标部分：
            llen, hig = image.size
            # box = (0,hig-70,llen,hig)  （tmz)
            # box = (0,hig-60,llen,hig-30)
            # box = (0,hig-65,llen,hig-25) (tyzl)
            # box = (0, hig - 110, llen, hig - 73)
            #box = (0, hig - 70, llen, hig - 20) 我的恶魔
            box = (100, hig - (len_to_end+50), llen-100, hig - 50)
            img = image.crop(box)
            # img.show()
            # 保存 
            cutName = os.path.join(cutDir, dirname)
            img.save(cutName[:-n] + "-cut" + frmStr)  #
            cnt = cnt + 1
            print("  " + str(cnt) + '/' + str(N))
        print(" ::: <cut_batch> succeed finished  ~ ~")

def start_demo():
    # s1: check paras;
    print(sys.argv[0])
    if len(sys.argv) != 4:
        print(len(sys.argv))
        print('usage: ' + sys.argv[0] + ' srcWav dstDir frameRate')
        sys.exit()
    srcWav = sys.argv[1]
    dstDir = sys.argv[2]
    len_to_end = sys.argv[3]
    frameRate = 1  # int(sys.argv[3])
    # fTime = float(sys.argv[4])
    # set by hand :
    Fs = 16000
    chNum = 1
    sTime = 5 * 60  # sec
    eTime = 40 * 60  # sec

    pa, Name = os.path.split(srcWav)
    pureName, ext = os.path.splitext(Name)

    dstPicDir = os.path.join(dstDir, pureName + '-' + str(sTime) + '-' + str(eTime) + '-pic-dir-full')
    dstPicDir_cut = os.path.join(dstDir, pureName + '-' + str(sTime) + '-' + str(eTime) + 'pic-dir-cut')
    tarAudio = os.path.join(dstDir, pureName + '-' + str(sTime) + '-' + str(eTime) + '-1ch-16k.wav')

    if os.path.isdir(dstPicDir):
        removeALL(dstPicDir_cut)
    ffmpeg_get_audio(srcWav, tarAudio, Fs, chNum, sTime, eTime)
    ffmpeg_get_jpg(srcWav, dstPicDir, frameRate)

    #
    # cut_batch(dstPicDir, dstPicDir_cut,len_to_end)

    # ocr process ;
    # getSegWav(srcWav,srcTxt,dstWavDir,frameRate,fTime)

    #   python py_mv_pic_ocr_spe.py /Users/king/Desktop/codec/py_movie_pic_ocr_speech/wdyzzbp.mkv /Users/king/Desktop/codec/py_movie_pic_ocr_speech/dest

# def start_loop():
#

def get_all_files_path_name(path_source='.'):
    file_list = []
    for root, dirs, files in os.walk(path_source):
        for filename in files:
            file_msg = filename, os.path.join(root, filename), root
            file_list.append(file_msg)
    return file_list
def getLenTime(filename):
    command = ["ffprobe.exe","-loglevel","quiet","-print_format","json","-show_format","-show_streams","-i",filename]
    result = subprocess.Popen(command,shell=True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    out = result.stdout.read()
    # temp = str(out.decode('gbk'))
    data = json.loads(out)["format"]['duration']
    return int(float(data))

def getTimeSec(file0):
    import librosa
    y,sr = librosa.load(file0,sr=None)
    timeLenSec = librosa.get_duration(y,sr)

    return timeLenSec

if __name__ == "__main__":
    # s1: check paras;
    # print(sys.argv[0])
    # if len(sys.argv) != 4:
    #     print(len(sys.argv))
    #     print('usage: ' + sys.argv[0] + ' srcWav dstDir frameRate')
    #     sys.exit()
    source_path = 'D:/yuan/movie'
    file_list = get_all_files_path_name(source_path)
    for each in file_list:
        file_name,file_path = each[0],each[1]
        print file_name.decode('gbk')
        time_total = getLenTime(file_path)
        if time_total < 5*60:
            print '时长小于10分钟，跳过',file_name
            continue


        srcWav = file_path #sys.argv[1]
        dstDir = os.path.join(source_path,'aout2')#sys.argv[2]
        # len_to_end = #sys.argv[3]
        frameRate = 1  # int(sys.argv[3])
        # fTime = float(sys.argv[4])
        # set by hand :
        Fs = 16000
        chNum = 1
        sTime = 3 * 60  # sec
        eTime = time_total - 5*60  # sec
        print 3*60 ,time_total - 5*60

        pa, Name = os.path.split(srcWav)
        pureName, ext = os.path.splitext(Name)

        dstPicDir = os.path.join(dstDir, pureName + '-' + str(sTime) + '-' + str(eTime) + '-pic-dir-full')
        dstPicDir_cut = os.path.join(dstDir, pureName + '-' + str(sTime) + '-' + str(eTime) + 'pic-dir-cut')
        tarAudio = os.path.join(dstDir, pureName + '-' + str(sTime) + '-' + str(eTime) + '-1ch-16k.wav')

        if os.path.isdir(dstPicDir):
            removeALL(dstPicDir_cut)
        ffmpeg_get_audio(srcWav, tarAudio, Fs, chNum, sTime, eTime)
        ffmpeg_get_jpg(srcWav, dstPicDir, frameRate)

        # cut_batch(dstPicDir, dstPicDir_cut, len_to_end)

