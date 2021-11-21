
#ONLY RUN FROM WITHIN SRC FOLDER
#author: nighmared
#version: 1

#here comes readme magic
r_top=$(cat ../README_TEXT.md)
struct=$(bash dotree.sh)
echo "">../README.md #clean
cat ../README_TEXT.md>>../README.md
echo $' \n\n ``` \n'>>../README.md
bash dotree.sh>>../README.md
echo $' ``` \n'>>../README.md
echo "Updated tree part of README 1/2"


pytest -x
retcode=$?
if [ $retcode != 0 ]
then
	echo "\033[0;31m"
	echo ""
	echo "***************************"
	echo "\nSomething went wrong with the tests, not pushing!\n"
	echo ""
	echo "***************************"
	echo "\033[0m"
	return 1
fi

echo "Passed tests 2/2"

git add -u
git commit -S 
git push
