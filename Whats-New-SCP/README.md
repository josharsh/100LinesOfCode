# What's New SCP

This is a bash script for downloading new files from a remote directory. 

## Purpose

When running a file server, there can be many files on the server, and a user often only wants to download the newest files since they last accessed the server. Although applications like rsync can help download only new files, I wanted to try writing a bash script for accomplishing this task. Using ssh and scp, this script will automatically download all new files located on a remote file server since the last time that the application was run.

## Usage

To use the application, run the `whats-new` file from a terminal by typing `./whats-new`. If this is the first time that the script has been run, there will be an initial setup phase for entering the IP address of the server, username for ssh login, directory to download files to, directory to watch for new files, and which SSH key to use for login. After this, any time that the script is run, all new files will be downloaded in the watched folder since last time the script is run. It is recommended to use an SSH key without a passphrase on it since the `ssh` and `scp` commands are called multiple times in the script, so it would be annoying to have to constantly type in a passphrase.

## Future Ideas for Improvement

* Ability to unselect specific files to avoid downloading them
* Design a better interface for navigating the application using tput
* Only require that the user enters SSH key passphrase one single time
