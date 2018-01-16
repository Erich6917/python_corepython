# -*- coding: utf-8 -*-
# @Time    : 2018/1/11
# @Author  : LIYUAN134
# @File    : num.py
# @Commment: python集中集合类型
#            List 元组 字典
#
import heapq


def println():
    print '=========================='


def dict_loop():
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


def dict_mulkeys():
    from collections import defaultdict
    d = {
        'a': [1, 2, 3],
        'b': [4, 5]
    }
    e = {
        'a': {1, 2, 3},
        'b': {4, 5}
    }
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    print d

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)


def dict_sort():
    prices = {
        'ACME': 45.23,
        'AAPL': 61.78,
        'IBM': 205.55,
        'HPQ': 376.20,
        'FB': 10.75
    }
    print min(prices.values())
    # 为了对字典值执行计算操作，通常需要使用zip() 函数先将键和值反转过来。比
    # 如，下面是查找最小和最大股票价格和股票值的代码：
    print min(zip(prices.values(), prices.keys()))
    print min(zip(prices.keys(), prices.values()))
    # '类似的，可以使用zip() 和sorted() 函数来排列字典数据：'
    print sorted(zip(prices.values(), prices.keys()))
    println()
    # 可以在min() 和max() 函数中提供key 函数参数来获取最小值或最大值对应的键的信息
    print min(prices, key=lambda k: prices[k])
    # 但是，如果还想要得到最小值，你又得执行一次查找操作。比如：
    min_value = prices[min(prices, key=lambda k: prices[k])]
    print min_value


def dict_cal():
    # 计算
    a = {'x': 1,
         'y': 2,
         'z': 3
         }
    b = {'w': 10,
         'x': 11,
         'y': 2
         }
    a.keys() & b.keys()
    # print a.keys() & b.keys()


def dict_remove_duplicates():
    print 'aa'
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    item_set = set()
    for each in a:
        item_set.add(each)
    for each in a:
        if each not in item_set:
            # yield each
            item_set.add(each)
    print item_set
    print list(item_set)


def dict_same():
    prices = {
        'ACME': 45.23,
        'ACME': 61.78,
        'IBM': 205.55,
        'HPQ': 376.20,
        'FB': 10.75
    }
    print set(prices)
    print list(set(prices))
    # print dict(set(prices))


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


def rang_demo():
    for ii in range(1, 5):
        print ii
    for ii in range(5, 11):
        print ii


def list_update():
    list = ['physics', 'chemistry', 1997, 2000];
    print 'old', list[2]
    list[2] = 'changes'
    print 'update>', list[2]

    # 可以直接删除某一个元素
    println()

    print 'length:', len(list)
    print '组合 ', [1, 2, 3] + [4, 5, 6]
    print '重复 ', ['hi!'] * 4
    print 'in ,not in ', (3 in [1, 2, 3])
    


list_update()


def list_sub():
    arr = []
    for ii in range(1, 10):
        arr.append(ii)
    print arr[5:]
    print arr[:5]
    print arr[:100]
    print arr[100:]


def list_distinct():
    url_list = []
    url_list.append('11')
    url_list.append('22')
    url_list.append('22')
    url_list.append('33')
    print len(url_list)
    url_list = list(set(url_list))
    for ss in url_list:
        print ss


def list_find_max():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]


def list_find_entity_max():
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(8, portfolio, key=lambda s: s['price'])
    print cheap
    print len(expensive)
    print expensive

# if __name__ == '__main__':
#     # list_find_max()
#     list_find_entity_max()
