# coding=utf8
'''
Created on 2017年6月12日

@author: Administrator
'''

# 类的方法
# 　　在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
# 私有的类方法
# 　　__private_method 两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用slef.__private_methods
class people:  
    #定义基本属性  
    name = ''  
    age = 0  
    #定义私有属性,私有属性在类外部无法直接进行访问  
    __weight = 0  
    #定义构造方法  
    def __init__(self,n,a,w):  
        self.name = n  
        self.age = a  
        self.__weight = w  
    def speak(self):  
        print("%s is speaking: I am %d years old" %(self.name,self.age))
        
# 二、继承类定义：
class student(people):  
    grade = ''  
    def __init__(self,n,a,w,g):  
        #调用父类的构函  
        people.__init__(self,n,a,w)  
        self.grade = g  
    #覆写父类的方法  
    def speak(self):  
        print("%s is speaking: I am %d years old,and I am in grade %d"%(self.name,self.age,self.grade))       
# 2.类的多重继承
#另一个类，多重继承之前的准备  
class speaker():  
    topic = ''  
    name = ''  
    def __init__(self,n,t):  
        self.name = n  
        self.topic = t  
    def speak(self):  
        print("I am %s,I am a speaker!My topic is %s"%(self.name,self.topic))  

#多重继承  
class sample(speaker,student):  
    a =''  
    def __init__(self,n,a,w,g,t):  
        student.__init__(self,n,a,w,g)  
        speaker.__init__(self,n,t)
        print 'init'

