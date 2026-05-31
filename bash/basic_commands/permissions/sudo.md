sudo su -
The above command requires a password to run any commands with sudo.
 There are certain occasions where we may be allowed to execute certain 
applications, or all applications, without having to provide a password:



sudo -l

    (user : user) NOPASSWD: /bin/echo



sudo -u user /bin/echo Hello World!

    Hello World!



user1 auf user2 wechseln syntax (das was bei htb funktioniert hat)

sudo -su user2
