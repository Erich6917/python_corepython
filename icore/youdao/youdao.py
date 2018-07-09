# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 
# @Author  : ErichLee ErichLee@qq.com
# @File    : youdao.py
# @Comment : 
#            

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import httplib
import md5
import urllib
import urllib2
import random
import json
import base64
import os

appKey = '6638e682b402e927'
secretKey = '5pWM3lThVXHaXq7XxmZHqrEmtOQcxx83'
httpClient = None

try:
    filepath = 'source'
    for root, dirs, files in os.walk(filepath):
        for filename in files:
            tpath = filepath + '/' + filename
            print tpath

            f = open(tpath, 'rb')  # 二进制方式打开图文件 需要用户在d:\1.png 放这个图片并且里面得有文字
            img = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
            f.close()

            detectType = '10011'
            imageType = '1'
            langType = 'zh-en'  # en
            salt = random.randint(1, 65536)

            sign = appKey + img + str(salt) + secretKey
            m1 = md5.new()
            m1.update(sign)
            sign = m1.hexdigest()
            data = {'appKey': appKey,
                    'img': img,
                    'detectType': detectType,
                    'imageType': imageType,
                    'langType': langType,
                    'salt': str(salt),
                    'sign': sign,
                    'docType': 'json'}
            data = urllib.urlencode(data)
            req = urllib2.Request('http://openapi.youdao.com/ocrapi', data)

            # response是HTTPResponse对象
            response = urllib2.urlopen(req)
            readJson = response.read()
            rtjson = json.loads(readJson)
            if rtjson:
                # print rtjson
                regions = rtjson.get("Result").get("regions")
                if regions:
                    # print "regions>", regions
                    for each in regions:
                        linelist = each.get("lines")
                        # print "lines>", linelist
                        for line in linelist:
                            wordlist = line.get('words')
                            print '   ',
                            for word in wordlist:
                                print word.get('text'),
                            print
                    pass
                else:
                    print "   未识别到结果"

                    # print unicode(readJson, "utf-8")
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
