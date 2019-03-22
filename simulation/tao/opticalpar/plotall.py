#!/usr/bin/env python
# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
import pylab as pl
f = open('/media/tao/_dde_data/arlierwork/simulation/tao/opticalpar/ej200out.txt')
f1 = open('/media/tao/_dde_data/arlierwork/simulation/tao/opticalpar/pmtout.txt')
s = f.readline()
s1 = f1.readline()
a1=[]
a2=[]
b1=[]
b2=[]
count=0
while (count<301):
     arr=s.split(' ')
     arr1=s1.split(' ')
#     print arr
#     print arr[1]
#     a1=arr[0]
     a1.append(float(arr[0]))
     b1.append(float(arr1[0]))
     a2.append(float(arr[1].replace('\r\n',''))) #readline 读取文件的时候，默认加上“\n"
     b2.append(float(arr1[1].replace('\r\n',''))/100.) #readline 读取文件的时候，默认加上“\n"
#     a2=arr[1].replace('\n','') #readline 读取文件的时候，默认加上“\n"
     s=f.readline()
     s1=f1.readline()
     count+=1
pl.figure(figsize=(8,8))
#axes = pl.plot(111)
fig=pl.plot(a1,a2,".",label='emission spectrum of EJ-200',c=(0,0.0,0.0),alpha=0.5,linestyle="-")
pl.suptitle('EJ-200 Emission Spectrum and PMT Response')
#pl.plot(x,y,"ro",label='the original data',c=(1,0.2,0.5),alpha=0.5)
pl.style.use('ggplot')
#pl.grid(axis='x')
pl.grid(True)
#pl.grid(color='g',linewidth=2,alpha=0.2,ls='--',lw=1)
#pl.axis([350,550,0,1])
pl.xlabel('wavelength [nm]',color='k',fontsize=15,rotation=0) 
pl.ylabel('light output [A.U]',color='k',fontsize=15,rotation=90) 
pl.plot(b1,b2,".",label='PDE of PMT XP3232',color='g',alpha=0.5,linestyle="-")
pl.legend(loc="upper right")
pl.savefig("allplot.eps")
pl.show()

