# coding=utf8
'''
Created on 2017年6月12日

@author: Administrator
'''
def listLoop():
    list1 = ['physics', 'chemistry', 1997, 2000];
    print 'loop method 1 :'
    for single in list1:
        print "{",list1.index(single),":",single,"}",
    print
    print 'loop method 2 :'    
    for ii in range(len(list1)):
        print "{",ii,":",list1[ii],"}",
    print
    print 'loop method 3'
    
    for i,val in enumerate(list1):
        print "{",i,":",val,"}",
def listApi1():    
    list1 = [1,2,3]
    list2 = {5,6,7}
    arr2 = []
    
    
    list1.append(3)
    list1.extend(list2)
    print list1
    print max(list1)
    print min(list1)
    print list1.count(3)
    
    list1.insert(1, 33)
    list1.remove(3)
    list1.sort()
    
    print list1
    
    
    
listApi1()