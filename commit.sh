git add .
mydate= date +%F 
echo $mydate
git commit -m '$mydate'
git push -u origin master
