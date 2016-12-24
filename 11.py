#coding: utf-8
print '请选择以下功能：\nx(退出)\n1（求和）\n2(求平均数)'
a=10
b=2
one = raw_input('请输入编号:')
while one !='x':
    if one.isdigit() and int(one) == 1:  #.isdigit()是判别输入的字符串是否是数值
        print '求%d和%d和为：%d' % (a,b,a+b)
        one = raw_input('请选择')

    elif one.isdigit() and int(one) == 2:
        print  '求%d和%d的平均数为：%.1f' % (a,b,(a+b)/2)
        one = raw_input('请选择')
    else:
        print '请重新输入：\nx(退出)\n1（求和）\n2(求平均数)'
        one = raw_input()
print '成功退出'
raw_input()