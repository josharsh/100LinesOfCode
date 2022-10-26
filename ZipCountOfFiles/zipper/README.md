
# File Zipper with Configurable File Count

This project will allow the user to zip all files in an entire directory. But that's not all! This project will allow the user to configure how many files go into the zip file and what the resulting zip files will be named. 


## Installation

Use your favorite java compilier to compile the program into a jar file. 

Or copy the supplied jar file and run it with java -jar.     

## FAQ

#### Question 1 How do I use this?

Answer 1 Enter at the command line the jar file name and the parameters.
The parameters for the project are
1) the maximum number of files to put into
each resulting .zip file.

2) the directory name you want to zip. This can be absolute or relative.

3) the file name you want to give all of your resulting zip files.

Example: java -jar zipper.jar 25 c:\users\user1\documents c:\users\user1\desktop\zips.zip

This will create zip files on the desktop named zips-#-#.zip

If the documents directory has 80 files in it, the resulting zip files will be:

zips-1-25.zip

zips-26-50.zip

zips-50-75.zip

zips-76-80.zip

#### Question 2 Why would I ever need this?

Answer 2 You probably won't, but I did when I wrote it originally because I was submitting
zip files to a website that would handle zips that had <= 100 files in it. I needed to submit over 8,000 files so
I created a program that would split them up into zip files that had a max of 100
files in them. 

## Feedback

If you have any feedback, please reach out to me at sjharper79@gmail.com.

## 🚀 About Me
I've been working in IT for almost 20 years. Before I started in IT, I was in college
for programming. I learned C and C++, VB.Net, and object oriented programming. 

Then I went to a school to learn about Windows computers and got a job as a Systems Engineer
where I did very little programming. Over the course of my 20 years in this career, I've learned a ton of stuff,
including programming in Java. Now I write programs for fun, but I'm also writing one for my work, even though I'm not a developer.