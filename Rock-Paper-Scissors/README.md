# Rock Paper Scissors #

## Description ##
<Rock-Paper-Scissors, Swarag-N>

Project Description:
An extension of the traditional game of rock-paper-scissors with more options the user can choose from. User will play against the computer that will randomly generate a move. The results of who won or lost or if the result was a draw will be printed. The user's score will be saved and updated after each round, and the user can access the score anytime. 

Project Idea: An extension of the traditional game of rock-paper-scissors with more options while playing against a random generator.

Project Implementation: This project is written in Python and is played in the console.

Source code: N/A

Link to app: N/A


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
