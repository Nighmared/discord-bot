
echo "">README.md #clean
cat README_TEXT.md>>README.md
echo $' \n\n ``` \n'>>README.md
bash dotree.sh>>README.md
echo $' ``` \n'>>README.md
echo "Updated tree part of README 1/3"
