# python-mail
Python SMTP client for sending mail using python CLI

<b>ASSETS:</b> <br>
Assets directory consists of following files and directory:<br>1. contacts.txt -> this is the list of contacts in the format name email-id<br>2. message.txt -> this file consists of a template. You can edit this file with your content.<br>3. ASSETS consists of a subdir 'cache' which will cache the failed mails

<b>LOGS:</b> <br>
This directory consists of mailinglog.log file generated from python logging module.

<b>USAGE:</b> <br>
To run the program, run 
```
$python main.py
```

To run, you may have to change **host** and **port** as per your mail provider in ```mailer.py``` in line 11<br>
```s = smtplib.SMTP(host='smtp.gmail.com', port=587)```
