# coding=-utf8
'''
Created on 2017年9月6日

@author: Administrator
'''
def func_getmsg():
    a = 1
    b = '33'
    return a,b
def func_getlist():
    a = [1,3,4,5,6]
    b = 4
    return a,b
def test_getmsg():
    a,b = func_getmsg()
    print a
    print b
    
    la,lb = func_getlist()
    print la
    print lb
    

if __name__ =='__main__':
    test_getmsg()