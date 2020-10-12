#!/bin/bash

set -e
sed -e 's/:[^:\/\/]/="/g;s/$/"/g;s/ *=/=/g' credentials.yaml > file.sh
source file.sh
python create.py $1
cd $path/$1
ls
git init
git remote add origin git@github.com:$github_username/$1.git
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin master
code .
