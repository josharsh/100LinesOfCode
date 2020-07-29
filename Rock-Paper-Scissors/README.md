# Rock Paper Scissors #

## Description ##

Play more options than simple rock-paper-scissor, this script includes other options for
you to try.

## Author ##

[Swarag-N](https://github.com/Swarag-N)

## How to Play ##

Create a `rating.txt` file to store your score aganist computer.

```console
$python rock-paper-scissors.py
```

|Option|Description|
|---|---|
|`!rating`|Shows score of current user|
|`!exit`|Saves current score and exits|

Output:

``` code
$ python rock-paper-scissors.py
Enter Your name: Swarag
Hello, Swarag
Press Enter to cont. with default options or give options
rock,paper,wolf
Okay, let's start
wolf
There is a draw wolf
rock
Sorry, but computer chose paper
wolf
Sorry, but computer chose rock
!rating
Your rating:  50
!exit
Swarag 50
Data Saved
Bye!
```

```code
$ python rock-paper-scissors.py
Hello, Swarag
Loaded Score from Last Game
Press Enter to cont. with default options or give options

Okay, let's start
!rating
Your rating:  50
rock
Sorry, but computer chose paper
paper
Well done. Computer chose rock and failed
!exit
Swarag 150
Data Saved
Bye!
```
