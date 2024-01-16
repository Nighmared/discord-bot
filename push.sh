
#ONLY RUN FROM WITHIN SRC FOLDER
#author: nighmared
#version: 1

#here comes readme magic
bash update-readme.sh
black .
isort .

echo "Autoformatted and sorted imports 2/3"

pytest -x botpy
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

echo "Passed tests 3/3"

git add -u
git commit -S 
git push
