#coding: utf-8
import os
ls=os.linesep
fileappend=open('E:/python/ex01/01.txt','a')
fileappend.write('追加内容: '+ls)  #不用\n　如果使用os.linesep
fileappend.write('\n')
while True:
    aline=raw_input("请输入(点击'.'退出):")
    if aline != ".":
       fileappend.write('%s%s' % (aline,ls))
    else:
        break
fileappend.close()