# coding=-utf8
'''
Created on 2017年9月6日

@author: Administrator
'''


def println():
    print '=========================='


def test_dict():
    dicts = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print dicts['Name']

    # 遍历 k，v
    for k, v in dicts.items():
        print k, v, ',',
    println()

    for k in dicts.keys():
        print k,
    println()

    for ii in range(1, 10):
        if ii == 2:
            continue
        print ii, ','


def list_loop():
    ilist = ['html', 'js', 'css', 'python']

    # 方法1
    print '遍历列表方法1：'
    for i in ilist:
        print ("序号：%s   值：%s" % (ilist.index(i) + 1, i))

    print '\n遍历列表方法2：'
    # 方法2
    for i in range(len(ilist)):
        print ("序号：%s   值：%s" % (i + 1, ilist[i]))

    # 方法3
    print '\n遍历列表方法3：'
    for i, val in enumerate(ilist):
        print ("序号：%s   值：%s" % (i + 1, val))

    # 方法3
    print '\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：'
    for i, val in enumerate(ilist, 2):
        print ("序号：%s   值：%s" % (i + 1, val))


print 'hello'

if __name__ == '__main__':
    test_dict()
