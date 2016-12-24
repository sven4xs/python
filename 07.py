#coding:utf-8
a=[1,2,3,4,56]
i=0
sum=0
while i<len(a):
    sum=sum+a[i]
    i+=1
print '你的sum=%d' % sum
average=float(sum)/5
print 'average=%f' % average
raw_input()