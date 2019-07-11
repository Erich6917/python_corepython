# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 
# @Author  : ErichLee ErichLee@qq.com
# @File    : pic_find_location.py
# @Comment : 图片上标记位置，显示具体坐标
#            

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import cv2
import numpy as np


# img = cv2.imread(u"D:/yuan/movie/aout/a/HW之破晓之战-01_1frt-1.jpg")


## 读取图像，解决imread不能读取中文路径的问题
def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img


pic_path = u'D:/yuan/step1-pic-full/batch4-20190530/need/zhandiqiangwang/zhandiqiangwang-07-180-2363-pic-dir-full/zhandiqiangwang-07_1frt-21.jpg'
img = cv_imread(pic_path)


# print img.shape

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        print xy
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)


cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)

while (True):
    try:
        cv2.waitKey(100)
    except Exception:
        cv2.destroyWindow("image")
        break

cv2.waitKey(0)
cv2.destroyAllWindow()
