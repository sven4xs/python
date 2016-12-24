#coding:utf-8
import os
ls=os.linesep
fname = raw_input('请创建文件： ')
a=[]
try:
    mask=open(fname,'r')
    if mask:
        print '该文件已存在'
except IOError,e:
    print '系统自动帮您创建文件%s' % fname
    mask = open(fname, 'w')
    while True:
        entry=raw_input("input everything you want(click '.' to quit): \n>")
        if entry =='.':
            break
        else:
            a.append(entry)

    mask.writelines(['%s%s' % (x,ls)for x in a])
    mask.close()
    print '成功写入'