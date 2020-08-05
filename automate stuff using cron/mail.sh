#!/bin/sh
 
MAILFILE=path/to/mail/file #if you want extra messages like logs
echo -e "Subject: Machine turned on @ `date`\nTo: toEmail"  
echo "\n" >> $MAILFILE
echo "Have a nice day !" >> $MAILFILE 
cat $MAILFILE | ssmtp toEmail
rm $MAILFILE
