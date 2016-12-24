# coding: utf-8
#def tishi():
 #   a = int(raw_input('Enter number between 0-100: '))
#    if 0<=a<=100:
 #       print 'success!'
#    else:
#        tishi()

#tishi()


a = int(raw_input('请输入0-100之间的整数: '))
while a<0 or a>100:
    a = int(raw_input('输出错误，请重新输入: '))
print '成功！'