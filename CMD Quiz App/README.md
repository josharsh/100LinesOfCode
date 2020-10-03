# CMD Quiz App
A simple quiz app on command line interface using golang

# Packages used
- encoding/csv
- flag
- fmt
- os
- strings
- time

# How to use the app
Execute the `main.go` file using the `go run main.go` command.<br>
By default the questions are provided from `problems.csv` file but the user can provide their own questions using the `--csv` flag then path to the file.<br>
The user is given 30 seconds to complete the exercise but that time limit can also be changed by providing the `--limit` flag then the time limit of the test.<br>
At the end of the test the user is shown the answers given, whether they were correct or not and the correct answer and the number of correct answers and the time taken by the user to complete the whole test.<br>
User can use `-h` flag to know more about the flags in the program

# Working
- `flag` package is used to handle inputs from flags provided by the user.
- `encoding/csv` package is used to read and parse csv files
- `time` package and `channels` are used to maintain proper handling of time limits of the quiz