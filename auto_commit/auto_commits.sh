#!/bin/bash
repo=$1
cd "$repo"
git add .
modified=$(git status | grep 'modified' | sed 's/modified:/ /g' )

d=$(date +"%I:%M %P")    
if [ -z $modified ]; then
    echo "$d : nothing to commit"
else
    echo "$d : modified "$modified
    git commit -m "modified: $modified"
fi

