# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 
# @Author  : LIYUAN134
# @File    : argparse.py
# @Commment: 
#
import argparse


def argdemo1():
    parser = argparse.ArgumentParser(description='Short sampleapp')

    parser.add_argument('-a', action="store_true", default=False)

    parser.add_argument('-b', action="store", dest="b")

    parser.add_argument('-c', action="store", dest="c", type=int)

    print parser.parse_args(['-a', '-bval', '-c', '3'])


def argdemo2():
    parser = argparse.ArgumentParser(
        description='Examplewith long option names',
    )

    parser.add_argument('--noarg', action="store_true",
                        default=False)

    parser.add_argument('--witharg', action="store",
                        dest="witharg")

    parser.add_argument('--witharg2', action="store",
                        dest="witharg2", type=int)

    print parser.parse_args(
        ['--noarg', '--witharg', 'val', '--witharg2=3']
    )


if __name__ == '__main__':
    argdemo2()
