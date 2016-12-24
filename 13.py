#coding: utf-8
import os
ls=os.linesep
while True:
    fname=raw_input('请给文件命名： ')
    if os.path.exists(fname):
        print '该文件名已存在'
    else:
        break
a=[]
while True:
    entry=raw_input("input everything you want(click '.' to quit): ")
    if entry =='.':
        break
    else:
        a.append(entry)
mask=open(fname,'w')
mask.writelines(['%s%s' % (x,ls)for x in a])
mask.close()
print '成功写入'


