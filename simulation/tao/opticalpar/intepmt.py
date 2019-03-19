#!/usr/bin/env python
# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
import pylab as pl

f = open('/media/tao/_dde_data/arlierwork/simulation/tao/opticalpar/PMTxp3232.txt')
s = f.readline()
a1=[]
a2=[]
count=0
#print(s)
while (count<144):
     arr=s.split(' ')
#     print arr
#     print arr[1]
     a1.append(float(arr[0]))
     a2.append(float(arr[1].replace('\r\n',''))) #readline 读取文件的时候，默认加上“\n"
#     a2=arr[1].replace('\n','') #readline 读取文件的时候，默认加上“\n"
     s=f.readline()
     count+=1

#print(a1)
#print(a2)
#x=np.linspace(0,10,11)
#x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
x=np.array(a1)
#y=np.sin(x)
y=np.array(a2)
#print(x)
#xnew=np.linspace(0,10,101)
xnew=np.linspace(300,600,301)


pl.figure(figsize=(8,8))
#axes = pl.plot(111)
fig=pl.plot(x,y,"o",label='the original data',c=(0,0.0,0.0),alpha=0.5)
pl.suptitle('PDE wavelength response  and interpolation')
#pl.plot(x,y,"ro",label='the original data',c=(1,0.2,0.5),alpha=0.5)
pl.style.use('ggplot')
#pl.grid(axis='x')
pl.grid(True)
#pl.grid(color='g',linewidth=2,alpha=0.2,ls='--',lw=1)
#pl.axis([350,550,0,1])
pl.xlabel('wave length [nm]',color='k',fontsize=15,rotation=0) 
pl.ylabel('PDE of PMT xp3232[A.U]',color='k',fontsize=15,rotation=90) 
#pl.xticks([420,440,460,480],['420','440','490','480']) 
for kind in ["nearest"]:#插值方式
#for kind in ["nearest","zero","slinear","quadratic","cubic"]:#插值方式
    #"nearest","zero"为阶梯插值
    #slinear 线性插值
    #"quadratic","cubic" 为2阶、3阶B样条曲线插值
    f=interpolate.interp1d(x,y,kind=kind)
    # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    ynew=f(xnew)
    pl.plot(xnew,ynew,label=str(kind)+ ' interpolated data',color='g',markersize=.31)
print(xnew,ynew)
pl.legend(loc="upper right")
pl.savefig("pmttest.eps")
pf = open("pmtout.txt","w")
i=1
while i<=len(xnew):
    print >> pf, "%3d %0.5f" % (xnew[i-1], ynew[i-1])
    i += 1
pf.close()



pl.show()