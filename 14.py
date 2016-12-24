#coding: utf-8
fname=raw_input('请输入文件名： ')
print
try:
    mask=open(fname,'r')
except IOError,e:
    print '文件打开错误'
else:
    for i in mask:
        print i.strip('\n')
    mask.close()




