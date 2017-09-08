'''
Created on 2017年9月6日

@author: Administrator
'''
import time

def demo_join():
    MAX = 9000000  
    char_list = [ chr((i % 26) +97)  for i in xrange(MAX) ]  
      
    my_str=''  
    last_time = time.time()  
    for i in char_list:  
        my_str = my_str + i  
    print time.time() - last_time  
    print '-' * 80  

    my_str=''  
    t_list=[]  
    last_time = time.time()
    for i in char_list:  
        t_list.append(i)  
    my_str = ''.join(t_list)  
    print time.time() - last_time  
    print '-' * 80  

def demo_sub():
    str = '0123456789'
    print str[0:3] #截取第一位到第三位的字符
    print str[:] #截取字符串的全部字符
    print str[6:] #截取第七个字符到结尾
    print str[:-3] #截取从头开始到倒数第三个字符之前
    print str[2] #截取第三个字符
    print str[-1] #截取倒数第一个字符
    print str[::-1] #创造一个与原字符串顺序相反的字符串
    print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
    print str[-3:] #截取倒数第三位到结尾
    print str[:-5:-3] #逆序截取，具体啥意思没搞明白？