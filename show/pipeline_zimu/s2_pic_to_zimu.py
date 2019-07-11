# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 
# @Author  : ErichLee ErichLee@qq.com
# @File    : pic_mv_cut.py
# @Comment : 图片在确定坐标之后，截取图片中字幕的部分
#            

import sys
import os

from PIL import Image
import util.file_check_util as file_util

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
    l_right = llen - 100
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
    'bu-zhe': 45,
    'dui-de-shi-jian-dui-de-ren-di-er-ji': 25,
    'fei-nan-qiu': 42,
    'gu-men-di-yi-ji': 20,
    'huang-tu-gao-tian': 45,
    'jiang-hu-zhi-gui-mian-yi-yun': 20,
    'jiao-shi-de-na-yi-jian': 20,
    'jing-zhe': 45,
    'jue-mi-ren-wu': 15,

    'ni-qing-chun-di-yi-ji': 45,
    'nv-shen': 12,
    'peng-pai': 20,
    'si-jie-mei': 50,
    'wei-qing-chun-dian-zan': 58,
    'wen-fang-si-bao': 20,
    'wo-de-ai-dui-ni-shuo': 40,
    'wo-men-de-si-shi-nian': 50,
    'xiao-xin-wo-yao-fang-da-zhao-le': 20,
    'xing-fu-yi-jia-ren': 45,
    'yang-guang-de-kuai-le-sheng-huo-zhi-shen-shi-pin-ge': 25,
    'yao-de-jin-se-cheng-bao': 10,
    'yong-yuan-yi-jia-ren': 45,
    'yu-xie-shi-si-nian': 25,
    'Aqingjinhualun': 24,
    'bangbangdexingfushenghuo': 45,
    'diexiechangjiang': 20,
    'Jhuyedian': 86,
    'NMshuyuwodexingguang': 7,
    'Frenyuan': 40,
    'Qshideshoutao':50,
    'womenkebukeyibuyoushang':45,
    'xiarixintiao':50,
    'xinshengshuihupan':46,
    'yiwenbudingqing':50,
    'zhandiqiangwang':25,

}


def start():
    content_list = [ 'Frenyuan','Qshideshoutao',
    'womenkebukeyibuyoushang',
    'xiarixintiao',
    'xinshengshuihupan',
    'yiwenbudingqing',
    'zhandiqiangwang',
                  ]

    for content in content_list:
        print 'start', content
        root_path = u'D:/yuan/step1-pic-full/batch4-20190530/need'
        root_output = os.path.join(root_path, u'output')
        source_path = os.path.join(root_path, content)
        file_list = get_all_jpg(source_path)
        for each in file_list:
            jpg_name, jpg_path, jpg_root = each[0], each[1], each[2]
            # print jpg_name, jpg_path
            output_path = jpg_root.replace(root_path, root_output).replace(u'\\', u'/')
            if not os.path.exists(output_path):
                print '创建目标文件,', output_path
                os.makedirs(output_path)

            # print os.path.join(output_path, jpg_name)
            jpg_output = os.path.join(output_path, jpg_name)
            pic_cut(jpg_path, jpg_output, dict_type.get(content))

            # print jpg_output


start()
