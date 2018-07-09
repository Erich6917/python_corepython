# coding=utf8

# Created on 2017年6月12日
#
# @author: Administrator


# 类的方法
# 　　在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
# 私有的类方法
# 　　__private_method 两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用slef.__private_methods
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s is speaking: I am %d years old" % (self.name, self.age))


# 二、继承类定义：
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g
        # 覆写父类的方法

    def speak(self):
        print("%s is speaking: I am %d years old,and I am in grade %d" % (self.name, self.age, self.grade))

        # 2.类的多重继承


# 另一个类，多重继承之前的准备
class Speaker(object):
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("I am %s,I am a speaker!My topic is %s" % (self.name, self.topic))

        # 多重继承


class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)
        print 'init'


# 类的属性
# dir()返回的仅是对象的属性的一个名字列表
print dir(People)
# __dict__返回的是一个字典，
# 它的键(keys)是属性名，键值(values)是相应的属性对象的数据值。
print People.__dict__

# >>> class C(object): # define class 定义类
# ... version = 1.2 # static member 静态成员
# >>> c = C() # instantiation 实例化
#
# >>> C.version # access via class 通过类来访问
# >>> c.version # access via instance 通过实例来访问
# >>> C.version += 0.1 # update (only) via class 通过类（只能这样）来更新
# >>> C.version # class access 类访问
#
# >>> c.version # instance access, which 实例访问它，其值已被改变
