from datetime import datetime
import os

def setup():
    #check if the specific hidden file exists
    if os.path.isfile(".duck"):
        print("Quack Quack!")
        #read the file put it in cmd
        with open(".duck", "r") as file:
            cmd = file.readline()
        return cmd
    #if not, create it
    FILE_NAME = input("Enter the file name: ")
    TXED = input("Which text editor do you want to use: ")
    cmd = TXED + " " + FILE_NAME
    with open(".duck", "w") as duck:
        duck.write(cmd)
    return cmd

def main():
    cmd = setup()
    #remove the first word from the command
    FILE_NAME = cmd.partition(" ")[2]

    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    hour = now.hour
    minute = now.minute
    second = now.second
    day_of_week = now.weekday()
    with open(FILE_NAME, "a") as duck:
        duck.write("Me to Duck on " + str(day_of_week) + ": " + str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second) + os.linesep)
    os.system(cmd)

if __name__ == "__main__":
    main()