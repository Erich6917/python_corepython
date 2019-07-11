# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 
# @Author  : ErichLee ErichLee@qq.com
# @File    : zip_each.py
# @Comment : 
#            

import sys
import util.file_check_util as file_util
import zipfile
import os

reload(sys)
sys.setdefaultencoding('utf-8')


# 目录下每一个文件单独压缩成一个文件

def zip_each_file(source_path):
    file_list = file_util.get_all_files_path_name(source_path)
    out_dir = os.path.join(source_path, 'out')
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    for file_name, file_path, file_root in file_list:
        # print file_name, file_path, file_root

        out_name = file_name.replace('.wav', '.zip')
        out_path = os.path.join(out_dir, out_name)

        print out_name, out_path, file_name
        zip = zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED)
        zip.write(file_path, file_name)
        zip.close()


# path = u'E:/clean-fayuan/Batch5-20190628/wav_source/output/output/output'
# path = u'E:/video/qiangqiangsanrenxing2017/video_source/output/output'
# zip_each_file(path)
