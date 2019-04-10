# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 
# @Author  : ErichLee ErichLee@qq.com
# @File    : pic_mv_cut.py
# @Comment : 
#            

import sys
import os

from PIL import Image

reload(sys)
sys.setdefaultencoding('utf-8')


def get_all_jpg(path_source='.'):
    file_list = []
    for root, dirs, files in os.walk(path_source):
        for filename in files:
            if filename.endswith(".jpg"):
                file_msg = filename, os.path.join(root, filename), root
                file_list.append(file_msg)
    return file_list


def pic_cut(input, output, size=60):
    img = Image.open(input)
    llen, hig = img.size
    l_end = hig - size
    l_left = 0 + 50
    l_right = llen - 200
    l_top = l_end - 50
    box = (l_left, l_top, l_right, l_end)
    # print llen, hig, l_left, l_top, l_right, l_end
    cropped = img.crop(box)  # (left, upper, right, lower)
    cropped.save(output)


dict_type = {
    u'HW之破晓之战': 40,
    u'HW之千里同风': 40,
    u'R间规则第二季': 30,
    u'S空侠': 85,
    u'WD恶魔少爷': 25,
    u'WJ徒弟又挂了': 36,
    u'WY你的光年距离2': 14,
    u'W的保姆手册': 50,
    u'发酵吧，创业菌': 55,
    u'决币': 55,
    u'区小队': 70,
    u'外滩钟声': 45,
    u'因为爱你': 15,
}


def start():
    content_list = [u'决币', u'区小队', u'外滩钟声', u'因为爱你']

    for content in content_list:
        print 'start', content
        source_path = u'D:/yuan/aout/ap2/{}'.format(content)
        file_list = get_all_jpg(source_path)
        for each in file_list:
            jpg_name, jpg_path, jpg_root = each[0], each[1], each[2]
            # print jpg_name, jpg_path
            output_path = jpg_root.replace(u'/aout', u'/Acut-temp').replace(u'\\', u'/')
            if not os.path.exists(output_path):
                print '创建目标文件,', output_path
                os.makedirs(output_path)

            # print os.path.join(output_path, jpg_name)
            jpg_output = os.path.join(output_path, jpg_name)
            pic_cut(jpg_path, jpg_output, dict_type.get(content))

            # print jpg_output


start()
