#!/bin/bash
#PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
cd /media/tao/_dde_data/arlierwork
git add .
#mydate= date "+%Y-%m-%d-%H:%M:%S.%N"
#echo $mydate
git commit -m `date +%Y-%m-%d-%H-%M-%s`-arlier
git push -u origin master
