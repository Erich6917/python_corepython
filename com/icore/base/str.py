# -*- coding: utf-8 -*-
# @Time    : 2017/9/20
# @Author  : LIYUAN134
# @File    : jsontest.py
# @Commment:
#
import time
import types
import re
import os
from calendar import month_abbr
from loggerUtil import infos, printLine


def demo_join():
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print ' '.join(parts)
    print ''.join(parts)
    infos('如果只是连个字符串简单的拼接可不用+')
    print 'Hello' 'World'

    data = ['ACME', 50, 91.1]
    print ','.join(str(d) for d in data)
    print '==========================='
    # data = ['ACME', 50, 91.1]
    # s = ','
    # for d in data:
    #     print str(d)
    #     s = s.join(str(d))
    #     print '>',s
    # # print s
    a, b, c = 'B', 'T', 'S'
    print(a + ':' + b + ':' + c)  # Ugly
    print(':'.join([a, b, c]))  # Still ugly
    # print(a, b, c, sep=':')  # Better
    printLine()


def demo_sub():
    str = '0123456789'
    print str[0:3]  # 截取第一位到第三位的字符
    print str[:]  # 截取字符串的全部字符
    print str[6:]  # 截取第七个字符到结尾
    print str[:-3]  # 截取从头开始到倒数第三个字符之前
    print str[2]  # 截取第三个字符
    print str[-1]  # 截取倒数第一个字符
    print str[::-1]  # 创造一个与原字符串顺序相反的字符串
    print str[-3:-1]  # 截取倒数第三位与倒数第一位之前的字符
    print str[-3:]  # 截取倒数第三位到结尾
    print str[:-5:-3]  # 逆序截取，具体啥意思没搞明白？


# print demo_sub()

# 字符串连接
def demo_strjoin():
    # 方法1：直接通过加号(+)操作符连接,效率低下
    # 因为python中字符串是不可变的类型，使用 + 连接两个字符串时会生成一个新的字符串，生成新的字符串就需要重新申请内存，
    # 当连续相加的字符串很多时(a + b + c + d + e + f + ...) ，效率低下就是必然的了
    myEmail = 'liyuan134' + '@pingan' + '.com' + '.cn'
    print myEmail


# β 字符串拆分，可以根据字符串切分，即调用string本身API，或者根据正则切分，即调用re.split
def demo_split():
    msg = 'liyuan134|@pignan|com|cn'
    rt = msg.split("|")
    print rt


def demo_split2():
    # 未使用捕获组
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    print re.split(r'[;,\s]\s*', line)

    # 使用捕获组
    # 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
    rt = re.split(r'([;j,j\s])\s*', line)
    # for each in rt:
    #     print each, '>',
    alues = rt[::2]
    delimiters = rt[1::2] + ['']
    print alues
    print delimiters

    # 使用非捕获组,
    # 你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表达式的
    rt = re.split(r'([;j,j\s])\s*', line)
    for each in rt:
        print each, '>',


# 检查字符串的开头或者结尾
def demo_start_end():
    filename = 'spam.txt'
    filename.endswith('.txt')
    filename.startswith('file:')
    dirs = os.listdir('.')
    for each in dirs:
        if each.endswith('.py'):
            print 'HA', each
        else:
            print 'ELSE', each
    infos('使用正则表达式匹配')

    url = 'http://www.python.org'
    rt = re.match('http:jhttps:jftp:', url)
    print rt


def demo_find():
    text = 'yeah, but no, but yeah, but no, but yeah'
    print text.find('no')

    infos('正则匹配查询')
    text1 = '11/27/2012'
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text1):
        infos('yes')
    else:
        infos('no')

    infos('findall 方法：')
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print datepat.findall(text)


def _change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    # 年份通过计算加1
    return '{} {} {}'.format(m.group(2), mon_name, int(m.group(3)) + 1)


def demo_replace():
    # 对于简单的字面模式，直接使用str.repalce() 方法即可
    text = 'yeah, but no, but yeah, but no, but yeah'
    infos(text.replace('yeah', 'yep'))

    # 对于复杂的模式，请使用re 模块中的sub() 函数

    # 可以拿到捕获组具体的内容，\1 \2 \3  但是不能计算
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    rt = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print rt

    # 如果想计算的话，可以通过回调函数如下
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    rt = datepat.sub(_change_date, text)
    infos(rt)


def demo_replace_upper_lower():
    # 为了在文本操作时忽略大小写，你需要在使用re 模块的时候给这些操作提供
    # re.IGNORECASE 标志参数
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print re.findall('python', text, flags=re.IGNORECASE)

    print re.sub('python', 'snake', text, flags=re.IGNORECASE)


def demo_match_most_short():
    text2 = 'Computer says "no." Phone says "yes."'
    str_pat = re.compile(r'\"(.*?)\"')
    rt = str_pat.findall(text2)
    if rt:
        for single in rt:
            print single
    else:
        print 'NOT MATCH'


def demo_clean():
    s = ' hello world \n'
    print s.strip()
    print s.lstrip()
    print s.rstrip()

    t = '-----hello====='
    print t.lstrip('-')
    print t.strip('-=')

    # with open(filename) as f:
    #     lines = (line.strip() for line in f)
    # for line in lines:
    #     print(line)


def demo_just():
    text = 'Hello World'
    print '[' + text.ljust(20) + ']'
    print '[' + text.rjust(20) + ']'
    print '[' + text.center(20) + ']'
    print '[' + text.rjust(20, '=') + ']'
    print '[' + text.center(20, '*') + ']'

    # 函数format() 同样可以用来很容易的对齐字符串。你要做的就是使用<,>
    # 或者字符后面紧跟一个指定的宽
    print '[' + format(text, '>20') + ']'
    print '[' + format(text, '<20') + ']'
    print '[' + format(text, '^20') + ']'

    infos('如果你想指定一个非空格的填充字符，将它写到对齐字符的前面即可')
    print format(text, '=>20s')
    print format(text, '*^20s')

    infos('当格式化多个值的时候，这些格式代码也可以被用在format() 方法中')
    print '{:>10s} {:>10s}'.format('Hello', 'World')

    infos('format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使得它非常的通用')
    x = 1.2345
    print format(x, '>10')
    print format(x, '^10.2f')


def demo_format():
    # 创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。

    # 通过使用字符串的format() 方法来解决这个问题
    s = '{name} has {n} messages.'
    print s.format(name='Guido', n=37)

    # name = 'Guido'
    # n = 37
    # print s.format_map(vars())

    # name = 'Guido'
    # n = 37
    # print '%(name) has %(n) messages.' % vars()

def demo_format2():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

    import textwrap
    # print(textwrap.fill(s, 70))
    # print(textwrap.fill(s, 40))
    print(textwrap.fill(s, 40, initial_indent='^^^^^^^^^^'))
    printLine()
    print(textwrap.fill(s, 40, subsequent_indent='^^^^^^^^^^'))
    printLine()

demo_format2()


def demo_type():
    msg = '123'
    arr = []
    arr.append(msg)
    # print type(msg)
    # print type(arr)
    # print types(msg)
    print isinstance(msg, str)
    print isinstance(arr, list)
