# Docker Volume S3 Backup

## Introduction
This is a script that gathers the data from a docker volume, compresses it and uploads it to a defined S3 bucket.

## Usage
This is meant to run as a cronjob repeatedly.
To run this:
* Git clone this.
* Set up the secrets.conf file. 
* Add the python file to your root user's crontab

# Helpful notes:
If you would like to save your secrets in your repository, you can GPG encrypt/decrypt your secrets :)

To encrypt: `gpg --symmetric --cipher-algo AES256 filename.ext`

To decrypt: `gpg --decrypt filename.ext.gpg > filename.ext`

