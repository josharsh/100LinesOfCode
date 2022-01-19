#!/bin/bash

textbook_name=$1
num=$2
field_box=()

if [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then
    echo
    echo `basename $0` " [filename_param]  [integer_param]"
    echo -e "\n"
    echo '    '`basename $0`" is a script that takes as first parameter the name of a .txt file,"
    echo '    '"as a second parameter a positive integer N, greater than 0"
    echo '    '"and returns the N most seen words that are included in the .txt file"
    echo -e "\n"
    exit 0
fi




while read line; do
IFS=' |-' 
read -ra stringarray <<< "$line"

for i in "${stringarray[@]}"; do
	
	result1=
	for (( j=0; j<${#i}; j++ )); do
  		currChar=${i:$j:1}
  		
  		if [[ "$currChar" == "'" ]]; then
  			i=${i%\'*}
  		fi
  		
  		if [[ "$currChar" =~ [a-zA-Z] ]];then
  			if [[ "$currChar" =~ [A-Z] ]]; then
  				currChar=${currChar,,}
			fi
  			
  			result1=$result1$currChar
		fi
  		
  		
	done;
	
	if ! [ -z "$result1" ]; then
		field_box+=("$result1")

	fi
done;

done <"$textbook_name"

> "appendmode.txt"
for i in "${field_box[@]}"
do
: 

echo -n $i" " >> "appendmode.txt"
done

sed -e 's/\s/\n/g' < "appendmode.txt" | sort | uniq -c | sort -nr | head  -$num | sed -E 's/(.*) (.*)/\2 \1/'
rm "appendmode.txt"
