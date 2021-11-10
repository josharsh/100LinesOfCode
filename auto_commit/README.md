# Auto_Commit 
## Description:

This is a bash script for commiting changes after specified interval automatically. Just run the script and start working on your project it will autocommits changes you have made, after interval specified by you.

## Get Started

1- Download script and open your favourite terminal.
2- Run following command to make this script executeable if not already.
NOTE: Replace "< text >" with real arguments.
```

chmod u+x <path to file>/auto_commit.sh

```
Example:

![Screenshot from 2021-09-21 17-33-55](https://user-images.githubusercontent.com/53839118/134172801-5a7e9cc2-7c7e-4d57-9885-338c590be10b.png)


3- Run watch command with this script and specify the time interval. Also pass the path of repository you will be making changes in.
```

watch -n300 <path to script file> <path to local repository>

```
![Screenshot from 2021-09-21 17-36-14](https://user-images.githubusercontent.com/53839118/134173143-523c601f-100c-4c26-b8cd-68b19be55296.png)

Here -n300 means script will check for commits after every 300 seconds or 5 min. You can also see more options by reading man pages by command:
```
man watch

```
running script will look like:
if no commits detected
![Screenshot from 2021-09-21 17-36-25](https://user-images.githubusercontent.com/53839118/134173678-ebaad5cb-a8f2-4a46-a3c8-8bfcc0d1f3b1.png)

and if commits detected

![Screenshot from 2021-09-21 17-38-12](https://user-images.githubusercontent.com/53839118/134173769-ba74d623-7360-42da-9d52-4b5aa0bc4dac.png)


