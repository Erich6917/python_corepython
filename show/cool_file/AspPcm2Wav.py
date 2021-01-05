#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
@Descripttion: 音频降采样
                asp audio signal processing
@version: V1版本
@Author: lixf
@Date: 2019-11-15 9:46
@LastEditors: lixf
'''
import librosa
import matplotlib.pyplot as plt
import librosa.display
import os
import soundfile as sf
import wave

srcpath = r"D:\03工作\亚信\testdata\G00001"
tarpath = r"D:\工作\亚信\testdata\data_test1"
SmallWavNum = 0  # 短音频数目


def is_wav(f):
    res = True
    try:
        wave.open(f)
    except wave.Error as e:
        res = False
    return res
 
 
def pcm2wav(pcm_file, save_file, channels=1, bits=16, sample_rate=16000):
    """ pcm转换为wav格式
        Args:
            pcm_file pcm文件
            save_file 保存文件
            channels 通道数
            bits 量化位数，即每个采样点占用的比特数
            sample_rate 采样频率
    """
    if is_wav(pcm_file):
        raise ValueError('"' + str(pcm_file) + '"' +
                         " is a wav file, not pcm file! ")
 
    pcmf = open(pcm_file, 'rb')
    pcmdata = pcmf.read()
    pcmf.close()
 
    if bits % 8 != 0:
        raise ValueError("bits % 8 must == 0. now bits:" + str(bits))
 
    wavfile = wave.open(save_file, 'wb')
 
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
 
    wavfile.writeframes(pcmdata)


if __name__ == '__main__':
    #  获取文件总数目
    TotalFileNum = 0  # 音频文件总数目
    DoneFileNum = 0  # 已处理的音频文件数目
    for root, dirs, files in os.walk(srcpath.encode('utf-8').decode('utf-8')):  # 遍历音频
        for wavfile in files:  # 过滤pcm的音频
            if os.path.splitext(wavfile)[1] == '.pcm':
                TotalFileNum += 1

    TotalLen = 0
    SAMPLE = 8000
    for root, dirs, files in os.walk(srcpath.encode('utf-8').decode('utf-8')):
        for audiofile in files:
            if os.path.splitext(audiofile)[1] == '.pcm':  # 过滤pcm格式音频
                fullsrcfile = os.path.join(root, audiofile)  # 源音频全路径
                fulltarfile = fullsrcfile.replace('G00001', 'G00001_1').replace('.pcm', '.wav')
                if not os.path.exists(os.path.split(fulltarfile)[0]):
                    os.makedirs(os.path.split(fulltarfile)[0])
                pcm2wav(fullsrcfile, fulltarfile)  # 音频降采样
                DoneFileNum += 1
                print("~~~~~~total file num: %d, done file num: %d" % (TotalFileNum, DoneFileNum))