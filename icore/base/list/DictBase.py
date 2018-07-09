# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 
# @Author  : ErichLee ErichLee@qq.com
# @File    : DictBase.py
# @Commment: 
#            

import sys
from loggerUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')

dtypes = {
    's1': '在业',
    's2': '存续',
    's3': '吊销',
    's4': '注销',
    's5': '迁出',
}


def dict_demo1():
    ljinfos("get( x [ , y]) 返回字典 d 中键 x 对应的值，键 x 不存在的时候返回 y， y 的默认值为None")
    infos(dtypes.get('s1', 's2'))

    ljinfos("items() key value遍历")
    ljinfos("keys() ")
    ljinfos("values()")
    for key, val in dtypes.items():
        infos('  key > ', key, ' val > ', val)

    ljinfos("pop( x[, default]) ) 返回给定键 x 对应的值 如果x不在字典d，则返回default；"
            "若x既不在d中，同时default未设置，则引起KeyError类型错误")
    infos(' pop >', dtypes.pop('s1'))
    infos(' 剩余字典 KEY', dtypes.keys())

    ljinfos("update( x ) 将字典 x 所有键值对添加到字典 d 中（不重复，重复的键值对用字典 x 中的键值对替代字典 d 中）")
    dic_cp = {}
    dic_cp.update(dtypes)
    print ' update > ', dic_cp.keys()

    ljinfos("clear 清空字典 ")
    dtypes.clear()
    infos(dtypes)

    


dict_demo1()
