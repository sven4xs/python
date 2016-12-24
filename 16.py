#coding:utf-8
import os
while True:
    fname = raw_input('请输入文件名： ')
    if os.path.exists(fname):
        break
    else:
        print '打开文件错误，没有此文件'
mask=open(fname,'r')
for i in  mask:
    print i,
mask.close()