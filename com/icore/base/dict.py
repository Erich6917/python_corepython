# coding=-utf8
'''
Created on 2017年9月6日

@author: Administrator
'''
def println():
    print '=========================='
def test_dict():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print dict['Name']
    
    #遍历 k，v
    for k,v in dict.items():
        print k,v,',',
    println()
    
    for k in dict.keys() :
        print k,
    println()
    
    
    for ii in range(1,10):
        if ii == 2 :
            continue
        print ii,','
    
    
    
    
    
    
    

if __name__ =='__main__':
    test_dict()