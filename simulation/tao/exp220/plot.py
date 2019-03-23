#!/usr/bin/env python
# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
import pylab as pl

f = open('/media/tao/_dde_data/arlierwork/simulation/tao/exp220/example.lvm') #换成你自己的文件名
s = f.readline()
a1=[]
a2=[]
nevent=1
rec_length=2002   #2002ns 是取数时的采样长度。
count=0
eventnum=0
while (count<rec_length*nevent):  
     arr=s.split(' ')
#     print arr
     a1.append(float(arr[0]))
     a2.append(count)
     s=f.readline()
     count+=1
#print(a1)
#print(a2)
#x=np.linspace(0,10,11)
#x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
x=np.array(a1)
y=np.array(a2)
#print(x)


pl.figure(figsize=(8,8))
#axes = pl.plot(111)
fig=pl.plot(y,x,"r.",label='the waveform ',c=(0,0.0,0.0),alpha=0.5,linestyle='-')
pl.suptitle('example waveform')
#pl.plot(x,y,"ro",label='the original data',c=(1,0.2,0.5),alpha=0.5)
pl.style.use('ggplot')
#pl.grid(axis='x')
pl.grid(True)
pl.grid(color='g',linewidth=2,alpha=0.2,ls='--',lw=1)
#pl.axis([350,550,0,1])
pl.xlabel('time  [ns]',color='k',fontsize=15,rotation=0) 
pl.ylabel('voltage [mV]',color='k',fontsize=15,rotation=90) 
pl.legend(loc="upper right")
pl.savefig("wave.eps")
pl.show()
