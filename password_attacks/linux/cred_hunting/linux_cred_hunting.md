# SEARCHING FILES
```
for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done
for i in $(find / -name *.cnf 2>/dev/null | grep -v "doc\|lib");do echo -e "\nFile: " $i; grep "user\|password\|pass" $i 2>/dev/null | grep -v "\#";done
```


# SEARCHING DATABASES
```
for l in $(echo ".sql .db .*db .db*");do echo -e "\nDB File extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share\|man";done
```


# SEARCHING NOTES
```
find /home/* -type f -name "*.txt" -o ! -name "*.*"
```

            
# SEARCHING SCRIPTS
```
for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share";done
```


# ENUMERATING CRONJOBS
```
cat /etc/crontab
ls -la /etc/cron.*/
```


# ENUMERATING HISTORY FILE
```
i.e. .bash_history .bashrc or .bash_profile
tail -n5 /home/*/.bash*
```


# ENUMERATING LOG FILES
```
for i in $(ls /var/log/* 2>/dev/null);do GREP=$(grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null); if [[ $GREP ]];then echo -e "\n#### Log file: " $i; grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null;fi;done
```


# LAZAGNE
```
https://github.com/AlessandroZ/LaZagne
sudo python2.7 laZagne.py all
```


# READING MEMORY (ROOT NEEDED)
```
https://github.com/huntergregal/mimipenguin
sudo python3 mimipenguin.py
```


# BROWSER DECRYPT TOOLS
```
https://github.com/unode/firefox_decrypt
ls -l .mozilla/firefox/ | grep default
cat .mozilla/firefox/1bplpd86.default-release/logins.json | jq .
```











    
