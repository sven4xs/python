#coding:utf-8
import os
ls=os.linesep
while True:
    print '1、创建一个文本文件\n2、显示一个文本文件\n3、退出 '
    str = raw_input('请选择：  ')
    if str == '1':
        while True:
            fname = raw_input('请给文件命名： ')
            if os.path.exists(fname):
                print '该文件名已存在'
            else:
                break
        a = []
        while True:
            entry = raw_input("input everything you want(click '.' to quit): ")
            if entry == '.':
                break
            else:
                a.append(entry)
        mask = open(fname, 'w')
        mask.writelines(['%s%s' % (x, ls) for x in a])
        mask.close()
        print '成功写入'
    elif str == '2':
        fname = raw_input('请输入文件名： ')
        print
        try:
            mask = open(fname, 'r')
        except IOError, e:
            print '文件打开错误'
        else:
            for i in mask:
                print i.strip('\n')
            mask.close()
    elif str ==' 3':
        break
    else:
        print '您选择的功能有误！'

