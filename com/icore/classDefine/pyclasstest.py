# coding=utf8
'''
Created on 2017年6月12日

@author: Administrator
'''
from pyclass import  *
def d_people():
    p = people('liyuan',23,70)  
    p.speak()
    

def d_student():    
    s = student('ken',20,60,3)  
    s.speak()

def d_sample():
    test = sample("Tim",25,80,4,"Python")  
    test.speak()#方法名同，默认调用的是在括号中排前地父类的方法
    
d_sample()