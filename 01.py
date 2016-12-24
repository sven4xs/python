try:
    filename = raw_input('Enter file name: ')
    fobj = open(filename, 'r')
    for i in fobj:
        print i,
    fobj.close()
except IOError, e:
    print 'file open erroe:', e