# r/Politics Scraper

## Requirements:
You'll need to have Selenium, pandas, time, and bs4 installed on your system.

## Instructions:
In order to run this program, please first install the packages listed above. Afterwards, you will need
to also install the Selenium Chrome web driver (or a different browser of your choosing -- although this 
will require additional changes to be made to the program) and modify the path specified on line 12 to point 
to the path location of the web driver on your machine. 

https://chromedriver.chromium.org/downloads

## What does this program do?

This program scrapes the top results on the r/politics webpage and creates a CSV file with the count of each word
listed in the thread titles. It automatically sorts the words from highest frequency to lowest and can be used 
to visually inspect what topics are trending in politics at that given point in time. The CSV file should be created in the working
directory that the rpolitics_scraper.py file is located in.

