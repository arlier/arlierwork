git add .
mydate= date "+%Y-%m-%d %H:%M:%S.%N"
echo $mydate
git commit -m '$mydate'
git push -u origin master
