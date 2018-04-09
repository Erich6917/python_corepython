#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import xlrd


def paraseExcel():
    # 文件位置
    excelFile = xlrd.open_workbook('1.xlsx')
    sheet = excelFile.sheet_by_index(0)
    nrows = sheet.nrows
    total = 0

    skey = ''
    t1, t2, t3 = (0, 0, 0)
    for i in range(1, nrows):
        if total > 100:
            return
        total += 1
        print total,
        name, v1, v2, v3 = sheet.cell(i, 0).value, \
                           sheet.cell(i, 5).value, \
                           sheet.cell(i, 10).value, \
                           sheet.cell(i, 11).value
        if skey is None or skey == '':
            skey = name
            t1, t2, t3 = v1, v2, v3
            print 'init First type and write excel detail', name, v1, v2, v3
        else:
            if name == skey:
                t1, t2, t3 = t1 + v1, t2 + v2, t3 + v3
                print 'write excel detail', name, v1, v2, v3
            else:
                print 'write excel Total Finish the type', name, t1, t2, t3
                skey = name
                t1, t2, t3 = v1, v2, v3
                print 'init new type and write excel detail', name, v1, v2, v3


if __name__ == '__main__':
    paraseExcel()
