# Change a filename
This is a bash script which allows you to change the start or end of your filename

This can be done either via an interactive method, or by using command line flags

# Author
[EuanB26](https://github.com/EuanB26)

# Usage
I've given examples in the code, however, if you need a refresh
```bash
$ ./change -i
$ ./change -f hello_world -s -mv hello goodbye
$ ./change -f hello_world -e -cp hello goodbye
```
*Please note: command line flags must be given in this order*

## Command line flags
```sh
Interactive mode:
	-i 		interactive

If not interactive:
	-f, --file	specify the file
	-s, --start	characters at the start of the file
	-e, --end 	characters at the end of the file
	-mv 		use the "mv" command
	-cp		use the "cp" command
```

# Output
## Command line arguments
```sh
$ ls
change_filename.sh hello_world
$ ./change_filename.sh -f hello_world -s -cp hello goodbye
'hello_world' -> 'goodbye_world'
$ ls
change_filename.sh  goodbye_world  hello_world
```
## Interactive
```sh
$ ls
change_filename.sh hello_world
$ ./change_filename.sh -i       
Filename to change? 
> hello_world
Would you like to change the start or the end of hello_world [s/e]? 
> s
Would you like to move or copy the file? [mv/cp]
> mv
What characters in "hello_world" would you like to swap? 
> hello
What characters would you like to replace "hello" with? 
> new
renamed 'hello_world' -> 'new_world'
$ ls
change_filename.sh  new_world
```
