# Author
Rahmanu Hermawan
# About
In the beginning, this app is intended to be my wife's pregnancy log. She
measures her body weight and abdominal circuference every week. I got an idea
to created a very simple app which can do such thing. Log the data to a text file,
and everytime I add more data. The data will be displayed on the browser as plain text.
This app is served by my Raspberry Pi at home. So everytime I can access it :)

Lately, I think this app can be used more than that. It can be used to log everything, manually.
For example to log your diet program, you can log your weight throughout the program.
But again, this logger is a manual logger. So you need to input the data manually.

# Usage
To run the app, just type `node pregnancy-logger`, then open http://127.0.0.1:3000 
on your browser and log some data. For example, I want to log my weight: http://127.0.0.1:3000/72.6.
Then it will automatically add 72.6 kg to log.txt and show it to browser.
Not only that, this app can also log more data such as week number. For example
I want to log week and weight, it will be http://127.0.0.1:3000/28;72.6. Very simple.
