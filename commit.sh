git add .
mydate= date "+%Y-%m-%d-%H:%M:%S.%N"
echo $mydate
git commit -m `date +%Y-%m-%d-%H-%M-%s`-arlier
git push -u origin master
