
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
git add -u
git commit -S 
git push
