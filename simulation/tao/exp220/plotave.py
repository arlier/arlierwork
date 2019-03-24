#!/usr/bin/env python
# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
import pylab as pl
f = open('/media/tao/_dde_data/arlierwork/simulation/tao/exp220/example.lvm')#换成你自己的文件名
s = f.readline()
a1=[]
nevent=580
rec_length=1999   #2002ns 是取数时的采样长度。
count=0
eventnum=0
time=0
avewave=np.zeros( rec_length )
while (count<rec_length*nevent):  
     arr=s.split(' ')
     a1.append(float(arr[0]))
     s=f.readline()
     avewave[time]+=float(arr[0])/nevent
     time+=1
     if(count%rec_length==0):
         eventum=eventnum+1
         time=0
     count+=1
x=np.array(a1)
y=np.linspace(1,rec_length,rec_length)
pl.figure(figsize=(8,8))
fig=pl.plot(y,avewave,"r.",label='the average waveform ',c=(0,0.0,0.0),alpha=0.5,linestyle='-')
pl.suptitle('example average waveform')
pl.style.use('ggplot')
pl.grid(True)
pl.grid(color='g',linewidth=2,alpha=0.2,ls='--',lw=1)
pl.xlabel('time  [ns]',color='k',fontsize=15,rotation=0) 
pl.ylabel('voltage [mV]',color='k',fontsize=15,rotation=90) 
pl.legend(loc="upper right")
pl.savefig("avewave.eps")
pl.show()
