#coding:utf-8
import os
ls = os.linesep
def writer():
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
def read():
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
def main():
    while True:
        print '1、创建并写入文件'
        print '2、显示文件'
        print '3、退出！'
        abc=raw_input('请选择功能： ')
        if abc == '1':
            writer()
        elif abc=='2':
            read()
        elif abc=='3':
            break
        else:
            print '输入错误'
if __name__=='__main__':
    main()
