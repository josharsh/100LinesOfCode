#!/bin/bash

help_me () {
	echo "usage: ./change [-h] [-i] -f filename -s [-e] -mv [-cp] old_chars new_chars

Change the name of a given file

Interactive mode:
	-i 		interactive

If not interactive:
	-f, --file	specify the file
	-s, --start	characters at the start of the file
	-e, --end 	characters at the end of the file
	-mv 		use the \"mv\" command
	-cp		use the \"cp\" command

Example: $ ./change -i
Example: $ ./change -f hello_world -s -mv hello goodbye
Example: $ ./change -f hello_world -e -cp hello goodbye

Note: options must be given in this order

Todo: make filename upper or lower case

switch case = \${filename,}
all lowercase = \${filename,,}
capitalise = \${filename^}
all uppercase = \${filename^^}
Remove any matching characters, such as spaces
Replace any matching characters with something new, such as\"_\" to \"-\"
"
	exit
}

error_shown () (echo -e "-------------------\nInvalid option \"$1\"\n-------------------\n" )

swapping () {
	if [ $2 = 1 ]; then for i in $1; { $3 -v $i $5${i#$4}; }
	else for i in $1; { $2 -v $i ${i%$3}$4; }
	fi; exit
}

function interactive {
	read -p "Filename to change? `echo $'\n> '`" filename
	read -p "Would you like to change the start or the end of $filename [s/e]? `echo $'\n> '`" which_change

	if [ ${which_change,,} = "s" ]; then change_start=1
	elif [ ${which_change,,} = "e" ]; then change_end=1
	else error_shown $which_change; echo -e "You have options "s" or "e"\nPlease try again\n"; exit; fi

	read -p "Would you like to move or copy the file? [mv/cp]`echo $'\n> '`" cmd
	if [ ${cmd,,} = "mv" ]; then cmd="mv"
	elif [ ${cmd,,} = "cp" ]; then cmd="cp"
	else error_shown $cmd; echo -e "You have options \"mv\" or \"cp\"\nPlease try again\n"; exit
	fi
	read -p "What characters in \"$filename\" would you like to swap? `echo $'\n> '`" old_chars
	read -p "What characters would you like to replace \"$old_chars\" with? `echo $'\n> '`" new_chars

	swapping $filename $change_start $cmd $old_chars $new_chars
}

getting_args () {
	case $1 in
		-f | --file ) shift; filename=$1 ;;
		-i | --interactive ) interactive ;;
		-h | --help ) help_me ;;
		* ) error_shown $1; help_me ;;
	esac

	case $2 in -s | --start ) change_start=1 ;; -e | --end ) change_end=1 ;; * ) error_shown $2; help_me ;; esac

	case $3 in -mv ) cmd="mv";; -cp ) cmd="cp" ;; * ) error_shown $3; help_me ;; esac

	old_chars=$4; new_chars=$5
}

getting_args $@
swapping $filename $change_start $cmd $old_chars $new_chars
